import re
import argparse

def count_words(book):
       return f"Found {len(book.split())} total words"

def count_most_common(book, top_words):
       book = book.lower().split()
       most_common = {}
       pattern = r"[^\w\s]"
       with open("stopwords.txt") as file:
                     stopwords = set(file.read().splitlines())
       for word in book:
              word = re.sub(pattern, "", word)
              
              if word in stopwords:
                     continue
              elif word not in most_common:
                     most_common[word] = 1
              else:
                     most_common[word] += 1
       sorted_words =  sorted(most_common.items(), key= lambda x: x[1], reverse= True)
       return sorted_words[:top_words]

def count_characters(book):
       book = book.lower()
       result = {}
       for char in book:
              if char.isalpha():
                     try:
                            result[char] += 1
                     except KeyError:
                            result[char] = 1     
       return result

def sort_result(chars):
       report = []
       for char in chars:
              report.append({"character": char, "count": chars[char]})
       report.sort(key=lambda character: character["count"], reverse=True)
       return report

def create_report(report, result, book_path, top_words):
       print("============ BOOKBOT ============")
       print(f"Analyzing book found at {book_path}")
       print("----------- Word Count ----------")
       print(result)
       print("--------- Character Count -------")
       for char in report:
              print(f"{char["character"]}: {char["count"]}")
       for word in top_words:
              print(f"{word[0]}: {word[1]}")
       print("============= END ===============")

