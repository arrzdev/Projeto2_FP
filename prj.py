#posicao: (2,7) coluna 2, linha 7

# -- TAD posicao -- #

#Contrutores
def cria_posicao(x:int, y:int) -> tuple:
    '''
    Esta funcção é um construtor que recebe os valores correspondentes às coordenadas de uma posição e devolve a posição correspondente. Os argumentos são verificados, gerando um ValueError com a mensagem "cria_posicao: argumentos invalidos" caso os seus argumentos não sejam válidos

    PARAMETERS
    ----------
    - x: int
    \n\tCordenada x
    - y: int
    \n\tCordenada y

    RETURN
    ------
    - posicao: tuple:
    \n\tPosicao, correspondente as cordenadas x e y
    '''

    if type(x) != int or type(y) != int or x<0 or y<0:
        raise ValueError("cria_posicao: argumentos invalidos")
    
    posicao = (x,y) 
    return  posicao

def cria_copia_posicao(posicao:tuple) -> tuple:
    '''
    Esta funcção recebe uma posição e devolve uma cópia nova da posição
    '''

    return posicao.copy()

#Seletores
def obter_pos_x(posicao:tuple) -> int:
    '''
    Esta função recebe uma posição e devolve a componente x
    '''

    return posicao[0]

def obter_pos_y(posicao:tuple) -> int:
    '''
    Esta função recebe uma posição e devolve a componente y
    '''

    return posicao[1]

#Reconhecedor
def eh_posicao(argumento) -> bool:
    '''
    Esta função devolve um boolean, True se o seu argumento for um TAD posicão e False caso contrário
    '''

    if type(argumento) == tuple and len(argumento) == 2 and type(argumento[0]) == int and type(argumento[1]) == int and argumento[0] >= 0 and argumento[1] >= 0:
        return True

    #otherwise
    return False

#Teste
def posicoes_iguais(posicao1:tuple, posicao2:tuple) -> bool:
    '''
    Esta função retorna um boolean, True se as posições forem iguais, False caso contrário.
    '''

    res = posicao1 == posicao2
    return res

#Transformador
def posicao_para_str(posicao:tuple) -> str:
    '''
    Esta função retorna a cadeia de caracteres "(x,y)" que representa o seu argumento, sendo os valores x e y as cordenadas da posicao
    '''
    return str(posicao)

#Alto Nivel
def obter_posicoes_adjacentes(posicao:tuple) -> tuple:
    '''
    Esta função recebe uma posição e devolve um tuplo com as posições adjacentes a essa posição, começando pela posição acima e seguindo no sentido horário
    '''

    x = obter_pos_x(posicao)
    y = obter_pos_y(posicao)

    posicoes_adjacentes = ()

    #cima
    if y != 0:
        posicoes_adjacentes += (cria_posicao(x, y-1),)

    #direita (como nao temos o tamanho do tabuleiro não da para verificar nada)
    posicoes_adjacentes += (cria_posicao(x+1, y),)
    
    #baixo (como nao temos o tamanho do tabuleiro não da para verificar nada)
    posicoes_adjacentes += (cria_posicao(x, y+1),)

    #esquerda
    if x != 0:
        posicoes_adjacentes += (cria_posicao(x-1, y),)

    return posicoes_adjacentes

def ordenar_posicoes(posicoes:tuple) -> tuple:
    '''
    Esta função recebe um tuplo contendo posições e devolve um tuplo contendo essas mesmas posições ordenadas pela ordem de leitura do prado 
    '''
    
    #Implementação do algoritmo de sort (complexidade: n!)
    sorted_tuple = ()

    for _ in range(len(posicoes)):
        min_index = 0

        for i in range(len(posicoes)):
            if obter_pos_y(posicoes[i]) < obter_pos_y(posicoes[min_index]):
                min_index = i
            elif obter_pos_y(posicoes[i]) == obter_pos_y(posicoes[min_index]):
                if obter_pos_x(posicoes[i]) < obter_pos_x(posicoes[min_index]):
                    min_index = i
        
        #"adicionar" o nosso melhor valor ao tuplo dos sorted
        sorted_tuple += (posicoes[min_index],)

        #"remover" do tuplo non-sorted o valor que foi selecionado
        posicoes = posicoes[:min_index] + posicoes[min_index+1:]
            
    return sorted_tuple

