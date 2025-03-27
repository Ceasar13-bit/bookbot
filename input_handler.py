def parse_user_command(user_input:str) -> str:
    command_parsers = {
        "top": lambda args: {"n": int(args[0])},
        "lower_text": lambda args: {},
        "omit_stop_words": lambda args: {"s": "stopwords.txt"},
        "count_characters": lambda args: {},
        "count_words": lambda args: {},
        "clean_text" : lambda args: {},
        "sort" : lambda args: {"b": bool(args[0])}
    }
    tokens = user_input.lower().strip().split()
    cmd = tokens[0]
    args = tokens[1:]
    if cmd in command_parsers:
        parser = command_parsers[cmd]
        param = parser(args)
        return (cmd, param)
    raise Exception("unknown command")