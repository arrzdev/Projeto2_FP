#posicao: (2,7) coluna 2, linha 7

#from functools import reduce

# -- AUXILIARES -- #
def deep_copy(elem):
    if type(elem) == dict:
        return {deep_copy(key): deep_copy(elem[key]) for key in elem.copy()}

    if type(elem) == list:
        return [deep_copy(e) for e in elem.copy()]

    if type(elem) == tuple:
        return tuple(deep_copy(e) for e in elem[::])

    return elem




# ---------------- #

# -- TAD posicao -- #

#Construtores
def cria_posicao(x:int, y:int) -> tuple:
    '''
    Esta funcção é um construtor que recebe os valores correspondentes às coordenadas de uma posição e devolve a posição correspondente. Os argumentos são verificados, gerando um ValueError com a mensagem "cria_posicao: argumentos invalidos" caso os seus argumentos não sejam válidos
    '''

    if type(x) != int or type(y) != int or x<0 or y<0:
        raise ValueError("cria_posicao: argumentos invalidos")
    
    posicao = (x,y) 
    return posicao

def cria_copia_posicao(posicao:tuple) -> tuple:
    '''
    Esta funcção recebe uma posição e devolve uma cópia nova da posição
    '''

    return deep_copy(posicao)

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

    if type(argumento) != tuple or len(argumento) != 2:
        return False

    if type(argumento[0]) != int or type(argumento[1]) != int:
        return False
    
    if argumento[0] < 0 or argumento[1] < 0:
        return False

    return True

#Teste
def posicoes_iguais(posicao1:tuple, posicao2:tuple) -> bool:
    '''
    Esta função retorna um boolean, True se as posições forem iguais, False caso contrário.
    '''

    return eh_posicao(posicao1) and eh_posicao(posicao2) and posicao1 == posicao2

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

    #inverter o tuplo posicao e ordenar dessa forma.. 1º a linha; 2º a coluna
    posicoes_ordenadas = tuple(sorted(posicoes, key=lambda x: (obter_pos_y(x), obter_pos_x(x))))

    return posicoes_ordenadas

#-------------------#   

# -- TAD animal -- #

#Construtores
def cria_animal(especie:str, f_reproducao:int, f_alimentacao:int) -> dict:
    '''
    Esta função recebe uma cadeia de caracteres não vazia correspondente à espécie do animal e dois valores inteiros correspondentes à frequência de reprodução (maior do que 0) e à frequência de alimentação a (maior ou igual a 0); e devolve o animal. Animais com frequência de alimentação maior que 0 são considerados predadores, caso contrário são considerados presas. A função verifica a validade dos seus argumentos, gerando um ValueError com a mensagem "cria_animal: argumentos invalidos" caso os seus argumentos não sejam válidos.
    '''

    if type(especie) != str or len(especie) == 0 or type(f_reproducao) != int or type(f_alimentacao) != int or f_reproducao <= 0 or f_alimentacao < 0:
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
    #AQUI: Posso usar o reconhecedor que vou definir a seguir para verificar se isto é um animal e entao fazer a copia?
    return deep_copy(animal)
    
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

    if "especie" not in animal or "f_reproducao" not in animal or "f_alimentacao" not in animal or "idade" not in animal or "fome" not in animal:
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
    return eh_animal(animal) and bool(animal["f_alimentacao"])
    
def eh_presa(animal):
    return eh_animal(animal) and not bool(animal["f_alimentacao"]) 

#Teste
def animais_iguais(animal1, animal2):
    return eh_animal(animal1) and eh_animal(animal2) and animal1 == animal2 

#Transformadores
def animal_para_char(animal):
    caracter = obter_especie(animal)[0]

    if eh_predador(animal):
        return caracter.upper()
    else:
        return caracter.lower()

def animal_para_str(animal):

    especie = obter_especie(animal)

    f_reproducao = obter_freq_reproducao(animal)
    f_alimentacao = obter_freq_alimentacao(animal)

    idade = obter_idade(animal)
    fome = obter_fome(animal)

    niveis = []

    if f_reproducao != 0:
        niveis.append(f"{idade}/{f_reproducao}")

    if f_alimentacao != 0:
        niveis.append(f"{fome}/{f_alimentacao}")

    niveis_string = ";".join(niveis)

    return f"{especie} [{niveis_string}]"


