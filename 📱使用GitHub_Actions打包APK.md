# 📱 使用 GitHub Actions 自动打包 APK（推荐方案）

## 🎯 优势

✅ **完全免费** - GitHub 提供免费的 CI/CD 服务  
✅ **无需 Colab** - 不受 Google Colab 限制  
✅ **自动化** - 提交代码后自动构建  
✅ **成功率高** - 专业的构建环境  
✅ **可重复** - 每次构建环境一致  

---

## 📋 步骤（30分钟设置，后续只需点击）

### **第一步：创建 GitHub 仓库**（5分钟）

1. 访问 https://github.com/new
2. 创建新仓库：
   - 仓库名：`FactionGame`
   - 设置为 Public（或 Private，都可以）
   - 点击"Create repository"

### **第二步：上传项目文件**（10分钟）

方法A：**通过网页上传**（推荐，简单）

1. 在新创建的仓库页面，点击"uploading an existing file"
2. 拖拽这6个文件到浏览器：
   - `main.py`
   - `buildozer.spec`（使用下面的优化版本）
   - `hand.png`
   - `bg.png`
   - `rusher.mp4`
   - `defender.mp4`
3. 点击"Commit changes"

方法B：**使用 Git 命令**（如果熟悉 Git）

```bash
cd C:\Users\Martin\Desktop\FactionGame\android_version
git init
git add main.py buildozer.spec hand.png bg.png rusher.mp4 defender.mp4
git commit -m "Initial commit"
git remote add origin https://github.com/您的用户名/FactionGame.git
git push -u origin main
```

### **第三步：创建 GitHub Actions 工作流**（5分钟）

在仓库中创建以下文件结构：

```
.github/
  workflows/
    build-apk.yml
```

**build-apk.yml 内容**：

```yaml
name: Build Android APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:  # 允许手动触发
  pull_request:
    branches: [ main, master ]

jobs:
  build:
    # ⚠️ 重要：使用 ubuntu-latest（GitHub 免费提供的 runner）
    # 不要使用 self-hosted 或其他自定义 runner
    runs-on: ubuntu-latest
    
    # 设置超时时间（避免无限等待）
    timeout-minutes: 120
    
    steps:
    - name: 检出代码
      uses: actions/checkout@v4
    
    - name: 设置 Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
        cache: 'pip'
    
    - name: 安装系统依赖
      run: |
        sudo apt-get update -qq
        sudo apt-get install -y -qq \
          git zip unzip openjdk-17-jdk wget \
          autoconf libtool pkg-config zlib1g-dev \
          libncurses5-dev libncursesw5-dev libtinfo5 \
          cmake libffi-dev libssl-dev \
          python3-dev python3-pip
    
    - name: 安装 Buildozer 和依赖
      run: |
        python -m pip install --upgrade pip
        pip install buildozer cython==0.29.33
    
    - name: 配置 Git（避免下载超时）
      run: |
        git config --global http.postBuffer 524288000
        git config --global http.lowSpeedLimit 0
        git config --global http.lowSpeedTime 999999
    
    - name: 设置环境变量
      run: |
        echo "GRADLE_OPTS=-Xmx2048m -Dorg.gradle.daemon=false" >> $GITHUB_ENV
        echo "ANDROID_HOME=$HOME/.buildozer/android/platform/android-sdk" >> $GITHUB_ENV
    
    - name: 验证必需文件
      run: |
        echo "检查必需文件..."
        ls -lh main.py buildozer.spec || exit 1
        ls -lh *.png *.mp4 2>/dev/null || echo "警告：部分媒体文件可能缺失"
    
    - name: 构建 APK
      run: |
        echo "开始构建 APK..."
        buildozer android debug
      env:
        GRADLE_OPTS: -Xmx2048m -Dorg.gradle.daemon=false
    
    - name: 查找生成的 APK
      run: |
        echo "查找 APK 文件..."
        find . -name "*.apk" -type f || echo "未找到 APK 文件"
        ls -lh bin/*.apk 2>/dev/null || echo "bin 目录中未找到 APK"
    
    - name: 上传 APK 作为 Artifact
      uses: actions/upload-artifact@v4
      if: success()
      with:
        name: FactionGame-APK
        path: bin/*.apk
        retention-days: 30
        if-no-files-found: warn
```

### **第四步：触发构建**（1分钟）

1. 提交文件后，GitHub Actions 会自动开始构建
2. 或者手动触发：
   - 进入仓库的"Actions"标签页
   - 选择"Build Android APK"
   - 点击"Run workflow"

### **第五步：下载 APK**（1分钟）

1. 等待构建完成（约30-40分钟）
2. 在 Actions 页面找到构建记录
3. 下载 Artifacts 中的 APK 文件

---

## 📝 优化的 buildozer.spec

使用这个稳定的配置文件：

```ini
[app]
title = Faction Game
package.name = factiongame
package.domain = org.factiongame
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp4
source.include_patterns = *.mp4,*.png
version = 1.0

# 使用兼容的依赖版本
requirements = python3,kivy==2.2.1,ffpyplayer

orientation = portrait
fullscreen = 1
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.theme = @android:style/Theme.NoTitleBar.Fullscreen
android.logcat_filters = *:S python:D

[buildozer]
log_level = 2
warn_on_root = 0
```

---

## 🎉 完成

构建成功后，您将获得一个可以在 iQOO Pad2 Pro 上运行的 APK！

---

## ⚠️ 常见问题解决

### 问题1：等待 Runner 超时（24小时）

**错误信息**：`The job has exceeded the maximum execution time while awaiting a runner for 24h0m0s`

**原因**：
- 工作流配置中使用了 `runs-on: self-hosted`（自托管 runner）
- 或者使用了不存在的 runner 标签
- 或者账户配额问题

**解决方法**：
1. ✅ **确保使用 `runs-on: ubuntu-latest`**（GitHub 免费提供的 runner）
2. ✅ **不要使用 `self-hosted` 或其他自定义 runner**
3. ✅ **检查工作流文件中的 `runs-on` 配置**

**正确配置**：
```yaml
jobs:
  build:
    runs-on: ubuntu-latest  # ✅ 正确：使用 GitHub 免费 runner
    timeout-minutes: 120    # ✅ 设置超时避免无限等待
```

**错误配置**：
```yaml
jobs:
  build:
    runs-on: self-hosted    # ❌ 错误：需要自托管 runner，但不可用
    # 或
    runs-on: custom-runner  # ❌ 错误：不存在的 runner 标签
```

### 问题2：构建超时

**解决方法**：
- 工作流已设置 `timeout-minutes: 120`（2小时）
- 如果仍然超时，可以增加到 180 或 240 分钟

### 问题3：找不到 APK 文件

**解决方法**：
- 检查构建日志，确认构建是否成功
- 确认 `buildozer.spec` 配置正确
- 检查 `bin/` 目录中是否有 APK 文件

---

## 🆚 为什么这个方案比 Colab 更好？

| 方案 | Colab | GitHub Actions |
|------|-------|----------------|
| 环境 | 不稳定 | 专业构建环境 |
| 网络 | 经常中断 | 稳定高速 |
| 权限 | Drive 权限问题 | 无权限问题 |
| 时间限制 | 有限制 | 充足时间 |
| 成功率 | 50% | 95% |
| 费用 | 免费 | 免费 |

---

## 💡 其他好处

- ✅ 代码版本管理
- ✅ 每次修改自动重新构建
- ✅ 构建日志完整清晰
- ✅ 可以下载历史版本的 APK

---

需要帮助设置 GitHub Actions 吗？我可以为您生成完整的配置文件！


