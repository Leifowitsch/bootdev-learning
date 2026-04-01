def filter_messages(messages):
    if len(messages) == 0:
        return [],[]
    liste_ohne_dang = []
    dang_anzahl = []
    dang_counter = 0
    for message in messages:
        dang_counter = 0
        words = message.split()
        laenge = len(words)
        for i in range(laenge-1,-1,-1):
            if words[i] == "dang":
                dang_counter +=1
                del words[i]
        sentence = " ".join(words)
        liste_ohne_dang.append(sentence)
        dang_anzahl.append(dang_counter)
    return liste_ohne_dang, dang_anzahl

messagess = [
            "well dang it",
            "dang the whole dang thing",
            "kill that knight, dang it",
            "get him!",
            "donkey kong",
            "oh come on, get them",
            "run away from the dang baddies",
        ]
print(filter_messages(messagess))
