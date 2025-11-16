# 🔍 检查 GitHub Actions 配置

## 问题诊断：Runner 等待超时

如果遇到 `The job has exceeded the maximum execution time while awaiting a runner for 24h0m0s` 错误，请按以下步骤检查：

## ✅ 检查清单

### 1. 检查工作流文件位置

确保工作流文件在正确的位置：
```
.github/workflows/build-apk.yml
```

**检查方法**：
- 在 GitHub 仓库中，进入 `.github/workflows/` 目录
- 确认 `build-apk.yml` 文件存在

### 2. 检查 `runs-on` 配置

**打开 `build-apk.yml` 文件，检查第 74 行附近：**

✅ **正确配置**：
```yaml
jobs:
  build:
    runs-on: ubuntu-latest  # ✅ 必须使用这个
```

❌ **错误配置**（会导致等待超时）：
```yaml
jobs:
  build:
    runs-on: self-hosted    # ❌ 错误：需要自托管 runner
```

```yaml
jobs:
  build:
    runs-on: [self-hosted, linux]  # ❌ 错误：包含 self-hosted
```

```yaml
jobs:
  build:
    runs-on: custom-runner   # ❌ 错误：不存在的 runner 标签
```

### 3. 检查账户配额

**检查方法**：
1. 进入 GitHub 仓库
2. 点击 "Settings" → "Actions" → "Runners"
3. 确认没有配置自托管 runner
4. 检查 "Usage" 标签页，确认没有超出免费配额

### 4. 验证工作流文件语法

**检查方法**：
1. 在 GitHub 仓库中，进入 "Actions" 标签页
2. 点击工作流名称
3. 查看是否有语法错误提示

## 🔧 修复步骤

### 如果发现配置错误：

1. **编辑工作流文件**：
   - 在 GitHub 仓库中，点击 `.github/workflows/build-apk.yml`
   - 点击编辑按钮（铅笔图标）

2. **修改 `runs-on` 配置**：
   ```yaml
   jobs:
     build:
       runs-on: ubuntu-latest  # 确保是这一行
       timeout-minutes: 120    # 添加超时设置
   ```

3. **保存并提交**：
   - 点击 "Commit changes"
   - 这会触发新的构建

### 如果工作流文件不存在：

1. **创建目录结构**：
   ```
   .github/
     workflows/
       build-apk.yml
   ```

2. **复制正确的工作流内容**：
   - 使用 `android_version/.github/workflows/build-apk.yml` 中的内容
   - 或参考 `📱使用GitHub_Actions打包APK.md` 中的配置

## 📝 完整正确的工作流配置

如果您的配置有问题，请使用以下完整配置：

```yaml
name: Build Android APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:
  pull_request:
    branches: [ main, master ]

jobs:
  build:
    runs-on: ubuntu-latest  # ⚠️ 关键：必须是 ubuntu-latest
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

## 🚀 测试修复

修复后，按以下步骤测试：

1. **提交更改**：
   ```bash
   git add .github/workflows/build-apk.yml
   git commit -m "修复 runner 配置"
   git push
   ```

2. **或手动触发**：
   - 进入 GitHub 仓库的 "Actions" 标签页
   - 选择 "Build Android APK" 工作流
   - 点击 "Run workflow"

3. **观察构建**：
   - 应该立即开始（不再等待 24 小时）
   - 查看日志确认使用的是 `ubuntu-latest` runner

## 💡 提示

- ✅ **总是使用 `ubuntu-latest`**：这是 GitHub 免费提供的 runner
- ✅ **添加 `timeout-minutes`**：避免无限等待
- ❌ **不要使用 `self-hosted`**：除非您确实配置了自托管 runner
- ❌ **不要使用自定义 runner 标签**：除非您知道它们存在

## 📞 仍然有问题？

如果修复后仍然有问题，请检查：
1. GitHub Actions 是否已启用（Settings → Actions → General）
2. 仓库是否为私有（私有仓库有使用限制）
3. 账户是否被限制（检查 GitHub 通知）

