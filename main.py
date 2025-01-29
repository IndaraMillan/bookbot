def get_num_words(text):
    words = text.split()
    return len(words)


def read_text(path):
    with open(path) as f:
        return f.read()


def get_num_per_char(text):
    count_dict = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    return count_dict


def print_report(num_words, dict_char):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    sorted_dict = dict(
        sorted(dict_char.items(), key=lambda item: item[1], reverse=True)
    )
    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

    print("--- End report ---")


if __name__ == "__main__":
    text = read_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    char_counter_dict = get_num_per_char(text)
    print_report(num_words, char_counter_dict)
