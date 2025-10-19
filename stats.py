def word_counter(string):
    words = string.split()
    return len(words)

def char_counter(string):
    result = {}
    for ch in string:
        chl = ch.lower()
        if chl in result:
            result[chl] += 1
        else:
            result[chl] = 1
    return result

def sort_on(val):
    return val["num"]

def sorted_list(dict):
    solution=[]
    for char in dict:
        solution.append({"char" : char, "num" : dict[char]})
    solution.sort(reverse=True, key=sort_on)
    return solution
    
