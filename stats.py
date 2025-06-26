def word_count(text):
    words_only = text.split()
    num_words = len(words_only)
    return num_words

def character_count(text):
    text = text.lower()
    counts = {}
    for i in range(0, len(text)):
        if text[i] not in counts:
            counts[text[i]] = 1
        else:
            counts[text[i]] += 1
    return counts

def sorted_dict(dict):
    list_dict = []
    for char in dict:
        one_dict = {"char" : char, "num" : dict[char]}
        list_dict.append(one_dict)
    
    def sort_on(list_dict):
        return list_dict["num"]
    
    list_dict.sort(reverse=True, key=sort_on)

    return list_dict
