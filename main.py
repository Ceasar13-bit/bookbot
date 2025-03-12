import sys
import argparse
from stats import *
from cli import get_args

def main():
       args = get_args()
       book_path = args.file_path
       book = get_book_text(book_path)
       words = count_words(book)
       characters = sort_result(count_characters(book))
       show_top_words = int(input("How many most common words should I display? "))
       top_words = count_most_common(book, show_top_words)
       create_report(characters,words,book_path,top_words)
       
       

def get_book_text(path_to_book):
       try:
              with open(path_to_book) as file:
                     file_contens = file.read()
                     return file_contens
       except FileNotFoundError:
              print("No book found")
              sys.exit(2)

if __name__ == "__main__":
       main()