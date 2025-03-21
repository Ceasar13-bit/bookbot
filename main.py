from stats import *
from cli import get_args

def main():
       args = get_args()
       book_path = args.file_path
       book = get_book_text(book_path)
       words = count_words(book)
       characters = sort_result(count_characters(book))
       show_top_words = args.n
       top_words = count_most_common(book, show_top_words, args.omit_stop_words)
       create_report(characters,words,book_path,top_words)
       
       



if __name__ == "__main__":
       main()