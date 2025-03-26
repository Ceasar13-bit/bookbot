def parse_user_command(user_input:str) -> str:
    command_parsers = {
        "top": lambda args: {"n": int(args[0])},
        "lowercase": lambda args: {},
        "omit_stop_words": lambda args: {},
        "count_characters": lambda args: {}
    }
    tokens = user_input.lower().strip().split()
    cmd = tokens[0]
    args = tokens[1:]
    if cmd in command_parsers:
        parser = command_parsers[cmd]
        param = parser(args)
        return (cmd, param)
    raise Exception("unknown command")