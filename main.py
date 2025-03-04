import sys
from stats import count_words, count_characters, sort_result, create_report

def main():
       if len(sys.argv) != 2:
              print("Usage: python3 main.py <path_to_book>")
              sys.exit(1)
       book_path = sys.argv[1]
       book = get_book_text(book_path)
       words = count_words(book)
       characters = sort_result(count_characters(book))
       create_report(characters,words,book_path)

def get_book_text(path_to_book):
       try:
              with open(path_to_book) as file:
                     file_contens = file.read()
                     return file_contens
       except FileNotFoundError:
              print("No book found")
              sys.exit(2)


main()