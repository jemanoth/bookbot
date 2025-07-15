import sys
from stats import word_counter
from stats import character_counter
from stats import character_dict_sorter


def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def book_report_printer(book_path):
    content = get_book_text(book_path)
    word_count = word_counter(content)
    character_count = character_counter(content)
    character_dict_list = character_dict_sorter(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in character_dict_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_report_printer(sys.argv[1])
main()