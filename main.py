import sys
from stats import count_characters, chars_dict_to_sorted_list

USAGE = "Usage: python3 main.py <path_to_book>"

def main():
    # oczekujemy 2 elementów w argv: [nazwa_skryptu, ścieżka]
    if len(sys.argv) != 2:
        print(USAGE)
        sys.exit(1)

    path = sys.argv[1]

    print("======== BOOKBOT ========")
    print(f"Analyzing book found at {path}...")
    print("\n----- Word Count -----")

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # liczenie słów
    words = text.split()
    print(f"Found {len(words)} total words")

    # liczenie i sortowanie znaków
    print("\n----- Character Count -----")
    chars = count_characters(text)
    sorted_chars = chars_dict_to_sorted_list(chars)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("======== END ========")

if __name__ == "__main__":
    main()