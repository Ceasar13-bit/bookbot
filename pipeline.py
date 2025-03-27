from stats import *
pipeline_map = {
              "omit_stop_words" : omit_stop_words,
              "top" : get_top_n_sorted,
              "lower_text" : lowercase_text,
              "clean_tex" : clean_text,
              "count_words" : count_words,
              "count_characters" : count_characters,
              "sort" : sort_result,
       }