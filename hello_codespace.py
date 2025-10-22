# hello_codespace.py

import platform
import datetime

def main():
    print("Hello from your GitHub Codespace!")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()}")
    print(f"Time now: {datetime.datetime.now()}")

    # Simple computation test
    numbers = [1, 2, 3, 4, 5]
    squares = [n**2 for n in numbers]
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")

if __name__ == "__main__":
    main()
