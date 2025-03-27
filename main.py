from stats import *
from cli import get_args
from pipeline import pipeline_map
from input_handler import parse_user_command
import sys

def main():
       args = get_args()
       book_path = args.file_path
       book_text = get_book_text(book_path)
       data = book_text
       active_steps = []
       while True:
              user_command = input(">>")

              if user_command == "run":
                     for step_name, params in active_steps:
                            func = pipeline_map[step_name]
                            data = func(data, **params)
                     print(data)
                     active_steps = []
                     data = book_text
              elif user_command in pipeline_map:
                     active_steps.append(parse_user_command(user_command))
                     print(active_steps)
              
       
       



if __name__ == "__main__":
       main()