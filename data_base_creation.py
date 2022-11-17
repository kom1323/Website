import json
import os



master_data = {}


def get_dict_from_data(data) -> dict:

    words_dic = {}
    sec = {}
    words_to_remove = ["text", "start", "duration"]
    
# , "I", "the", "like", "to", "that", "of", "a", "and",
#                     "you", "is", "in", "think", "it", "so", "but", "yeah", "if", "we", "was", "he", "know", "for",
#                      "have", "dont", "on", "do", "its", "not", "what", "the'", "they", "because", "Im", "um", "at", "be",
#                      "or", "could", "well", "just", "can", "get", "are", "okay", "as", "going", "from"]


    for word in data.split():
        word = word.replace("'", "")
        word = word.replace(".", "")
        word = word.replace("{", "")
        word = word.replace("}", "")
        word = word.replace(":", "")

        if word not in words_to_remove and word.isalpha():
            words_dic[word] = words_dic.setdefault(word, 0) + 1


    sec = {k: v for k, v in sorted(words_dic.items(), key=lambda item: item[1])}

    return sec





for filename in os.listdir(f"{os.getcwd()}/videos_data"):
    with open(os.path.join(f"{os.getcwd()}/videos_data", filename), 'r') as f: # open in readonly mode
        
        data = f.read()
    

