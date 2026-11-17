# xijie-m24

A personal static assets repository hosted on npm, served through unpkg & jsDelivr CDN.

一个托管在 npm 上的个人静态资源仓库，通过 unpkg / jsDelivr CDN 访问。

- **GitHub**: https://github.com/xijie-m24/npm_xijie-m24
- **npm**: https://www.npmjs.com/package/xijie-m24

---

## 🖼️ 图片访问链接

### 通过 unpkg 和 jsDelivr 来访问npm包中的资源

- **unpkg**
  ```
  https://unpkg.com/xijie-m24@latest/images/joined-github.svg
  ```
- **jsDelivr**
  ```
  https://cdn.jsdelivr.net/npm/xijie-m24@latest/images/joined-github.svg
  https://fastly.jsdelivr.net/npm/xijie-m24@latest/images/joined-github.svg
  ```

> 💡 生产环境建议用**具体版本号**（如 `@1.0.0`）替代 `@latest`，避免内容变动带来的风险。

### 访问github仓库里的资源

- **GitHub 官方 Raw 链接（直链）**
  ```
  https://raw.githubusercontent.com/xijie-m24/npm_xijie-m24/main/images/joined-github.svg
  ```
- **jsDelivr CDN 链接（🌟 强烈推荐）**
  ```
  https://cdn.jsdelivr.net/gh/xijie-m24/npm_xijie-m24@main/images/joined-github.svg
  ```

> 💡 由于 GitHub 官方直链在某些地区（如中国大陆）访问可能较慢或不稳定，通常推荐使用免费的 **jsDelivr** CDN 来加速 GitHub 资源。

---

## 📦 npm 常用命令笔记

### 账号 / 登录

```bash
# 前提：确保使用的npm官方镜像源
npm login --registry https://registry.npmjs.org/    # 登录 npm，--registry指定官方镜像源
npm whoami                  # 查看当前登录用户，也需注意镜像源
npm logout                  # 退出登录
```

### 发布 / 版本管理

```bash
npm pack --dry-run          # 预览将被打包的文件（发布前必查）
npm publish                 # 发布无作用域包
npm publish --access public # 发布作用域包（如 @xijie-m24/xxx）时需加

npm version patch           # 1.0.0 → 1.0.1（修 bug）
npm version minor           # 1.0.0 → 1.1.0（新增功能，向后兼容）
npm version major           # 1.0.0 → 2.0.0（不兼容变更）

npm deprecate <pkg>@<ver> "<msg>"  # 弃用某个版本
npm unpublish <pkg>@<ver>          # 撤销发布（72 小时内有效）

npm pack vue --dry-run  # 预览远程包（如 vue）打包的文件
```

### 查看信息

```bash
# npm view是联网查看（例：npm view vue）
npm view xijie-m24          # 查看包信息
npm view xijie-m24 versions # 查看所有已发布版本，优先本地缓存（未过期时）
npm view xijie-m24 versions --prefer-online  # 强制远程 Registry（网络优先）
npm view xijie-m24 files    # 查看包内文件列表，白名单机制，package.json 中的 files 字段
npm view xijie-m24 dependencies  # 查看依赖项
npm view xijie-m24 --json   # 查看完整 package.json 信息

npm view vue main
npm view vue module
```

---

## 🌱 Git 常用命令笔记

### 初始化 / 关联远程

```bash
git init
git remote add origin git@github.com:xijie-m24/npm_xijie-m24.git
git remote set-url origin git@xxxxx:xijie-m24/npm_xijie-m24.git    # 修改origin
git remote -v               # 查看远程地址
git branch -M main          # 重命名主分支为 main
```

### 提交 / 推送

```bash
git status                  # 查看工作区状态
git add .                   # 暂存所有改动
git add <file>              # 暂存指定文件
git commit -m "msg"         # 提交
git push -u origin main     # 首次推送并建立跟踪
git push                    # 后续推送
```

### 拉取 / 同步

```bash
git pull                    # 拉取并合并
git fetch                   # 只拉取不合并
```

### 其他

```bash
git log --oneline --graph   # 简洁历史图
git diff                    # 查看未暂存改动
git restore <file>          # 撤销工作区修改
git reset --soft HEAD~1     # 撤销最近一次提交（保留改动）
```

---

## 🚀 从 0 到发布：完整流程

```bash
# 1. 初始化 git 并关联 GitHub（SSH）
git init
git remote add origin git@github.com:xijie-m24/npm_xijie-m24.git
git branch -M main

# 2. 首次提交并推送
git add .
git commit -m "init: add images and project config"
git push -u origin main

# 3. 登录 npm
npm login

# 4. 发布前检查将要打包的文件
npm pack --dry-run

# 5. 发布到 npm（无作用域包，不需要 --access public）
npm publish
```

**后续更新流程：**

```bash
# 先提交git，确保工作目录是干净的
git add .
git commit -m "feat: your changes for 1.1.0"

# 使用npm version，修改版本信息，默认会自动创建提交和标签
npm version patch    # 或 minor / major
npm version minor -m "chore(release): bump version to %s"

# git推送与npm发布
git push
npm publish
```

**npm version相关**

```bash
# 手动管理git的提交
npm version minor --no-git-tag-version
git add .
git commit -m "chore: release vX.X.X"
git tag vX.X.X
git push
git push origin main --tags
npm publish

# 其他命令
## 直接使用会修改package.json 和 package-lock.json 中的版本号，
## 并且进行Git 提交、打标签操作，要求工作目录必须是干净的，否则运行失败。
npm version patch    # 或 minor / major
## --force参数，会跳过工作目录是否干净的检查
npm version minor --force
## 自定义提交信息，使用 %s 占位符，它会被自动替换为升级后的新版本号。
npm version minor -m "chore(release): bump version to %s"
## 全局设置git-tag-version=false，
## npm version 将默认不进行任何 Git 操作（不检查、不提交、不打标签）。
npm config set git-tag-version false
## 命令中显式覆盖
npm version minor --git-tag-version
```

---

## 📄 License

MIT © [xijie-m24](https://github.com/xijie-m24)
