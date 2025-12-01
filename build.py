import subprocess
import sys
import time
import threading
import os

RESET = "\033[0m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

STAGES = {
    "Analysis": 10,
    "PYZ": 30,
    "PKG": 55,
    "EXE": 85,
    "completed successfully": 100,
}

current_progress = 0


def print_progress(progress):
    bar_length = 50
    filled = int(bar_length * progress / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    color = GREEN if progress == 100 else CYAN

    sys.stdout.write(f"\r{color}[{bar}] {progress}%{RESET}")
    sys.stdout.flush()


def process_stream(stream):
    global current_progress

    for raw in iter(stream.readline, ''):
        if not raw:
            continue

        line = raw.strip()

        # Warning
        if "WARNING" in line:
            print("\n" + YELLOW + line + RESET)

        # Progress detection
        for key, value in STAGES.items():
            if key in line:
                current_progress = value
                print_progress(current_progress)

        if "completed successfully" in line:
            print_progress(100)   # Показуємо 100%

            # Переходимо на новий рядок, щоб 100% залишалося видно
            sys.stdout.write("\n")
            sys.stdout.flush()

            # Очищаємо наступний рядок (на випадок якщо PyInstaller вже щось вивів)
            sys.stdout.write("\r" + " " * 80 + "\r")
            sys.stdout.flush()

            print(GREEN + "✔ Збірка завершена успішно!" + RESET)


def run_pyinstaller():
    print("=====================================")
    print("       🚀 Збірка EXE (PyInstaller)")
    print("=====================================")

    cmd = [
        "pyinstaller",
        "app.py",
        "--name", "app",
        "--onefile",
        "--clean",
        "--noconfirm",
        "--log-level=INFO",
        "--icon=icon.ico",
        "--add-data", "venv/Lib/site-packages/torch;tensor_libs/torch",
        "--hidden-import=torch",
        "--hidden-import=torch._C",
        "--hidden-import=diffusers",
        "--hidden-import=transformers",
        "--exclude-module=torch.utils.tensorboard",
        "--exclude-module=torch.distributed",
        "--exclude-module=torch.distributed.elastic",
        "--exclude-module=torch._inductor",
    ]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    t1 = threading.Thread(target=process_stream, args=(process.stdout,))
    t2 = threading.Thread(target=process_stream, args=(process.stderr,))

    t1.start()
    t2.start()

    process.wait()
    t1.join()
    t2.join()


if __name__ == "__main__":
    print_progress(0)
    print()
    run_pyinstaller()
