from stats import *
from cli import get_args
from pipeline import pipeline_map

def main():
       args = get_args()
       book_path = args.file_path
       book_text = get_book_text(book_path)
      
       active_steps = []
       while True:
              user_command = input(">>")
              tokens = user_command.split()
              command = tokens[0]
              argument = tokens[1]
              if command == "run":
                     ...
              elif command in pipeline_map:
                     ...
              
       
       



if __name__ == "__main__":
       main()