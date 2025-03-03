from stats import count_words

def main():
       print(count_words(get_book_text("books/frankenstein.txt")))

def get_book_text(path_to_book):
    with open(path_to_book) as file:
              file_contens = file.read()
              return file_contens



main()