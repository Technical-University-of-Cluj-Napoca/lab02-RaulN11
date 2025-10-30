from typing import DefaultDict


def group_anagrams(strs:list[str])->list[list[str]]:
    dicti = DefaultDict(list)
    result = [[]]
    chars=[]
    for s in strs:
        for c in s:
            chars.append(c)
        chars.sort()
        sortd=''.join(chars)
        dicti[sortd].append(s)
        chars=[]
    result=list(dicti.values())
    return result

if __name__=="__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "baboon", "boat"]))
    pass