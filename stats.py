import re
import sys

def get_book_text(path_to_book:str) -> str:
       try:
              with open(path_to_book) as book:
                     book_text = book.read()
                     return book_text
       except FileNotFoundError:
              print("No book found")
              sys.exit(2)

def clean_text(book_text:str) -> str:
       pattern = r"[^\w\s]"
       return re.sub(pattern, "", book_text)

def count_words(cleaned_book_text):
       words = {}
       cleaned_book_text = cleaned_book_text.split()
       for word in cleaned_book_text:
              words[word] = words.get(word, 0) + 1
       return words

def count_most_common(words:list, count:int) -> list:
    return words[:count]

def count_characters(book_text:str, case_sensitive:bool=False) -> dict:
       characters = {}
       if not case_sensitive:
              book_text = book_text.lower()
       for char in book_text:
              characters[char] = characters.get(char, 0) + 1  
       return characters

def sort_result(data_dict:dict, reverse: bool = True) -> list:
       report = sorted(data_dict.items(), key= lambda x: x[1], reverse= reverse)
       return report

def omit_stop_words(words_dict:dict) -> dict:
       with open("stopwords.txt") as file:
                     stopwords = set(file.read().splitlines())
       processed_words = words_dict.copy()
       new_words = dict(filter(lambda w: w[0] not in stopwords, processed_words.items()))
       return new_words

def apply_case_filter(book_text: str, case_sensitive: bool) -> str:
    return book_text if case_sensitive else book_text.lower()



def create_report(report, result, book_path, top_words): # marked for later removal
       print("============ BOOKBOT ============")
       print(f"Analyzing book found at {book_path}")
       print("----------- Word Count ----------")
       print(result)
       print("--------- Character Count -------")
       for char in report:
              print(f"{char["character"]}: {char["count"]}")
       print("--------- Top Words -------")
       for word in top_words:
              print(f"{word[0]}: {word[1]}")
       print("============= END ===============")