#Alto nivel
def eh_animal_fertil(animal):
    if obter_idade(animal) >= obter_freq_reproducao(animal):
        return True

    return False

def eh_animal_faminto(animal):
    if eh_predador(animal) and obter_fome(animal) >= obter_freq_alimentacao(animal):
        return True

    return False        

def reproduz_animal(animal):
    filho = cria_copia_animal(animal)

    #modificar o pai
    reset_idade(animal)

    #modificar o filho
    reset_idade(filho)
    reset_fome(filho)

    return filho

#------------------#


# -- TAD prado -- #
#Construtores
def cria_prado(posicao_infd:tuple, posicoes_rochedos:tuple, animais:tuple, posicoes_animais:tuple) -> dict:
    
    if not eh_posicao(posicao_infd):
        raise ValueError("cria_prado: argumentos invalidos")


    if type(posicoes_rochedos) != tuple:
        raise ValueError("cria_prado: argumentos invalidos")

    #verificar se todos os elementos dos rochedos sao posicoes e estao dentro do tabuleiro
    for posicao_rochedo in posicoes_rochedos:
        if not eh_posicao(posicao_rochedo):
            raise ValueError("cria_prado: argumentos invalidos")

        if not(obter_pos_x(posicao_infd) > obter_pos_x(posicao_rochedo) > 0):
            raise ValueError("cria_prado: argumentos invalidos")

        if not(obter_pos_y(posicao_infd) > obter_pos_y(posicao_rochedo) > 0):
            raise ValueError("cria_prado: argumentos invalidos")        
        
        #verificar se aparece a mesma posição várias vezes
        if posicoes_rochedos.count(posicao_rochedo) > 1:
            raise ValueError("cria_prado: argumentos invalidos")


    #verificação dos animais
    if type(animais) != tuple or len(animais) == 0:
        raise ValueError("cria_prado: argumentos invalidos")


    if type(posicoes_animais) != tuple or len(posicoes_animais) != len(animais):
        raise ValueError("cria_prado: argumentos invalidos")

    for posicao_animal in posicoes_animais:
        if not eh_posicao(posicao_animal):
            raise ValueError("cria_prado: argumentos invalidos")

        if not(obter_pos_x(posicao_infd) > obter_pos_x(posicao_animal) > 0):
            raise ValueError("cria_prado: argumentos invalidos")

        if not(obter_pos_y(posicao_infd) > obter_pos_y(posicao_animal) > 0):
            raise ValueError("cria_prado: argumentos invalidos")

        #no mesmo sitio de um rochedo
        if posicao_animal in posicoes_rochedos:
            raise ValueError("cria_prado: argumentos invalidos")

        #verificar se aparece a mesma posição várias vezes
        if posicoes_animais.count(posicao_animal) > 1:
            raise ValueError("cria_prado: argumentos invalidos")


    prado = {
        "tamanho": (obter_pos_x(posicao_infd)+1, obter_pos_y(posicao_infd)+1),
        "rochedos": posicoes_rochedos,
        "animais": {posicoes_animais[i]: animais[i] for i in range(len(posicoes_animais))}
    }

    return prado

def cria_copia_prado(prado: dict) -> dict:
    return deep_copy(prado)

#Seletores
def obter_tamanho_x(prado:dict) -> int:
    return prado["tamanho"][0]

def obter_tamanho_y(prado:dict) -> int:
    return prado["tamanho"][1]

def obter_numero_predadores(prado:dict) -> int:
    animais_e_posicoes = prado["animais"]

    animais = animais_e_posicoes.values()

    return len(list(filter(lambda x: eh_predador(x), animais)))

def obter_numero_presas(prado:dict) -> int:
    animais_e_posicoes = prado["animais"]

    animais = animais_e_posicoes.values()

    return len(list(filter(lambda x: eh_presa(x), animais)))

