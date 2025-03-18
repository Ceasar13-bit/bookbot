import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Bookbot - tool for text fiels analizing")
    parser.add_argument("file_path", type=str, help="path to the text file")
    parser.add_argument("--omit_stop_words", action="store_true", help="Remove stopwords from words count")

    return parser.parse_args()