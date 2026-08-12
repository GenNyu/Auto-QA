# Auto-QA — gõ `just` để xem toàn bộ lệnh.
#
# Dùng thẳng Python trong môi trường ảo, nên không cần activate venv bao giờ.

python := ".venv/bin/python"

# Hiện danh sách lệnh
default:
    @just --list --unsorted

# Cài đặt lần đầu (chạy một lần trên mỗi máy)
setup:
    ./setup.sh

# Mở shell đã bật sẵn venv — gõ `python script.py ...` trực tiếp, `exit` để thoát
shell:
    @echo "venv đã bật: $(pwd)/.venv  ·  gõ 'exit' để thoát"
    @VIRTUAL_ENV="$(pwd)/.venv" PATH="$(pwd)/.venv/bin:$PATH" exec $SHELL

# Kiểm tra máy đã sẵn sàng chưa
check:
    @{{python}} qa.py check

# Liệt kê các bộ đánh giá
list:
    @{{python}} qa.py list

# Tạo bộ đánh giá mới từ thư mục tài liệu — vd: just new input/kb/urbox
new folder *args:
    @{{python}} qa.py new {{folder}} {{args}}

# Chạy trọn 4 bước rồi mở báo cáo — vd: just run iso27001
run project:
    @{{python}} qa.py run {{project}}

# Bước 1: chỉ sinh câu hỏi
gen project *args:
    @{{python}} qa.py gen {{project}} {{args}}

# Bước 2: chỉ hỏi chatbot
ask project:
    @{{python}} qa.py ask {{project}}

# Bước 3: chỉ chấm điểm
score project:
    @{{python}} qa.py score {{project}}

# Bước 4: chỉ dựng lại báo cáo
report project:
    @{{python}} qa.py report {{project}}

# Mở báo cáo đã có sẵn mà không chạy lại gì
open project:
    @open runs/{{project}}/report.html

# Xoá kết quả của một bộ để chạy lại từ đầu (run folder + cache)
clean project:
    @rm -rf runs/{{project}} && echo "✓ Đã xoá runs/{{project}}"
    @rm -f cache/{{project}}_processed.json && echo "✓ Đã xoá cache/{{project}}_processed.json"
    @echo "✅ Sẵn sàng chạy lại: just gen {{project}}"

# Xoá tất cả cache và kết quả chạy (fresh start)
nuke:
    @rm -rf runs/*
    @rm -rf cache/*
    @echo "☢️  Đã xoá TẤT CẢ cache và runs. Sẵn sàng fresh start."

# Xoá file tạm (__pycache__, .DS_Store, test-results)
tidy:
    @rm -rf __pycache__ */__pycache__ test-results
    @find . -name .DS_Store -not -path "./node_modules/*" -not -path "./.venv/*" -delete
    @echo "Đã dọn file tạm"
