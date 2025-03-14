Template này cung cấp một cấu trúc dự án Tkinter chuẩn, bao gồm:

*   Tổ chức thư mục rõ ràng cho code GUI, logic, models, resources, và tests.
*   Các file cơ bản (`main.py`, `main_window.py`, `setup.py`, v.v.) đã sẵn sàng.
*   Tích hợp sẵn `requirements.txt` để quản lý dependencies.
*   Tự động tạo file `README.md` mô tả cấu trúc dự án.
*   Hỗ trợ nhiều license phổ biến (MIT, GPL, BSD, Apache, Unlicense, Proprietary, Custom), tự động tải/tạo file `LICENSE` tương ứng.
*   File cấu hình `pyproject.toml` và `setup.py` để dễ dàng đóng gói và chia sẻ.

**Cách Sử Dụng Template**

1.  **Cài đặt Cookiecutter:**

    Nếu bạn chưa có Cookiecutter, hãy cài đặt nó bằng pip:

    ```bash
    pip install cookiecutter
    ```

2.  **Tạo dự án từ template:**

    Mở terminal (hoặc command prompt) và chạy lệnh sau:

    ```bash
    cookiecutter https://github.com/ti014/cookiecutter-tkinter-app-template
    ```

    **Quan trọng:** Thay thế `<your-username>` và `<your-repo-name>` bằng tên người dùng và tên repository GitHub của bạn.

3.  **Trả lời các câu hỏi:**

    Cookiecutter sẽ hiển thị một loạt câu hỏi để bạn tùy chỉnh dự án:

    *   `project_name`: Tên của dự án (ví dụ: My Awesome App).
    *   `project_slug`: Tên thư mục dự án (sẽ được tự động tạo dựa trên `project_name`, nhưng bạn có thể thay đổi).
    *   `description`: Mô tả ngắn gọn về dự án.
    *   `author_name`: Tên tác giả.
    *   `author_email`: Địa chỉ email của tác giả.
    *   `license`: Chọn license cho dự án (MIT, GPL-3.0, BSD-3-Clause, Apache-2.0, Unlicense, Proprietary, Custom).
    *   `python_version`: Chọn phiên bản Python bạn muốn sử dụng.

    Bạn có thể nhấn Enter để chấp nhận các giá trị mặc định (trong ngoặc vuông), hoặc nhập giá trị mới.

4.  **Dự án của bạn đã sẵn sàng!**

    Cookiecutter sẽ tạo một thư mục mới (với tên `project_slug` bạn đã chọn) chứa toàn bộ code của dự án Tkinter.

**Cấu Trúc Dự Án**

Sau khi tạo dự án, bạn sẽ có cấu trúc thư mục như sau:

```
📁 <project_slug>/
├── 📂 src/                # Source code
│   ├── 📂 gui/            # GUI-related code (Tkinter)
│   │   ├── 📜 __init__.py
│   │   ├── 📜 main_window.py
│   │   ├── 📜 widgets.py
│   │   └── 📜 themes.py
│   ├── 📂 logic/          # Application logic
│   │   ├── 📜 __init__.py
│   │   ├── 📜 calculator.py  (Ví dụ)
│   │   └── 📜 data_handler.py (Ví dụ)
│   ├── 📂 models/         # Data models
│   │   ├── 📜 __init__.py
│   │   └── 📜 data_model.py (Ví dụ)
│   ├── 📂 resources/      # Static resources (images, icons, configs)
│   │   ├── 📂 images/
│   │   ├── 📂 icons/
│   │   └── 📂 configs/
│   ├── 📂 utils/          # Utility functions
│   │   ├── 📜 __init__.py
│   │   ├── 📜 config_parser.py (Ví dụ)
│   │   ├── 📜 file_utils.py    (Ví dụ)
│   │   └── 📜 string_utils.py  (Ví dụ)
│   ├── 📜 __init__.py
│   └── 📜 main.py         # Main application entry point
├── 📂 tests/              # Unit tests
│    ├── 📜 __init__.py
│    ├── 📜 test_logic.py   (Ví dụ)
│    └── 📜 test_utils.py   (Ví dụ)
├── 📂 docs/               # Documentation
│   ├── 📜 INSTALL.md
│   ├── 📜 README.md      # Hướng dẫn sử dụng, cấu trúc dự án, v.v.
│   └── 📜 USAGE.md
├── 📜 .gitignore          # Files and directories to ignore in Git
├── 📜 LICENSE             # Project license (hoặc placeholder)
├── 📜 pyproject.toml      # Project configuration (build system, etc.)
└── 📜 setup.py            # Setuptools configuration
```

**Chạy Ứng Dụng**

1.  **Cài đặt các thư viện cần thiết:**

    ```bash
    cd <project_slug>  # Di chuyển vào thư mục dự án
    pip install -r src/requirements.txt
    ```

2.  **Chạy ứng dụng:**

    ```bash
    python src/main.py
    ```


Với template Cookiecutter này, bạn có thể nhanh chóng bắt đầu phát triển các ứng dụng Tkinter mà không cần lo lắng về việc thiết lập dự án. 
Nếu bạn có bất kỳ câu hỏi hoặc đóng góp nào, hãy tạo một issue!
