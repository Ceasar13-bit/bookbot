import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Bookbot - tool for text fiels analizing")
    parser.add_argument("file_path", type=str, help="path to the text file")
    parser.add_argument("--omit_stop_words", action="store_true", help="Remove stopwords from words count")
    parser.add_argument("--top", type=int,default=10, help="Display top n words in given text")
    parser.add_argument("--lower_text",action="store_true", help="Lower text")
    parser.add_argument("--clean_text",action="store_true", help="Removes punctuation")
    return parser.parse_args()