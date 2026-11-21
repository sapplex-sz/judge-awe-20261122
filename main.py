import os

TEXT = (
    "A stone by the gate lies warm where the light has been, and lichen "
    "spreads over the stone. The lichen's edge has moved a little this year. "
    "The lane was laid on a fold the hill already held, long before the stone "
    "was set. Beyond the hill, a valley goes on.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
