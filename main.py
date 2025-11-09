from stats import count_characters

def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()

    words = text.split()
    print(f"Found {len(words)} total words")

    chars = count_characters(text)
    print(chars)

main()