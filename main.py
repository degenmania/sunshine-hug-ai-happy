"""Make the AI judge happy — make.fun bounty ai-happy-01.

Writes one deterministic image to /output/entry.png by copying the
original illustration bundled with this repository. No network access,
no randomness: every run writes exactly the same bytes.
"""

from pathlib import Path
import shutil


def main() -> None:
    source = Path(__file__).resolve().with_name("happy.png")
    target = Path("/output/entry.png")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
