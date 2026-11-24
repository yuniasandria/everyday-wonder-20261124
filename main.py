import os

PART_A = "The mirror fogs after my shower, "
PART_B = "and for a minute the bathroom forgets my face."
LINE = PART_A + PART_B
assert LINE == "The mirror fogs after my shower, and for a minute the bathroom forgets my face."
assert 1 <= len(LINE) <= 200, len(LINE)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
