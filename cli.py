import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Bookbot - tool for text fiels analizing")
    parser.add_argument("file_path")
    return parser.parse_args()