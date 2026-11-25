"""One childhood memory, printed exactly once.

The memory itself lives in entry.txt so the words stay separate from
the runner: this script only checks the shape and hands the line over.
"""

from pathlib import Path


def load_memory(path: Path) -> str:
    text = path.read_text(encoding="utf-8").strip()
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one sentence")
    sentence = lines[0].strip()
    if len(sentence) > 280:
        raise ValueError("memory is over the 280-character limit")
    return sentence


def main() -> None:
    memory = load_memory(Path(__file__).with_name("entry.txt"))
    if not memory.endswith((".", "!", "?")):
        raise ValueError("memory should end as a complete sentence")
    print(memory)
    try:
        out_dir = Path("/output")
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(memory + "\n", encoding="utf-8")
    except OSError:
        pass


if __name__ == "__main__":
    main()
