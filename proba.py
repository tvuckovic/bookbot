
dict = {
    "a":8,
    "b":15,
    "c":2,
    "d":199,
    "e":0,
    "f":10
}

vehicles = []
for d in dict:
    vehicles.append({"name":d, "num":dict[d]})

def kljuc(dict):
    return dict["num"]

sortirano = vehicles.sort(key=kljuc)


print(vehicles)