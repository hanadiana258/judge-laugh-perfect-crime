"""Comedy entry: drips the perfect-crime one-liner into the output folder.

A tiny stdlib program: finds a writable output directory (the sandbox's
MAKEFUN_OUTPUT_DIR, then /output, then a local ./out), writes entry.txt
holding the judged one-liner, and echoes it for the run log.
"""
import os

THE_LINE = "I fixed the bug by deleting the code. Nobody remembers what it did, including me, which is either a bug fix or a perfect crime."

def pick_output_dir():
    wanted = [os.environ.get("MAKEFUN_OUTPUT_DIR"), "/output",
              os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")]
    for path in wanted:
        if not path:
            continue
        try:
            os.makedirs(path, exist_ok=True)
            marker = os.path.join(path, ".write_test")
            open(marker, "w").close()
            os.remove(marker)
            return path
        except OSError:
            continue
    return None

def run():
    folder = pick_output_dir()
    if folder is None:
        raise SystemExit(1)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(THE_LINE)
    print(THE_LINE)

if __name__ == "__main__":
    run()
