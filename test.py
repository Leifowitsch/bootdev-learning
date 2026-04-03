def main():

    dict = {'t': 29493, 'h': 19176, 'e': 44538,}
    sortready= []
    for key in dict:
        new_dict = {}
        new_dict["name"] = key
        new_dict["num"] = dict[key]
        sortready.append(new_dict)
main()