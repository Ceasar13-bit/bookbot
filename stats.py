import string

def count_words(book):
       return f"Found {len(book.split())} total words"

def count_characters(book):
       book = book.lower()
       characters = string.printable + "æâêëô" #not needed
       result = {}
       for char in book:
              if char in characters:  #not needed
                     try:
                            result[char] += 1
                     except KeyError:
                            result[char] = 1
              
       return result

def sort_result(chars):
       report = []
       for char in chars:
              if char.isalpha():  #move to upper function
                     report.append({"character": char, "count": chars[char]})
       report.sort(key=lambda character: character["count"], reverse=True)
       return report

def create_report(report, result, book_path):
       print("============ BOOKBOT ============")
       print(f"Analyzing book found at {book_path}")
       print("----------- Word Count ----------")
       print(result)
       print("--------- Character Count -------")
       for char in report:
              print(f"{char["character"]}: {char["count"]}")
       print("============= END ===============")

