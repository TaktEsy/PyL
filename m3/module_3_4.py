def single_root_words (root_word, *other_words):
    same_words = []

    for w in other_words:
        if root_word.lower() in w.lower():
            same_words.append(w)
        # Если а != в, это ещё не значит что в != а...
        elif w.lower() in root_word.lower():
            same_words.append(w)

    print(same_words)

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')