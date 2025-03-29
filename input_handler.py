def parse_user_command(user_input:str) -> tuple:
    command_parsers = {
        "top": lambda args: {"count": 1} if not args else {"count": int(args[0])}, 
        "lower_text": lambda args: {},
        "omit_stop_words": lambda args: {"stopwords_path": "stopwords.txt"} if not args else {"stopwords_path": args[0]},
        "count_characters": lambda args: {},
        "count_words": lambda args: {},
        "clean_text" : lambda args: {},
        "sort" : lambda args: {"reverse": True} if not args else {"reverse" : not(args[0].lower() == "false")}
    }
    tokens = user_input.split()
    cmd = tokens[0]
    args = tokens[1:]
    if cmd in command_parsers:
        parser = command_parsers[cmd]
        param = parser(args)
        return (cmd, param)
    raise Exception("unknown command")