#-------------------#

# -- TAD animal -- #

#Construtores
def cria_animal(especie:str, f_reproducao:int, f_alimentacao:int) -> dict:
    '''
    Esta função recebe uma cadeia de caracteres não vazia correspondente à espécie do animal e dois valores inteiros correspondentes à frequência de reprodução (maior do que 0) e à frequência de alimentação a (maior ou igual a 0); e devolve o animal. Animais com frequência de alimentação maior que 0 são considerados predadores, caso contrário são considerados presas. A função verifica a validade dos seus argumentos, gerando um ValueError com a mensagem "cria_animal: argumentos invalidos" caso os seus argumentos não sejam válidos.
    '''

    if type(especie) != str or type(f_reproducao) != int or type(f_alimentacao) != int or f_reproducao <= 0 or f_alimentacao < 0:
        raise ValueError("cria_animal: argumentos invalidos")

    animal = {
        "especie": especie,
        "f_reproducao": f_reproducao,
        "f_alimentacao": f_alimentacao,
        "idade": 0,
        "fome": 0
    }

    return animal

def cria_copia_animal(animal):
    return animal.copy()
    
#Seletores
def obter_especie(animal):
    return animal["especie"]

def obter_freq_reproducao(animal):
    return animal["f_reproducao"]

def obter_freq_alimentacao(animal):
    return animal["f_alimentacao"]

def obter_idade(animal):
    return animal["idade"]

def obter_fome(animal):
    return animal["fome"]


#Modificadores
def aumenta_idade(animal):
    animal["idade"] += 1

    return animal

def reset_idade(animal):
    animal["idade"] = 0

    return animal

def aumenta_fome(animal):
    if animal["f_alimentacao"] != 0:
        animal["fome"] += 1

    return animal

def reset_fome(animal):
    animal["fome"] = 0

    return animal


#Reconhecedores
def eh_animal(animal):
    if type(animal) != dict or len(animal) != 5:
        return False

    keys = animal.keys()
    if "especie" not in keys or "f_reproducao" not in keys or "f_alimentacao" not in keys or "idade" not in keys or "fome" not in keys:
        return False

    especie = animal["especie"]
    f_reproducao = animal["f_reproducao"]
    f_alimentacao = animal["f_alimentacao"]
    idade = animal["idade"]
    fome = animal["fome"]

    if type(especie) != str or not especie.isalpha():
        return False

    if type(f_reproducao) != int or type(f_alimentacao) != int or f_reproducao <= 0 or f_alimentacao < 0:
        return False
    
    if type(idade) != int or type(fome) != int or idade < 0 or fome < 0:
        return False

    return True

def eh_predador(animal):
    #se f_alimentacao > 0, return True, False otherwise
    return bool(animal["f_alimentacao"])
    
def eh_presa(animal):
    return not bool(animal["f_alimentacao"])


#Teste
def animais_iguais(animal1, animal2):
    return animal1 == animal2 and eh_animal(animal1) and eh_animal(animal2)


#Transformadores
def animal_para_char(animal):
    caracter = animal["especie"][0]

    if eh_predador(animal):
        return caracter.upper()
    else:
        return caracter.lower()

def animal_para_str(animal):
    niveis = []

    if animal["f_reproducao"] != 0:
        niveis.append(f"{animal['idade']}/{animal['f_reproducao']}")

    if animal["f_alimentacao"] != 0:
        niveis.append(f"{animal['fome']}/{animal['f_alimentacao']}")

    niveis_string = ";".join(niveis)

    return f"{animal['especie']} [{niveis_string}]"


#Alto nivel
def eh_animal_fertil(animal):
    if animal["idade"] >= animal["f_reproducao"]:
        return True

    return False

def eh_animal_faminto(animal):
    if animal["fome"] >= animal["f_alimentacao"]:
        return True

    return False        

def reproduz_animal(animal):
    filho = cria_copia_animal(animal)

    #modificar o pai
    animal["idade"] = 0

    #modificar o filho
    filho["idade"] = 0
    filho["fome"] = 0

    return filho



#------------------#



















