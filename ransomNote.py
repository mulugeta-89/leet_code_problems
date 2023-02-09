def ransomNote(ransomNote, magazine):
    # magazine_dict = {}
    # ransom_dict = {}
    # for item in magazine:
    #     if item not in magazine_dict:
    #         magazine_dict[item] = 1
    #     else:
    #         magazine_dict[item] += 1
    # for item in ransomNote:
    #     if item not in ransom_dict:
    #         ransom_dict[item] = 1
    #     else:
    #         ransom_dict[item] +=1
    # for key in ransom_dict.keys():
    #     if key not in magazine_dict.keys():
    #         break
    #     else:
    #         if magazine_dict[key] == ransom_dict[key]:
    #             return True
    # return False
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    flag = False
    for item in ransomNote:
        if item not in magazine:
            flag = False
            break
        else:
            magazine.pop(magazine.index(item))
            flag = True
    return flag

print(ransomNote("fihjjjjei","hjibagacbhadfaefdjaeaebgi"))