def obter_posicao_animais(prado:dict) -> tuple:
    posicoes_e_animais = prado["animais"]

    posicoes = posicoes_e_animais.keys()

    #inverter o tuplo posicao e ordenar dessa forma.. 1º a linha; 2º a coluna
    posicoes_ordenadas = ordenar_posicoes(posicoes)

    return posicoes_ordenadas

def obter_animal(prado:dict, posicao:tuple) -> dict:
    
    animais = prado["animais"]

    return animais[posicao]

#Modificadores
def eliminar_animal(prado:dict, posicao:tuple) -> dict:
    animais = prado["animais"]

    #del animal
    del animais[posicao]

    return prado

def mover_animal(prado:dict, posicao:tuple, nova_posicao:tuple) -> dict:
    animais = prado["animais"]

    animais[nova_posicao] = animais[posicao]
    
    eliminar_animal(prado, posicao)

    return prado

def inserir_animal(prado:dict, animal:dict, posicao:tuple) -> dict:
    
    animais = prado["animais"]

    animais[posicao] = animal

    return prado



#Reconhecedores
def eh_prado(prado) -> bool:
    if type(prado) != dict or len(prado) != 3:
        return False
    
    #check keys
    if "tamanho" not in prado or "rochedos" not in prado or "animais" not in prado:
        return False

    if type(prado["tamanho"]) != tuple or len(prado["tamanho"]) != 2:
        return False

    if type(prado["rochedos"]) != tuple:
        return False

    if type(prado["animais"]) != dict:
        return False

    for posicao, animal in enumerate(prado["animais"]):
        if not eh_posicao(posicao):
            return False

        if not eh_animal(animal):
            return False

    return True

def eh_posicao_animal(prado:dict, posicao:tuple) -> bool:
    for pos in obter_posicao_animais(prado):
        if posicoes_iguais(pos, posicao):
            return True
    
    return False

def eh_posicao_obstaculo(prado:dict, posicao:tuple) -> bool:
    for pos in prado["rochedos"]:
        if posicoes_iguais(pos, posicao):
            return True
        
    if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0 or obter_pos_x(posicao) == obter_tamanho_x(prado)-1 or obter_pos_y(posicao) == obter_tamanho_y(prado)-1:
        return True

    return False

def eh_posicao_livre(prado:dict, posicao:tuple) -> bool:
    if not eh_posicao_animal(prado, posicao) and not eh_posicao_obstaculo(prado, posicao):
        return True
    
    return False

#Teste
def prados_iguais(prado1:dict, prado2:dict) -> bool:
    #AQUI: ?????????????
    return eh_prado(prado1) and eh_prado(prado2) and prado1 == prado2


#Transformador
def prado_para_str(prado:dict) -> str:
    
    tamanho_x = obter_tamanho_x(prado)
    tamanho_y = obter_tamanho_y(prado)

    linhas = []
    for y in range(tamanho_y):
        linha = ""
        
        for x in range(tamanho_x):
            posicao = cria_posicao(x, y)

            if eh_posicao_obstaculo(prado, posicao):
                if x == 0 or x == tamanho_x-1:
                    if y == 0 or y == tamanho_y-1:
                        linha += "+"
                    else:
                        linha += "|"
                elif y == 0 or y == tamanho_y-1:
                    linha += "-"

                #rochedos
                else:
                    linha += "@"
            
            #animais
            elif eh_posicao_animal(prado, posicao):
                animal = obter_animal(prado, posicao)
                linha += animal_para_char(animal)
            
            else:
                linha += "."

        #append
        linhas.append(linha)

    return "\n".join(linhas)


#Alto Nivel
def obter_valor_numerico(prado:dict, posicao:tuple) -> int:
    tamanho_x = obter_tamanho_x(prado)

    linha_y = obter_pos_y(posicao)
    coluna_x = obter_pos_x(posicao)

    #atraves da formula
    valor_numerico = (tamanho_x * linha_y) + coluna_x

    return valor_numerico
     
