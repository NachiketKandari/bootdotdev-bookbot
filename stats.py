def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_char(text):
    my_dict = {}
    for char in text.lower():
        if char == " " or char == "\n":
            continue
        if char in my_dict:
            my_dict[char] +=1
        else:
            my_dict[char] = 1

    return my_dict

def sort_on(items):
    return items["count"]

def get_sorted_dict(my_dict):
    new_list_of_dicts = []
    new_dict = {}

    for key, value in my_dict.items():
        new_list_of_dicts.append({"char":key, "count":value})
    
    new_list_of_dicts.sort(reverse=True, key = sort_on)

    
    for list_item in new_list_of_dicts:
        new_dict[list_item["char"]] = list_item["count"]
    
    return new_dict
