import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Bookbot - tool for text fiels analizing")
    parser.add_argument("file", type=str, help="path to the text file")

    return parser.parse_args()