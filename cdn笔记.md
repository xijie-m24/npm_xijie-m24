# 加速 github 仓库里的资源

## github 官方

> 示例路径：https://github.com/xijie-m24/npm_xijie-m24/blob/main/images/bg001.jpg  
> 推荐：https://raw.githubusercontent.com/xijie-m24/npm_xijie-m24/main/images/bg001.jpg

```txt
# 示例链接：
https://github.com/xijie-m24/npm_xijie-m24/blob/main/images/bg001.jpg?raw=true   --------》302重定向
https://github.com/xijie-m24/npm_xijie-m24/raw/main/images/bg001.jpg   -------------------》302重定向
https://raw.githubusercontent.com/xijie-m24/npm_xijie-m24/main/images/bg001.jpg
https://raw.githubusercontent.com/xijie-m24/npm_xijie-m24/refs/heads/main/images/bg001.jpg
```

## gh-proxy 镜像站

> 示例路径：https://github.com/xijie-m24/npm_xijie-m24/blob/main/images/bg001.jpg  
> gh-proxy 官网(教程)：https://gh-proxy.com/  
> 推荐：https://v4.gh-proxy.org/https://raw.githubusercontent.com/xijie-m24/npm_xijie-m24/main/images/bg001.jpg

```txt
# 示例链接：
https://gh-proxy.com/github.com/xijie-m24/npm_xijie-m24/blob/main/images/bg001.jpg
https://gh-proxy.com/raw.githubusercontent.com/xijie-m24/npm_xijie-m24/main/images/bg001.jpg

https://gh-proxy.org/https://raw.githubusercontent.com/xijie-m24/npm_xijie-m24/main/images/bg001.jpg   -----》主站
https://v4.gh-proxy.org/https://raw.githubusercontent.com/xijie-m24/npm_xijie-m24/main/images/bg001.jpg
https://cdn.gh-proxy.org/https://raw.githubusercontent.com/xijie-m24/npm_xijie-m24/main/images/bg001.jpg   -----》Fastly CDN 节点加速
```

## jsDelivr 官方

> 推荐：fastly.jsdelivr.net

```txt
# 示例链接(github资源)：
https://cdn.jsdelivr.net/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg   -------》自动调度后端
https://fastly.jsdelivr.net/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg
https://quantil.jsdelivr.net/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg
https://gcore.jsdelivr.net/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg
https://testingcf.jsdelivr.net/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg
```

## jsDelivr 第三方加速

> 推荐：cdn.jsdmirror.com

```txt
# JSDMirror
https://cdn.jsdmirror.com/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg

# 渺软公益CDN
https://jsd.onmicrosoft.cn/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg

# cdn.bili33.top（哔哩 CDN）
https://cdn.bili33.top/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg

# 渝伴 CDN
https://cdn.osyb.cn/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg

# “晓白”/ AKASS CDN
https://jsd.akass.cn/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg


https://cdn.jsdmirror.cn/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg
https://cdn.jsdelivr.net.cn/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg
https://jsdelivr.b-cdn.net/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg

```

# 加速 npm 资源

```txt
# npm官方
https://unpkg.com/xijie-m24@latest/images/joined-github.svg

# jsDelivr系列（官方）
https://cdn.jsdelivr.net/npm/xijie-m24@latest/images/joined-github.svg
https://fastly.jsdelivr.net/npm/xijie-m24@latest/images/joined-github.svg
https://quantil.jsdelivr.net/npm/xijie-m24@latest/images/joined-github.svg
https://gcore.jsdelivr.net/npm/xijie-m24@latest/images/joined-github.svg
https://testingcf.jsdelivr.net/npm/xijie-m24@latest/images/joined-github.svg

# jsDelivr系列（非官方）
https://cdn.jsdmirror.com/npm/xijie-m24@latest/images/joined-github.svg
https://jsd.onmicrosoft.cn/npm/xijie-m24@latest/images/joined-github.svg
https://cdn.bili33.top/npm/xijie-m24@latest/images/joined-github.svg
https://cdn.osyb.cn/npm/xijie-m24@latest/images/joined-github.svg
https://jsd.akass.cn/npm/xijie-m24@latest/images/joined-github.svg

https://cdn.jsdmirror.cn/npm/xijie-m24@latest/images/joined-github.svg
https://cdn.jsdelivr.net.cn/npm/xijie-m24@latest/images/joined-github.svg
https://jsdelivr.b-cdn.net/npm/xijie-m24@latest/images/joined-github.svg

# 其他
https://npm.webcache.cn/xijie-m24@latest/images/joined-github.svg -------》会自动转换latest------>阿里云CDN加速
https://npm.akass.cn/xijie-m24@latest/images/joined-github.svg
https://pkg.mini1.cn/xijie-m24@latest/images/joined-github.svg ----------》会自动转换latest
https://unpkg.luckincdn.com/xijie-m24@1.2.1/images/joined-github.svg -----》会自动转换latest
https://cdn.cbd.int/xijie-m24@latest/images/joined-github.svg -----------》会自动转换latest------->初七云

```

# 其他 2

```txt
https://npm.elemecdn.com/ylan-blog@latest/  -----------》为什么我的npm包不行呢？
https://npm.elemecdn.com/xijie-m24@latest/

https://npm.webcache.cn/xijie-m24@latest/   ------------》自动跳转到，访问挺快。查看包的文件结构
https://explore.webcache.cn/xijie-m24@1.2.1

https://registry.npmjs.org/xijie-m24
https://registry.npmjs.org/xijie-m24/latest
https://registry.npmjs.org/xijie-m24/1.2.1   ----------》返回一个json对象


# 缓存刷新：purge 接口
https://purge.jsdelivr.net/gh/{user}/{repo}@{ref}/{path}
https://purge.jsdelivr.net/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg

```
