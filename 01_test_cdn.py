#!/usr/bin/env python3
"""
测试 npm 包 xijie-m24 在多个 CDN 镜像上的可用性。
用法: python test_cdn.py
依赖: Python 3.7+ 标准库（无需安装第三方包）
"""

import json
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

PACKAGE = "xijie-m24"
RESOURCE = "images/joined-github.svg"
TIMEOUT = 15
MAX_WORKERS = 8


def get_latest_version(package):
    """从 npm registry 获取最新版本号，用于 ZStatic（不支持 @latest）。"""
    url = f"https://registry.npmjs.org/{package}/latest"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.load(resp)
            return data.get("version")
    except Exception as e:
        print(f"[警告] 获取 {package} 最新版本号失败: {e}")
        return None


def build_targets():
    """构建待测试的 (名称, URL) 列表。"""
    targets = [
        # 基于 jsDelivr 的镜像
        ("jsdmirror.cn", f"https://cdn.jsdmirror.cn/npm/{PACKAGE}@latest/{RESOURCE}"),
        (
            "jsdelivr.net.cn",
            f"https://cdn.jsdelivr.net.cn/npm/{PACKAGE}@latest/{RESOURCE}",
        ),
        (
            "jsdelivr.b-cdn.net",
            f"https://jsdelivr.b-cdn.net/npm/{PACKAGE}@latest/{RESOURCE}",
        ),
        # 基于 UNPKG 的镜像
        ("南科大", f"https://mirrors.sustech.edu.cn/unpkg/{PACKAGE}@latest/{RESOURCE}"),
        ("饿了么", f"https://npm.elemecdn.com/{PACKAGE}@latest/{RESOURCE}"),
        ("知乎", f"https://unpkg.zhimg.com/{PACKAGE}@latest/{RESOURCE}"),
        ("LuckinCDN", f"https://unpkg.luckincdn.com/{PACKAGE}@latest/{RESOURCE}"),
        ("迷你玩", f"https://pkg.mini1.cn/{PACKAGE}@latest/{RESOURCE}"),
        # 其他
        ("oncdn.cn", f"https://npm.oncdn.cn/{PACKAGE}@latest/{RESOURCE}"),
        ("iocdn.cc", f"https://cdn.iocdn.cc/npm/{PACKAGE}@latest/{RESOURCE}"),
        ("boochi.cn", f"https://cdn.boochi.cn/npm/{PACKAGE}@latest/{RESOURCE}"),
    ]

    # ZStatic 需要精确版本号
    version = get_latest_version(PACKAGE)
    if version:
        targets.append(
            ("ZStatic", f"https://s4.zstatic.net/npm/{PACKAGE}@{version}/{RESOURCE}")
        )
    else:
        print("[提示] 未获取到版本号，跳过 ZStatic 测试")

    return targets


def test_one(item):
    """测试单个 URL。"""
    name, url = item
    start = time.time()
    status = None
    ctype = ""
    size = ""
    svg_ok = False
    error = ""
    final_url = url

    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "*/*",
                "Accept-Encoding": "identity",
            },
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            status = resp.status
            final_url = resp.geturl()
            ctype = resp.headers.get("Content-Type") or ""
            size = resp.headers.get("Content-Length") or ""
            data = resp.read(1024 * 1024)  # 最多读 1MB，足够判断 SVG
            svg_ok = b"<svg" in data.lower()
    except urllib.error.HTTPError as e:
        status = e.code
        ctype = e.headers.get("Content-Type") or ""
        size = e.headers.get("Content-Length") or ""
        try:
            data = e.read(2048)
            svg_ok = b"<svg" in data.lower()
        except Exception:
            pass
        error = f"HTTP {e.code}"
    except urllib.error.URLError as e:
        error = f"URLError: {e.reason}"
    except TimeoutError:
        error = "Timeout"
    except Exception as e:
        error = f"{type(e).__name__}: {e}"

    elapsed = (time.time() - start) * 1000

    if status is None:
        status_str = "ERR"
    else:
        status_str = str(status)

    if not size:
        size = "-"
    if error:
        ctype = error[:20]

    return {
        "name": name,
        "url": url,
        "status": status_str,
        "elapsed": elapsed,
        "ctype": ctype,
        "size": size,
        "svg_ok": svg_ok,
        "error": error,
        "final_url": final_url,
    }


def main():
    targets = build_targets()
    print(f"测试包: {PACKAGE}")
    print(f"资源: {RESOURCE}")
    print(f"目标数量: {len(targets)}\n")

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_item = {executor.submit(test_one, item): item for item in targets}
        for future in as_completed(future_to_item):
            results.append(future.result())

    # 按原始顺序排序
    order = {item[0]: i for i, item in enumerate(targets)}
    results.sort(key=lambda r: order.get(r["name"], 999))

    # 打印表头
    header = f"{'名称':<18} {'状态':<5} {'耗时(ms)':>9} {'类型':<22} {'大小(B)':>8} {'SVG':<4} URL"
    print(header)
    print("-" * 120)

    success = []
    for r in results:
        svg_flag = "yes" if r["svg_ok"] else "no"
        line = (
            f"{r['name']:<18} {r['status']:<5} {r['elapsed']:>9.0f} "
            f"{r['ctype']:<22} {r['size']:>8} {svg_flag:<4} {r['url']}"
        )
        print(line)
        if r["status"] == "200" and r["svg_ok"]:
            success.append(r["url"])

    print("\n" + "=" * 60)
    print(f"成功: {len(success)} / {len(results)}")
    if success:
        print("\n可用的链接:")
        for url in success:
            print(url)
    else:
        print("没有成功获取到 SVG 内容的链接。")


if __name__ == "__main__":
    main()


"""
可用的链接:
https://cdn.jsdmirror.cn/npm/xijie-m24@latest/images/joined-github.svg
https://cdn.jsdelivr.net.cn/npm/xijie-m24@latest/images/joined-github.svg
https://pkg.mini1.cn/xijie-m24@latest/images/joined-github.svg
"""
