import concurrent.futures
import time

import requests

# 1. 定义要测试的 CDN 字典
cdns = {
    "unpkg (官方基线)": "https://unpkg.com/xijie-m24@latest/images/joined-github.svg",
    "jsDelivr (官方基线)": "https://cdn.jsdelivr.net/npm/xijie-m24@latest/images/joined-github.svg",
    "饿了么 (Eleme)": "https://npm.elemecdn.com/xijie-m24@latest/images/joined-github.svg",
    "知乎 (Zhihu)": "https://unpkg.zhimg.com/xijie-m24@latest/images/joined-github.svg",
    "Zstatic": "https://s4.zstatic.net/npm/xijie-m24@latest/images/joined-github.svg",
    "渺软公益 (UNPKG)": "https://npm.onmicrosoft.cn/xijie-m24@latest/images/joined-github.svg",
    "初七云 / CBD": "https://cdn.cbd.int/xijie-m24@latest/images/joined-github.svg",
    "chuqis 公益": "https://cdn.chuqis.com/npm/xijie-m24@latest/images/joined-github.svg",
}

# 淘宝镜像 URL (注意路径中多了 /files/)
npmmirror_url = (
    "https://registry.npmmirror.com/xijie-m24/latest/files/images/joined-github.svg"
)


def test_cdn(name, url, headers):
    """执行单次 CDN 请求测试"""
    start_time = time.time()
    try:
        # 发送 GET 请求
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        elapsed = (time.time() - start_time) * 1000

        # 判断状态
        if response.status_code == 200:
            # 核心校验：确保返回的是真正的 SVG，而不是 200 状态的 HTML 错误页
            content_type = response.headers.get("Content-Type", "")
            if "image/svg" in content_type or b"<svg" in response.content[:100]:
                status = "✅ 成功 (可用)"
            else:
                status = "⚠️ 异常 (非SVG文件)"
        else:
            status = f"❌ 失败 (HTTP {response.status_code})"

        return {
            "name": name,
            "status": status,
            "time": f"{elapsed:.0f} ms",
            "size": f"{len(response.content)} B",
            "type": response.headers.get("Content-Type", "Unknown"),
        }
    except Exception as e:
        elapsed = (time.time() - start_time) * 1000
        return {
            "name": name,
            "status": f"❌ 报错: {type(e).__name__}",
            "time": f"{elapsed:.0f} ms",
            "size": "N/A",
            "type": "N/A",
        }


def main():
    # 准备请求头 (模拟真实浏览器)
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    base_headers = {"User-Agent": ua}
    # 模拟从 GitHub 跨域请求 (用于测试 npmmirror 的 Referer 防盗链)
    referer_headers = {**base_headers, "Referer": "https://github.com/"}

    results = []
    print("🚀 开始测试 npm CDN 节点 (目标: xijie-m24/joined-github.svg)...\n")

    # 使用线程池并发测试，提高效率
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = []

        # 提交常规 CDN 测试任务
        for name, url in cdns.items():
            futures.append(executor.submit(test_cdn, name, url, base_headers))

        # 提交淘宝 npmmirror 对照测试 (带 Referer vs 无 Referer)
        futures.append(
            executor.submit(
                test_cdn, "淘宝npmmirror(带Referer)", npmmirror_url, referer_headers
            )
        )
        futures.append(
            executor.submit(
                test_cdn, "淘宝npmmirror(无Referer)", npmmirror_url, base_headers
            )
        )

        # 收集结果
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    # 打印格式化表格
    print(
        f"{'CDN 节点名称':<25} | {'测试结果':<20} | {'耗时':<10} | {'文件大小':<12} | Content-Type"
    )
    print("-" * 110)
    for r in sorted(results, key=lambda x: x["name"]):
        # 简单的终端对齐输出
        print(
            f"{r['name']:<20} | {r['status']:<18} | {r['time']:<7} | {r['size']:<10} | {r['type']}"
        )


if __name__ == "__main__":
    main()

"""
🚀 开始测试 npm CDN 节点 (目标: xijie-m24/joined-github.svg)...

CDN 节点名称                  | 测试结果                 | 耗时         | 文件大小         | Content-Type
--------------------------------------------------------------------------------------------------------------
Zstatic              | ❌ 报错: ConnectionError | 4539 ms | N/A        | N/A
chuqis 公益            | ❌ 报错: ConnectionError | 78 ms   | N/A        | N/A
jsDelivr (官方基线)      | ✅ 成功 (可用)          | 1988 ms | 32864 B    | image/svg+xml
unpkg (官方基线)         | ✅ 成功 (可用)          | 2647 ms | 32864 B    | image/svg+xml
初七云 / CBD            | ✅ 成功 (可用)          | 4728 ms | 32864 B    | image/svg+xml
淘宝npmmirror(带Referer) | ❌ 失败 (HTTP 403)    | 1611 ms | 140 B      | application/json; charset=utf-8      
淘宝npmmirror(无Referer) | ❌ 失败 (HTTP 403)    | 1917 ms | 140 B      | application/json; charset=utf-8      
渺软公益 (UNPKG)         | ❌ 报错: ConnectionError | 57 ms   | N/A        | N/A
知乎 (Zhihu)           | ❌ 失败 (HTTP 404)    | 1303 ms | 9 B        | text/plain; charset=utf-8
饿了么 (Eleme)          | ❌ 失败 (HTTP 404)    | 1401 ms | 427 B      | application/xml

"""
