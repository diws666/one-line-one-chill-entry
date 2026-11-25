import os

LINE = "I locked the front door, then heard the key turn in the lock from the inside."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = os.path.join(output_dir, "entry.txt")

os.makedirs(output_dir, exist_ok=True)
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
