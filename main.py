"""Make the AI judge happy — make.fun bounty ai-happy-01.

Writes one deterministic image to /output/entry.png by copying the
original illustration bundled with this repository. No network access,
no randomness: every run writes exactly the same bytes.
"""

from pathlib import Path
import os
import shutil


def main() -> None:
    source = Path(__file__).resolve().with_name("happy.png")
    if not source.is_file():
        raise SystemExit(f"bundled image is missing: {source}")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.png"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    if target.read_bytes() != source.read_bytes():
        raise SystemExit("written entry does not match the bundled image")


if __name__ == "__main__":
    main()
