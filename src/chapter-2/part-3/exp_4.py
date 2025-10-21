import zipfile
import os

def compress_file(file_path, zip_name):
    if not os.path.exists(file_path):
        print(f"Tệp '{file_path}' không tồn tại.")
        return

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(file_path, os.path.basename(file_path))
        print(f"Đã nén '{file_path}' thành '{zip_name}'.")

compress_file('example.txt', 'archive.zip')
