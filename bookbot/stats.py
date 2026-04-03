import sys


def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read()
    return text

def counting_words(text):
    words = text.split()
    counter = 0
    for word in words:
        counter +=1
    return counter

def counting_characters(text):
    chars_list = set()
    chars_dic = {}
    for buchstabe in text.lower():
        if buchstabe not in chars_list:
            chars_list.add(buchstabe)
            chars_dic[buchstabe] = 0
        if buchstabe in chars_list:
            chars_dic[buchstabe] += 1
    return chars_dic

def making_dict_sortready(dict):
    sortready= []
    for key in dict:
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = dict[key]
        sortready.append(new_dict)
        sortready.sort(reverse=True, key=sort_on)
    return sortready

def sort_on(dict):
    return dict["num"]

def printing_dict(sorted_dicts):
    for dict in sorted_dicts:
        print(f"{dict["name"]}: {dict["num"]}")

