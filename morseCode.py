def morseCode(words):
    sol_arr = []
    morse_dict = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..'}
    words = list(map(lambda item: item.upper(), words))
    for item in words:
        running = ""
        for little_item in item:
            running += morse_dict[little_item]
        sol_arr.append(running)
    return len(set(sol_arr))

    
print(morseCode(["gin", "zen", "gig", "msg"]))