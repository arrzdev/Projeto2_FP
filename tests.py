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

print(dictionary)

