def word_counter(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def character_counter(book_text):
    text_lowered = book_text.lower()
    character_counts = dict()

    for char in text_lowered:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts

def character_dict_sorter(character_dict):
    dict_list = []
    for char_pair in character_dict:
        new_dict = dict()
        new_dict["char"] = char_pair
        new_dict["num"] = character_dict[char_pair]
        dict_list.append(new_dict)
    ## Sorting Function
    def sort_on(items):
        return items["num"]
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list