def obter_movimento(prado:dict, posicao:tuple) -> tuple:
    valor_numerico = obter_valor_numerico(prado, posicao)

    posicoes_adjacentes = obter_posicoes_adjacentes(posicao)

    animal = obter_animal(prado, posicao)

    #se for predador
    if eh_predador(animal):
        
        #posições disponiveis
        posicoes_disponiveis = [posicao_t for posicao_t in posicoes_adjacentes if eh_posicao_livre(prado, posicao_t) or (eh_posicao_animal(prado, posicao_t) and eh_presa(obter_animal(prado, posicao_t)))]

        #se nao houver posicoes disponiveis
        if len(posicoes_disponiveis)  == 0:
            return posicao

        #posicoes com presas
        posicoes_presas = [posicao_t for posicao_t in posicoes_disponiveis if eh_posicao_animal(prado, posicao_t) and eh_presa(obter_animal(prado, posicao_t))]

        #se nao houver presas 
        if len(posicoes_presas) == 0:
            return posicoes_disponiveis[valor_numerico % len(posicoes_disponiveis)]

        '''#Se houver só 1 presa
        if len(posicoes_presas) == 1:
            return posicoes_presas[0]'''
        
        #se houver presas
        return posicoes_presas[valor_numerico % len(posicoes_presas)]

    #se for presa
    elif eh_presa(animal):
        #posições disponiveis
        posicoes_disponiveis = [posicao_t for posicao_t in posicoes_adjacentes if eh_posicao_livre(prado, posicao_t)]

        #se nao houver posicoes livre
        if len(posicoes_disponiveis) == 0:
            return posicao  
        
        #caso contrario escolher 1 delas
        return posicoes_disponiveis[valor_numerico % len(posicoes_disponiveis)]

'''
dim = cria_posicao(11, 4)
obs = (cria_posicao(4,2), cria_posicao(5,2))
an1 = tuple(cria_animal("rabbit", 5, 0) for i in range(3))
an2 = (cria_animal("lynx", 20, 15),)
pos = tuple(cria_posicao(p[0],p[1]) for p in ((5,1),(7,2),(10,1),(6,1)))
prado = cria_prado(dim, obs, an1+an2, pos)
obter_tamanho_x(prado), obter_tamanho_y(prado)

print(prado_para_str(prado))
p1 = cria_posicao(7,2)
p2 = cria_posicao(9,3)
prado = mover_animal(prado, p1, p2)

print(prado)
print(prado_para_str(prado))
print(obter_valor_numerico(prado, cria_posicao(9,3)))
print(posicao_para_str(obter_movimento(prado, cria_posicao(5,1))))
print("\n")
print(posicao_para_str(obter_movimento(prado, cria_posicao(6,1))))
print("\n")
print(posicao_para_str(obter_movimento(prado, cria_posicao(10,1))))
'''

#-----------------#



def geracao(prado:dict) -> dict:

    posicoes_animais = obter_posicao_animais(prado)
    animais_mortos = []
    

    for posicao in posicoes_animais:
        
        #se o animal tiver sido morto
        for pos in animais_mortos:
            if posicoes_iguais(pos, posicao):
                continue

        animal = obter_animal(prado, posicao)

        aumenta_fome(animal)
        aumenta_idade(animal)

        nova_posicao = obter_movimento(prado, posicao)

        if not posicoes_iguais(posicao, nova_posicao):
            #visto que na funcao obter movimento nos excluimos as posicoes\
            # com predadores podemos so verificar se a posicao e um animal
            if eh_posicao_animal(prado, nova_posicao):

                #remover a presa
                eliminar_animal(prado, nova_posicao)
                animais_mortos.append(nova_posicao)
                
                #resetar a fome do predador
                reset_fome(animal)

            mover_animal(prado, posicao, nova_posicao)

            #verificar idade de reproduçao
            if eh_animal_fertil(animal):
                #reproduzir
                filho = reproduz_animal(animal)

                #inserir filho na posicao antiga
                inserir_animal(prado, filho, posicao)

        #verificar a fome 
        if eh_animal_faminto(animal):
            #remover o predador
            eliminar_animal(prado, nova_posicao)

    return prado

