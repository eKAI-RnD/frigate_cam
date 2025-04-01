import os
from dotenv import load_dotenv

# Load biến từ file .env
load_dotenv()

# Lấy biến môi trường
frigate_dir = os.getenv("FRIGATE_BASE_DIR")
print(frigate_dir)  # Kết quả: /media/frigate
