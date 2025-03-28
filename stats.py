import re
import sys
from collections import Counter

def get_book_text(path_to_book:str) -> str:
       try:
              with open(path_to_book,encoding="utf-8-sig") as book:
                     book_text = book.read()
                     return book_text
       except FileNotFoundError:
              print("No book found")
              sys.exit(2)

def clean_text(text: str) -> str:
       return re.sub(r"[^\w\s]", "", text)

def count_words(book_text:str) -> dict:
       words = book_text.split()
       return Counter(words)

def get_top_n_sorted(words:list, count:int = 1) -> list:
    return words[:count]

def count_characters(book_text:str) -> dict:
       return Counter(book_text)

def sort_result(data_dict:dict, reverse: bool = True) -> list:
       report = sorted(data_dict.items(), key= lambda x: x[1], reverse= reverse)
       return report

def omit_stop_words(words_dict: dict, stopwords_path: str = "stopwords.txt") -> dict:
    try:
        with open(stopwords_path) as file:
            stopwords = set(file.read().splitlines())
    except FileNotFoundError:
        print(f"Stop words file not found at {stopwords_path}")
        sys.exit(3)

    return {word: count for word, count in words_dict.items() if word not in stopwords}

def lowercase_text(book_text: str) -> str:
    return book_text.lower()


