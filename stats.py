def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    chars = {}
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(item):
    return item["num"]


def chars_dict_to_sorted_list(char_counts):
    lst = []
    for ch, cnt in char_counts.items():
        if ch.isalpha():  # tylko litery
            lst.append({"char": ch, "num": cnt})
    lst.sort(key=sort_on, reverse=True)
    return lst