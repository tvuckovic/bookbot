from stats import *

def get_book_text(rel_path):
    with open(rel_path) as book:
        contents = book.read()
    return contents

def report(path, num_words, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        if not char["char"].isalpha():
            continue
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_to_analyze = get_book_text(path)
    number_of_words = word_counter(book_to_analyze)
    dict_za_sort = char_counter(book_to_analyze)
    final_dict = sorted_list(dict_za_sort)
    report(path, number_of_words, final_dict)

main()