def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    char_counts = {}
    lowercase_text = text.lower()
    
    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else: 
            char_counts[char] = 1
    return char_counts

def get_sorted_list(char_counts_dict):
    def sort_on(item):
        return item["num"]

    dict_list = []
    for char in char_counts_dict:
        dict_list.append({"char": char, "num": char_counts_dict[char]})
    
    dict_list.sort(reverse=True, key=sort_on)
    return(dict_list)