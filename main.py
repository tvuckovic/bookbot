def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        rijeci = word_count(file_contents)
        slova = character_count(file_contents)

        a = sortirano(slova)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{rijeci} words found in the document")
        print(" ")
        for slovo in a:
            if slovo["name"] in "abcdefghijklmnopqrstuvwxyz":
                print(f"The '{slovo["name"]}' character was found {slovo["num"]} times")
        print("--- End report ---")


def word_count(knjiga):
    splitano = knjiga.split()
    return len(splitano)

def character_count(knjiga):
    result = {}
    prava_knjiga = knjiga.lower()
    for letter in prava_knjiga:
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result

def sortirano(slova_sort):
    lista = []
    for slovo in slova_sort:
        lista.append({"name":slovo, "num":slova_sort[slovo]})
    
    def key(lista):
        return lista["num"]
    
    lista.sort(reverse=True, key=key)
    return lista

main()
