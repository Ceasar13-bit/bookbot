def parse_user_command(user_input:str) -> str:
    command_parsers = {
        "top": lambda args: {"count": 1} if not args else {"count": int(args[0])}, #like that for all f with default args
        "lower_text": lambda args: {},
        "omit_stop_words": lambda args: {"stopwords_path": "stopwords.txt"},
        "count_characters": lambda args: {},
        "count_words": lambda args: {},
        "clean_text" : lambda args: {},
        "sort" : lambda args: {"reverse": True}
    }
    tokens = user_input.split()
    cmd = tokens[0]
    args = tokens[1:]
    if cmd in command_parsers:
        parser = command_parsers[cmd]
        param = parser(args)
        return (cmd, param)
    raise Exception("unknown command")