def simula_ecossistema(file_name: str, geracoes: int, verboso: bool):
    with open(file_name, "r") as f:
        linhas = f.readlines()

    #clean lines
    linhas_limpas = [linha.replace("\n", "").strip() for linha in linhas]

    inf_d = eval(linhas_limpas[0])
    rochedos = eval(linhas_limpas[1])

    #animais
    animais = ()
    posicoes_animais = ()

    for linha in linhas_limpas[2:]:
        animal_e_posicao = eval(linha)

        animal = animal_e_posicao[:-1]
        posicao = animal_e_posicao[-1]

        #atualizar o tuplo
        animais += (cria_animal(animal[0], animal[1], animal[2]),)
        posicoes_animais += (posicao,)

    #criar prado
    prado = cria_prado(inf_d, rochedos, animais, posicoes_animais)

    for gen in range(0,geracoes+1):
        gen_presas = obter_numero_presas(prado)
        gen_predadores = obter_numero_predadores(prado)

        if (verboso and (gen == 0 or last_gen_predadores != gen_predadores or last_gen_presas != gen_presas)) or (not verboso and (gen == 0 or gen == geracoes)):

            print(f"Predadores: {gen_predadores} vs Presas: {gen_presas} (Gen. {gen})")
            print(prado_para_str(prado))
        
        last_gen_presas = gen_presas
        last_gen_predadores = gen_predadores

        prado = geracao(prado)

    return gen_predadores, gen_presas


dim = cria_posicao(11, 4)
obs = (cria_posicao(4, 2), cria_posicao(5, 2))
an1 = tuple(cria_animal('rabbit', 5, 0) for i in range(3))
an2 = (cria_animal('lynx', 20, 15), )
pos = tuple(
    cria_posicao(p[0], p[1])
    for p in ((5, 1), (7, 2), (10, 1), (6, 1)))
prado = cria_prado(dim, obs, an1 + an2, pos)
'''
for x, y in ((4, 2), (5, 2), (0, 0), (0, 5), (3, 0), (11, 4), (11, 2), (7, 4)):
    pos_obs = cria_posicao(x, y)
    print(eh_posicao_obstaculo(prado, pos_obs))'''

#print(prado_para_str(prado))

#print(eh_posicao_livre(prado, cria_posicao(5, 1)))

'''
dim = cria_posicao(11, 4)
obs = (cria_posicao(4, 2), cria_posicao(5, 2))
an1 = tuple(cria_animal('rabbit', 5, 0) for i in range(3))
an2 = (cria_animal('lynx', 20, 15), )
pos = tuple(
    cria_posicao(p[0], p[1])
    for p in ((5, 1), (7, 2), (10, 1), (6, 1)))
prado = cria_prado(dim, obs, an1 + an2, pos)

for x, y, res in ((5, 1, '(4, 1)'), (6, 1, '(5, 1)'), (10, 1,'(10, 2)')):
    mov = obter_movimento(prado, cria_posicao(x, y))
    print(res == posicao_para_str(mov))
'''

'''
prado = {'tamanho': (12, 5), 'rochedos': ((4, 2), (5, 2)), 'animais': {(5, 1): {'especie': 'rabbit', 'f_reproducao': 5, 'f_alimentacao': 0, 'idade': 0, 'fome': 0}, (7, 2): {'especie': 'rabbit', 'f_reproducao': 5, 'f_alimentacao': 0, 'idade': 0, 'fome': 0}, (10, 1): {'especie': 'rabbit', 'f_reproducao': 5, 'f_alimentacao': 0, 'idade': 0, 'fome': 0}, (6, 1): {'especie': 'lynx', 'f_reproducao': 20, 'f_alimentacao': 15, 'idade': 0, 'fome': 0}}}

copia = cria_copia_prado(prado)

print(prados_iguais(prado, copia))

p1 = cria_posicao(7, 2)
p2 = cria_posicao(9, 3)
prado = mover_animal(prado, p1, p2)

print(prados_iguais(prado, copia))
'''

#x = obter_movimento(prado, cria_posicao(5,1))
#print(simula_ecossistema("config.txt", 20, False))

'''
dim = cria_posicao(5, 16)
animal = cria_animal('rabbit', 5, 0)
posicao = cria_posicao(3, 5)
prado = cria_prado(dim, (), (animal, ), (posicao, ))
print(prado)
'''

#copia = cria_copia_prado(prado)




