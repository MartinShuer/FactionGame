# 🎯 快速开始指南

## 方案选择

您现在有 **3 个完整的打包方案**，请选择一个：

---

## 🥇 方案 A：GitHub Actions（最推荐）

**适合：** 想要最简单、最稳定的方案

### 步骤（10分钟配置，20分钟构建）：

#### 1. 上传到 GitHub

```powershell
# 打开 PowerShell，运行：
cd C:\Users\Martin\Desktop\FactionGame\android_version

# 如果已有 .git 目录，先删除
if (Test-Path .git) { Remove-Item .git -Recurse -Force }

# 初始化
git init
git add .
git commit -m "FactionGame - Ready to build"
```

#### 2. 在 GitHub 创建仓库

1. 打开 https://github.com/new
2. 仓库名：`FactionGame`
3. 设置为 **Private**（私有，不会公开）
4. **不要**勾选 README、.gitignore 等
5. 点击 **Create repository**

#### 3. 推送代码

```powershell
# 替换 YOUR_USERNAME 为您的 GitHub 用户名
git remote add origin https://github.com/YOUR_USERNAME/FactionGame.git
git branch -M main
git push -u origin main
```

#### 4. 查看构建进度

1. 打开仓库页面
2. 点击顶部 **Actions**
3. 等待构建完成（约20分钟）
4. 点击构建记录 → 下载 **Artifacts** 中的 APK

---

## 🥈 方案 B：WSL 本地构建

**适合：** 想要完全本地控制、可反复构建

### 步骤（25分钟配置，30-50分钟构建）：

#### 1. 安装 WSL

**以管理员身份运行 PowerShell**：

```powershell
cd C:\Users\Martin\Desktop\FactionGame\android_version

# 运行安装脚本
.\01-安装WSL.ps1

# 重启电脑（必需）
```

#### 2. 配置 Ubuntu 环境

重启后，打开 **Ubuntu** 应用，运行：

```bash
cd /mnt/c/Users/Martin/Desktop/FactionGame/android_version
bash 02-配置Ubuntu环境.sh
```

#### 3. 构建 APK

```bash
bash 03-构建APK.sh
```

等待构建完成，APK 会自动复制到桌面！

---

## 🥉 方案 C：Google Colab（不推荐）

虽然准备了脚本，但成功率低，不建议使用。

---

## ⚡ 推荐决策树

```
是否有 GitHub 账号？
├─ 是 → 使用 GitHub Actions（方案 A）⭐⭐⭐⭐⭐
│      最简单、最稳定、最快
│
└─ 否 → 使用 WSL 本地构建（方案 B）⭐⭐⭐⭐
       一次配置，终身使用
```

---

## 📞 我需要您告诉我：

**您想用哪个方案？**

1. **GitHub Actions** - 我帮您上传到 GitHub
2. **WSL 本地构建** - 我指导您安装 WSL
3. **都可以** - 我推荐 GitHub Actions

请回复数字或方案名称！
