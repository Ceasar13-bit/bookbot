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
              user_command = input(">>").lower().strip()
              command = user_command.split()
              if not command:
                     continue
              elif command[0] == "run":
                     for step_name, params in active_steps:
                            func = pipeline_map[step_name]
                            data = func(data, **params)
                     print(data)
                     active_steps = []
                     data = book_text
              elif command[0] in ("clear", "reset"):
                     active_steps = []
                     print("Pipeline cleared")
              elif command[0] == "exit!":
                     sys.exit()            
              elif command[0] in pipeline_map:
                     active_steps.append(parse_user_command(user_command))
              elif command[0] == "show":
                     for i, step in enumerate(active_steps):
                            params = ", ".join(f"{k}={v}" for k, v in step[1].items()) if step[1] else ""
                            print(f"{i + 1} {step[0]} {params}")
              elif command[0] == "remove":
                     if not active_steps:
                            print("You haven't input any command yet")
                     elif len(command) == 1:
                            removed = active_steps.pop()
                            print(f"removed {removed[0]}")
                     elif len(command) == 2 and command[1].isdigit():
                            if 1 <= int(command[1]) <= len(active_steps):
                                   removed = active_steps.pop(int(command[1]) - 1)
                                   print(f"Removed step {command[1]}: {removed[0]}")
                            else:
                                   print(f"Invalid index: {command[1]}. Use 'show' to see current steps.")
                     else:
                            print("usage: remove <command index number>")
              elif command[0] == "insert":
                     if len(command) == 2 and command[1] in pipeline_map:
                            active_steps.append(parse_user_command(command[1]))
                     elif len(command) == 3 and command[1] in pipeline_map and command[2].isdigit():
                            active_steps.insert(int(command[2]) - 1, parse_user_command(command[1]))
                     else:
                            print("usage: insert <command_name> [index number]")
              else:
                     print("unknown command")
       
if __name__ == "__main__":
       main()