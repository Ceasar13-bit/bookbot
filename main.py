
def main():
       print(count_words(get_book_text("books/frankenstein.txt")))

def get_book_text(path_to_book):
    with open(path_to_book) as file:
              file_contens = file.read()
              return file_contens

def count_words(book):
       return f"{len(book.split())} words found in the document"

main()