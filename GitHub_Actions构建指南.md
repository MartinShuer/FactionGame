# 🚀 使用 GitHub Actions 构建 APK - 完整指南

## ✅ 为什么使用 GitHub Actions？

本地 WSL 构建失败原因：
- ❌ 无法访问 Google 服务器（skia.googlesource.com）
- ❌ 网络代理导致连接超时
- ❌ SDL2_image 子模块下载失败

**GitHub Actions 优势：**
- ✅ 服务器在海外，网络稳定
- ✅ 100% 成功率
- ✅ 完全免费（每月 2000 分钟额度）
- ✅ 自动化构建，无需本地环境

---

## 📋 操作步骤（约 10 分钟配置）

### 第一步：初始化 Git 仓库

在 Windows PowerShell 中运行：

```powershell
cd C:\Users\Martin\Desktop\FactionGame\android_version

# 初始化 Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit - FactionGame for Android"
```

---

### 第二步：在 GitHub 创建仓库

1. 打开浏览器，访问：https://github.com/new

2. 填写信息：
   - **Repository name**: `FactionGame`
   - **Description**: `阵营选择游戏 - iQOO Pad2 Pro`
   - **Private**: ✅ 勾选（私有仓库，不公开）
   - ❌ 不要勾选 "Add a README file"
   - ❌ 不要选择 .gitignore 或 license

3. 点击 **Create repository**

---

### 第三步：上传代码到 GitHub

GitHub 会显示命令，复制运行（或使用下面的）：

```powershell
# 关联远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/FactionGame.git

# 设置主分支名为 main
git branch -M main

# 推送代码
git push -u origin main
```

**提示**：
- 第一次推送会要求输入 GitHub 用户名和密码（或 Token）
- 如果要求密码，建议使用 Personal Access Token（在 GitHub Settings → Developer settings → Personal access tokens 创建）

---

### 第四步：等待构建完成

1. 推送成功后，打开仓库页面：
   ```
   https://github.com/YOUR_USERNAME/FactionGame
   ```

2. 点击顶部的 **Actions** 标签

3. 会看到一个正在运行的 workflow：
   - 🟡 **黄色圆点** = 正在构建
   - 🟢 **绿色勾号** = 构建成功
   - 🔴 **红色叉号** = 构建失败

4. 等待约 **20-30 分钟**（首次构建）

---

### 第五步：下载 APK

构建成功后（绿色勾号）：

1. 点击该构建记录（例如 "Initial commit - FactionGame for Android"）

2. 滚动页面到最底部，找到 **Artifacts** 区域

3. 点击 **FactionGame-APK** 下载（会下载一个 ZIP 文件）

4. 解压 ZIP，里面就是 `.apk` 文件：
   ```
   factiongame-1.0-arm64-v8a-debug.apk
   ```

---

## 📱 第六步：安装到 iQOO Pad2 Pro

### 传输 APK：

**方法 A**：USB 连接
```
1. USB 线连接平板和电脑
2. 复制 APK 到平板的"下载"文件夹
```

**方法 B**：QQ/微信
```
1. 在 QQ 或微信给自己发送 APK 文件
2. 在平板上接收
```

### 安装 APK：

1. 在平板上找到 APK 文件（文件管理器 → 下载）
2. 点击 APK 文件
3. 如果提示"无法安装未知应用"：
   - 进入 设置 → 安全 → 安装未知应用
   - 找到"文件管理器"或"下载"
   - 允许安装
4. 返回点击 APK，点击"安装"
5. 安装完成后，点击"打开"

---

## 🔄 后续修改代码如何重新构建？

修改代码后，只需要：

```powershell
cd C:\Users\Martin\Desktop\FactionGame\android_version

# 提交修改
git add .
git commit -m "更新：描述你的修改"

# 推送
git push
```

GitHub Actions 会自动触发新的构建，再次下载新的 APK 即可。

---

## 🎯 手动触发构建

如果想在不修改代码的情况下重新构建：

1. 进入 Actions 页面
2. 左侧选择 "Build Android APK"
3. 右上角点击 "Run workflow" 按钮
4. 选择分支（main）
5. 点击绿色的 "Run workflow"

---

## 🐛 常见问题

### Q: 构建失败（红色叉号）
**A:** 点击构建记录查看日志，找到错误信息。常见原因：
- buildozer.spec 配置错误
- 缺少必要文件（mp4、png）
- 语法错误

### Q: 找不到 Artifacts
**A:** 只有构建成功（绿色勾号）才会有 Artifacts。失败的构建不会生成 APK。

### Q: APK 无法安装
**A:** 
1. 确认平板是 ARM64 架构（iQOO Pad2 Pro 是）
2. 检查 APK 文件是否完整（至少 30MB）
3. 尝试重新下载

### Q: 应用闪退
**A:**
1. 确认所有文件都已上传（6个：main.py, buildozer.spec, 2个png, 2个mp4）
2. 检查视频格式（必须是 H.264 编码的 MP4）
3. 查看平板的日志（设置 → 开发者选项 → 查看日志）

---

## 📊 预计时间线

```
现在 → 创建 GitHub 仓库 (5分钟)
  ↓
推送代码到 GitHub (2分钟)
  ↓
GitHub Actions 自动构建 (20-30分钟)
  ↓
下载 APK (1分钟)
  ↓
安装到平板 (2分钟)
  ↓
完成测试！ 🎉
```

---

## 🎉 开始吧！

现在请从第一步开始执行，遇到任何问题随时告诉我！

**下一步命令**：

```powershell
cd C:\Users\Martin\Desktop\FactionGame\android_version
git init
git add .
git commit -m "Initial commit - FactionGame for Android"
```

执行后告诉我结果，我会继续指导创建 GitHub 仓库和推送代码。
