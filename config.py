import os
import sys

# Визначаємо базову директорію від місця запуску:
# - для EXE: поруч із app.exe
# - для Python: папка файлу config.py
if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Абсолютні шляхи
MODEL_PATH = os.path.join(BASE_DIR, "models", "realvisxl")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
TOOLS_DIR = os.path.join(BASE_DIR, "tools")

# Параметри генерації
DEFAULT_STEPS = 25
DEFAULT_SEED = 12345

# Перевірка наявності моделі (опційно, для раннього виявлення помилок)
if not os.path.exists(MODEL_PATH):
    print(f"[УВАГА] Модель не знайдена за шляхом: {MODEL_PATH}")