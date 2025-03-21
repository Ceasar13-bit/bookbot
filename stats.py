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

def count_words(book_text, omit_stop_words=False): # add option to omit stop words, count case sensitive or case insensitive
       
       return

def count_most_common(book, top_words, omit_stop_words=False):
       book = book.lower().split()
       most_common = {}
       
       if omit_stop_words:       
              with open("stopwords.txt") as file:
                     stopwords = set(file.read().splitlines())
       for word in book:
              
              if omit_stop_words and word in stopwords:
                     continue
              elif word not in most_common:
                     most_common[word] = 1
              else:
                     most_common[word] += 1
       sorted_words =  sorted(most_common.items(), key= lambda x: x[1], reverse= True)
       return sorted_words[:top_words]

def count_characters(book_text:str) -> dict: # add option to count case sensitive or case insensitive
       characters = {}
       for char in book_text:
              if char.isalpha():
                     try:
                            characters[char] += 1
                     except KeyError:
                            characters[char] = 1     
       return characters

def sort_result(data_dict:dict, reverse: bool = True) -> list:
       report = sorted(data_dict.items(), key= lambda x: x[1], reverse= reverse)
       return report

def create_report(report, result, book_path, top_words):
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

