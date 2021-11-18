from prj import *

def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i

        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j

        #swap with first
        lista[i], lista[min_index] = lista[min_index], lista[i]

    return lista

def bubble_sort(lista):
    size = len(lista)

    while size != 0:
        for i in range(0, size-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
        
        size -= 1

    return lista

ls = [64,25,12,22,11]


tuplo = (1,2,3,4,5,6,7,8)

dictionary = {"especie": "coelho", "fome":2, "idade":0}

#Modificadores
def aumenta_idade(animal):
    animal["idade"] += 1

    return animal

aumenta_idade(dictionary)

#print(dictionary)


def copia(elem):
    if type(elem) == dict:
        return {copia(key): copia(elem[key]) for key in elem}

    if type(elem) == list:
        return [copia(e) for e in elem][::]

    if type(elem) == tuple:
        return tuple(copia(e) for e in elem)[::]

    return elem

dim = cria_posicao(11, 4)
obs = ()#(cria_posicao(4,2), cria_posicao(5,2))
an1 = tuple(cria_animal("rabbit", 5, 0) for i in range(3))
an2 = (cria_animal("lynx", 20, 15),)
pos = tuple(cria_posicao(p[0],p[1]) for p in ((5,1),(7,2),(10,1),(6,1)))
prado = cria_prado(dim, obs, an1+an2, pos)
#print(prado)

print(prado)
print(id(prado))
for i in prado:
    print(id(i))
print("\n===========\n")

x = copia(prado)
print(x)
print(id(x))
for i in x:
    print(id(i))

