def replace_words(dictionary, sentence):
    sentence = sentence.split(" ")
    dictionary.sort(key=lambda x: len(x), reverse=True)
    for idx, item in enumerate(sentence):
        for other_item in dictionary:
            if other_item in item and item[:len(other_item)] == other_item:
                sentence[idx] = other_item
    return " ".join(sentence)
