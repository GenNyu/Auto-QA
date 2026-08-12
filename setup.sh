#!/usr/bin/env bash
#
# Cài đặt Auto-QA. Chạy một lần duy nhất:
#
#     ./setup.sh
#
set -euo pipefail
cd "$(dirname "$0")"

echo ""
echo "Cài đặt Auto-QA"
echo "────────────────────────────────────────────────────────────"

# 1. Kiểm tra Python (ưu tiên pyenv/python3.9/python3)
PYTHON_CMD=""
if command -v python >/dev/null 2>&1; then
  PYTHON_CMD="python"
elif command -v python3.9 >/dev/null 2>&1; then
  PYTHON_CMD="python3.9"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON_CMD="python3"
fi

if [ -z "$PYTHON_CMD" ]; then
  echo "❌ Chưa có Python 3. Cài Python 3.9 tại: https://www.python.org/downloads/"
  exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
echo "  ✅ Python $PYTHON_VERSION"

# Cảnh báo nếu dùng Python 3.14
if [[ "$PYTHON_VERSION" == 3.14* ]]; then
  echo "⚠️  Python 3.14 có thể gây treo. Nên dùng Python 3.9."
  echo "   Nếu dùng pyenv: pyenv install 3.9.8 && pyenv global 3.9.8"
fi

# 2. Môi trường ảo + thư viện Python
if [ ! -d .venv ]; then
  echo "  ⏳ Tạo môi trường ảo..."
  $PYTHON_CMD -m venv .venv
fi
echo "  ⏳ Cài thư viện Python..."
./.venv/bin/pip install --quiet --upgrade pip
./.venv/bin/pip install --quiet -r requirements.txt
echo "  ✅ Thư viện Python"

# 3. Node + Playwright
if ! command -v npm >/dev/null 2>&1; then
  echo "❌ Chưa có Node.js. Cài tại: https://nodejs.org"
  exit 1
fi
echo "  ⏳ Cài Playwright..."
npm install --silent
npx playwright install chromium >/dev/null
echo "  ✅ Playwright"

# 4. File cấu hình bí mật
if [ ! -f .env ]; then
  cp .env.example .env
  echo "  ✅ Đã tạo file .env"
  NEEDS_ENV=1
else
  echo "  ✅ File .env đã có"
  NEEDS_ENV=0
fi

echo "────────────────────────────────────────────────────────────"

if [ "$NEEDS_ENV" = "1" ]; then
  echo ""
  echo "⚠️  Còn một bước thủ công: mở file .env và điền"
  echo "      • API key của LLM   (ví dụ OPENAI_API_KEY)"
  echo "      • CHAT_EMAIL và CHAT_PASSWORD để đăng nhập chatbot"
fi

if command -v just >/dev/null 2>&1; then
  echo ""
  echo "Sau đó kiểm tra lại bằng:"
  echo "      just check"
  echo ""
  echo "Rồi chạy đánh giá:"
  echo "      just list"
  echo "      just run iso27001"
  echo ""
  echo "Các lệnh 'just' đã dùng sẵn Python trong .venv, không cần activate."
  echo "Muốn gõ 'python ...' thủ công thì mở shell đã bật venv:"
  echo "      just shell"
  echo ""
else
  echo ""
  echo "💡 Cài thêm 'just' để gõ lệnh ngắn hơn:  brew install just"
  echo ""
  echo "Sau đó kiểm tra lại bằng:"
  echo "      ./.venv/bin/python qa.py check"
  echo ""
  echo "Rồi chạy đánh giá:"
  echo "      ./.venv/bin/python qa.py list"
  echo "      ./.venv/bin/python qa.py run iso27001"
  echo ""
fi
