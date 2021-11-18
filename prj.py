'''
Esta simulação decorre num prado rodeado por montanhas,
onde, no início, algumas das posições estão ocupadas por
animais (predadores ou presas) e as restantes estão
vazias ou contêm obstáculos. A população do prado evolui
ao longo de etapas de tempo discretas (gerações). A simulação
consiste na construção de gerações sucessivas da população no
prado.

André Filipe Silva Santos
andrefssantos@tecnico.ulisboa.pt
ist1103597

https://github.com/arrzdev
'''


# -- AUXILIARES -- #
def deep_copy(elem):
    '''
    universal → universal

    Esta função recebe qualquer elemento e gera uma copia dele e de todos os elementos que se encontram dentro recursivamente...
    '''
    
    if type(elem) == dict:
        return {deep_copy(key): deep_copy(elem[key]) for key in elem}

    if type(elem) == list:
        return [deep_copy(e) for e in elem]

    if type(elem) == tuple:
        return tuple(deep_copy(e) for e in elem[::])

    return elem

def posicao_para_tuplo(posicao):
    return (obter_pos_x(posicao), obter_pos_y(posicao))

# ---------------- #


# -- TAD posicao -- #

#Construtores
def cria_posicao(x:int, y:int) -> tuple:
    '''
    int × int → posicao

    Esta funcção é um construtor que recebe os valores correspondentes às coordenadas \
    de uma posição e devolve a posição correspondente. Os argumentos são verificados, \
    gerando um ValueError com a mensagem "cria_posicao: argumentos invalidos" caso os \
    seus argumentos não sejam válidos
    '''

    if type(x) != int or type(y) != int or x<0 or y<0:
        raise ValueError("cria_posicao: argumentos invalidos")
    
    posicao = (x,y) 
    return posicao

def cria_copia_posicao(posicao:tuple) -> tuple:
    '''
    posicao → posicao

    Esta funcção recebe uma posição e devolve uma cópia nova da posição
    '''

    return deep_copy(posicao)

#Seletores
def obter_pos_x(posicao:tuple) -> int:
    '''
    posicao → int

    Esta função recebe uma posição e devolve a componente x
    '''

    return posicao[0]

def obter_pos_y(posicao:tuple) -> int:
    '''
    posicao → int

    Esta função recebe uma posição e devolve a componente y
    '''

    return posicao[1]

#Reconhecedor
def eh_posicao(argumento) -> bool:
    '''
    universal → booleano

    Esta função devolve um boolean, True se o seu argumento for um TAD posicão e \
    False caso contrário
    '''

    if type(argumento) != tuple or len(argumento) != 2 or type(argumento[0]) != int or\
     type(argumento[1]) != int or argumento[0] < 0 or argumento[1] < 0: 
        return False

    return True

#Teste
def posicoes_iguais(posicao1:tuple, posicao2:tuple) -> bool:
    '''
    posicao × posicao → booleano

    Esta função retorna um boolean, True se os argumentos forem posições e forem \
    iguais, False caso contrário.
    '''

    return posicao1 == posicao2

#Transformador
def posicao_para_str(posicao:tuple) -> str:
    '''
    posicao → str

    Esta função retorna a cadeia de caracteres "(x,y)" que representa o seu argumento, \
    sendo os valores x e y as cordenadas da posicao
    '''
    return str(posicao)

#Alto Nivel
def obter_posicoes_adjacentes(posicao:tuple) -> tuple:
    '''
    posicao → tuplo

    Esta função recebe uma posição e devolve um tuplo com as posições adjacentes \
    a essa posição, começando pela posição acima e seguindo no sentido horário
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
    tuplo → tuplo

    Esta função recebe um tuplo contendo posições e devolve um tuplo contendo essas\
    mesmas posições ordenadas pela ordem de leitura do prado 
    '''

    #inverter o tuplo posicao e ordenar dessa forma.. 1º a linha; 2º a coluna
    posicoes_ordenadas = tuple(sorted(posicoes, key=lambda x: (obter_pos_y(x), obter_pos_x(x))))

    return posicoes_ordenadas

#-------------------#   

# -- TAD animal -- #

#Construtores
def cria_animal(especie:str, f_reproducao:int, f_alimentacao:int) -> dict:
    '''
    str × int × int → animal

    Esta função recebe uma cadeia de caracteres não vazia correspondente à espécie \
    do animal e dois valores inteiros correspondentes à frequência de reprodução \
    (maior do que 0) e à frequência de alimentação (maior ou igual a 0); e devolve \
    o animal. A função verifica a validade dos seus argumentos, gerando um ValueError \
    com a mensagem "cria_animal: argumentos invalidos" caso os seus argumentos não sejam válidos.
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
    '''
    animal → animal

    Esta função recebe um animal e devolve uma nova cópia do animal.
    '''

    return deep_copy(animal)
    
#Seletores
def obter_especie(animal):
    '''
    animal → str

    Esta função devolve a cadeia de caracteres correspondente à espécie do animal.
    '''

    return animal["especie"]

def obter_freq_reproducao(animal):
    '''
    animal → int

    Esta função devolve a frequência de reprodução do animal.
    '''

    return animal["f_reproducao"]

def obter_freq_alimentacao(animal):
    '''
    animal → int

    Esta função devolve a frequência de alimentação do animal.
    '''

    return animal["f_alimentacao"]

def obter_idade(animal):
    '''
    animal → int

    Esta função devolve a idade do animal. 
    '''

    return animal["idade"]

def obter_fome(animal):
    '''
    animal → int

    Esta função devolve a fome do animal.
    '''

    return animal["fome"]

#Modificadores
def aumenta_idade(animal):
    '''
    animal → animal

    Esta função modifica destrutivamente o animal incrementando o valor da sua \
    idade em uma unidade, e devolve o próprio animal.
    '''

    animal["idade"] += 1

    return animal

def reset_idade(animal):
    '''
    animal → animal

    Esta função modifica destrutivamente o animal definindo o valor da sua idade \
    igual a 0, e devolve o próprio animal.
    '''

    animal["idade"] = 0

    return animal

def aumenta_fome(animal):
    '''
    animal → animal
    
    Esta função modifica destrutivamente o animal predador incrementando o valor \
    da sua fome em uma unidade, e devolve o próprio animal. Esta operação não modifica os animais presa.
    '''

    if animal["f_alimentacao"] != 0:
        animal["fome"] += 1

    return animal

def reset_fome(animal):
    '''
    animal → animal

    Esta função modifica destrutivamente o animal definindo o valor da sua fome \
    igual a 0, e devolve o próprio animal.
    '''
    
    animal["fome"] = 0

    return animal

#Reconhecedores
def eh_animal(animal):
    '''
    universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD animal e False caso contrário.    
    '''
    
    if type(animal) != dict or len(animal) != 5:
        return False

    if "especie" not in animal or "f_reproducao" not in animal or \
        "f_alimentacao" not in animal or "idade" not in animal or \
        "fome" not in animal:
        return False

    especie = animal["especie"]
    f_reproducao = animal["f_reproducao"]
    f_alimentacao = animal["f_alimentacao"]
    idade = animal["idade"]
    fome = animal["fome"]

    if type(especie) != str or not especie.isalpha() or type(f_reproducao) != int or\
        type(f_alimentacao) != int or f_reproducao <= 0 or f_alimentacao < 0 or\
        type(idade) != int or type(fome) != int or idade < 0 or fome < 0:
        return False

    return True

def eh_predador(animal):
    '''
    universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD animal do tipo predador \
    e False caso contrário
    '''

    return eh_animal(animal) and bool(animal["f_alimentacao"])
    
def eh_presa(animal):
    '''
    universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD animal do tipo presa \
    e False caso contrário.
    '''
    
    return eh_animal(animal) and not bool(animal["f_alimentacao"]) 

#Teste
def animais_iguais(animal1, animal2):
    '''
    animal × animal → booleano

    Esta função devolve True apenas se os argumentos são animais e são iguais.
    '''

    return eh_animal(animal1) and animal1 == animal2 

#Transformadores
def animal_para_char(animal):
    '''
    animal → str

    Esta função devolve a cadeia de caracteres dum único elemento correspondente \
    ao primeiro carácter da espécie do animal passada por argumento, em maiúscula \
    para animais predadores e em minúscula para animais presa.
    '''
    
    caracter = obter_especie(animal)[0]

    return caracter.upper() if eh_predador(animal) else caracter.lower()

def animal_para_str(animal):
    '''
    animal → str

    Esta função devolve a cadeia de caracteres que representa o animal.
    '''

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
    '''
    animal → booleano

    Esta função devolve True caso o animal tenha atingido a idade de reprodução \
    e False caso contrário.
    '''

    return True if obter_idade(animal) >= obter_freq_reproducao(animal) else False

def eh_animal_faminto(animal):
    '''
    animal → booleano

    Esta função devolve True caso o animal tenha atingindo um valor de fome igual \
    ou superior à sua frequência de alimentação e False caso contrário. \
    As presas devolvem sempre False.
    '''

    return True if eh_predador(animal) and obter_fome(animal) >= obter_freq_alimentacao(animal) else False

def reproduz_animal(animal):
    '''
    animal → animal

    Esta função recebe um animal e devolve um novo animal da mesma espécie com \
    idade e fome igual a 0, modificando destrutivamente o animal passado como \
    argumento alterando a sua idade para 0.
    '''
    
    #modificar o pai
    reset_idade(animal)

    filho = cria_copia_animal(animal)
    reset_fome(filho)

    return filho

#------------------#


# -- TAD prado -- #
#Construtores
def cria_prado(posicao_infd:tuple, posicoes_rochedos:tuple, animais:tuple, posicoes_animais:tuple) -> dict:
    '''
    posicao × tuplo × tuplo × tuplo → prado

    Esta função recebe uma posição correspondente à montanha do canto inferior \
    direito do prado, um tuplo de 0 ou mais posiçõeses correspondentes aos rochedos, \
    um tuplo de 1 ou mais animais, e um tuplo da mesma dimensão do tuplo dos animais \
    com as posições correspondentes ocupadas pelos animais; e devolve o prado que \
    representa internamente o mapa e os animais presentes. O construtor verifica \
    a validade dos seus argumentos, gerando um ValueError com a mensagem \
    'cria prado: argumentos invalidos' caso os seus argumentos não sejam válidos.
    '''

    if not eh_posicao(posicao_infd) or type(posicoes_rochedos) != tuple:
        raise ValueError("cria_prado: argumentos invalidos")

    for posicao_rochedo in posicoes_rochedos:
        if not eh_posicao(posicao_rochedo) or \
            not(obter_pos_x(posicao_infd) > obter_pos_x(posicao_rochedo) > 0) or\
            not(obter_pos_y(posicao_infd) > obter_pos_y(posicao_rochedo) > 0):

            raise ValueError("cria_prado: argumentos invalidos")

    if type(animais) != tuple or len(animais) == 0 or type(posicoes_animais) != tuple or\
        len(posicoes_animais) != len(animais):
        raise ValueError("cria_prado: argumentos invalidos")

    for posicao_animal in posicoes_animais:
        if not eh_posicao(posicao_animal) or\
            not(obter_pos_x(posicao_infd) > obter_pos_x(posicao_animal) > 0) or\
            not(obter_pos_y(posicao_infd) > obter_pos_y(posicao_animal) > 0) or\
            posicao_animal in posicoes_rochedos:

            raise ValueError("cria_prado: argumentos invalidos")

    prado = {
        "tamanho": (obter_pos_x(posicao_infd)+1, obter_pos_y(posicao_infd)+1),
        "posicoes_rochedos": posicoes_rochedos,
        "animais": list(animais),
        "posicoes_animais": list(posicoes_animais)
    }

    return prado

def cria_copia_prado(prado: dict) -> dict:
    '''
    prado → prado

    Esta função recebe um prado e devolve uma nova cópia do prado.
    '''

    return deep_copy(prado)

#Seletores
def obter_tamanho_x(prado:dict) -> int:
    '''
    prado → int

    Esta função devolve o valor inteiro que corresponde à dimensão x do prado.
    '''
    
    return prado["tamanho"][0]

def obter_tamanho_y(prado:dict) -> int:
    '''
    prado → int

    Esta função devolve o valor inteiro que corresponde à dimensão y do prado.
    '''

    return prado["tamanho"][1]

def obter_numero_predadores(prado:dict) -> int:
    '''
    prado → int

    Esta função devolve o número de animais predadores no prado.
    '''

    animais = prado["animais"]

    return len(list(filter(lambda x: eh_predador(x), animais)))

def obter_numero_presas(prado:dict) -> int:
    '''
    prado → int

    Esta função devolve o número de animais presas no prado.
    '''

    animais = prado["animais"]

    return len(list(filter(lambda x: eh_presa(x), animais)))

def obter_posicao_animais(prado:dict) -> tuple:
    '''
    prado → tuplo

    Esta função devolve um tuplo contendo as posições do prado ocupadas por animais, \
    ordenadas em ordem de leitura do prado.
    '''
    
    posicoes_animais = prado["posicoes_animais"]

    return ordenar_posicoes(posicoes_animais)

def obter_animal(prado:dict, posicao:tuple) -> dict:
    '''
    prado × posicao → animal

    Esta função devolve o animal do prado que se encontra na posição passada como \
    argumento.
    '''

    animais = prado["animais"]  
    posicoes_animais = prado["posicoes_animais"]

    for i, pos in enumerate(posicoes_animais):
        if posicoes_iguais(pos, posicao):
            #print(animais[i])  
            return animais[i]

#Modificadores
def eliminar_animal(prado:dict, posicao:tuple) -> dict:
    '''
    prado × posicao → prado

    Esta função modifica destrutivamente o prado eliminando o animal da posição \
    passada como argumento deixando-a livre; devolve o próprio prado.
    '''
    
    animais = prado["animais"]
    posicoes_animais = prado["posicoes_animais"]

    #get posicao
    for i, pos in enumerate(posicoes_animais):
        if posicoes_iguais(pos, posicao):
            del posicoes_animais[i]
            del animais[i]

    return prado

def mover_animal(prado:dict, posicao:tuple, nova_posicao:tuple) -> dict:
    '''
    prado × posicao × posicao → prado

    Esta função modifica destrutivamente o prado movimentando o animal da posição \
    "posicao" para a nova posição "nova_posicao", deixando livre a posição onde se \
    encontrava; devolve o próprio prado.
    '''

    posicoes_animais = prado["posicoes_animais"]

    for i, pos in enumerate(posicoes_animais):
        if posicoes_iguais(pos, posicao):
            posicoes_animais[i] = nova_posicao

    return prado

def inserir_animal(prado:dict, animal:dict, posicao:tuple) -> dict:
    '''
    prado × animal × posicao → prado

    Esta função modifica destrutivamente o prado acrescentando na posição passada \
    como argumento o animal passado com argumento; devolve o próprio prado.
    '''

    prado["animais"].append(animal)
    prado["posicoes_animais"].append(posicao)

    return prado



#Reconhecedores
def eh_prado(prado) -> bool:
    '''
    universal → booleano

    Esta função devolve True caso o seu argumento seja um TAD prado e False caso \
    contrário.
    '''

    if type(prado) != dict or len(prado) != 4:
        return False
    
    #check keys
    if "tamanho" not in prado or "posicoes_rochedos" not in prado \
        or "animais" not in prado or "posicoes_animais" not in prado or \
        type(prado["tamanho"]) != tuple or len(prado["tamanho"]) != 2 or \
        type(prado["posicoes_rochedos"]) != tuple or \
        type(prado["animais"]) != list or len(prado["animais"]) == 0 or \
        type(prado["posicoes_animais"]) != list or \
        len(prado["posicoes_animais"]) != len(prado["animais"]):

        return False

    for ani in prado["animais"]:
        if not eh_animal(ani):
            return False

    for pos in prado["posicoes_animais"]:
        if not eh_posicao(pos):
            return False

    return True

def eh_posicao_animal(prado:dict, posicao:tuple) -> bool:
    '''
    prado × posicao → booleano

    Esta função devolve True apenas no caso da posição estar ocupada por um animal.
    '''
    
    for pos in obter_posicao_animais(prado):
        if posicoes_iguais(pos, posicao):
            return True
    
    return False

def eh_posicao_obstaculo(prado:dict, posicao:tuple) -> bool:
    '''
    prado × posicao → booleano

    Esta função devolve True apenas no caso da posição corresponder a uma montanha \
    ou rochedo.
    '''
    
    if obter_pos_x(posicao) == 0 or obter_pos_y(posicao) == 0 or \
        obter_pos_x(posicao) == obter_tamanho_x(prado)-1 or \
        obter_pos_y(posicao) == obter_tamanho_y(prado)-1:
        return True

    for pos in prado["posicoes_rochedos"]:
        if posicoes_iguais(pos, posicao):
            return True

    return False

def eh_posicao_livre(prado:dict, posicao:tuple) -> bool:
    '''
    prado × posicao → booleano

    Esta função devolve True apenas no caso da posição corresponder a um espaço \
    livre (sem animais, nem obstáculos).    
    '''
    
    if not eh_posicao_animal(prado, posicao) and not eh_posicao_obstaculo(prado, posicao):
        return True
    
    return False

#Teste
def prados_iguais(prado1:dict, prado2:dict) -> bool:
    '''
    prado × prado → booleano

    Esta função devolve True apenas se os argumentos forem prados e forem iguais.
    '''
    
    return eh_prado(prado1) and prado1 == prado2

#Transformador
def prado_para_str(prado:dict) -> str:
    '''
    prado → str

    Esta função devolve uma cadeia de caracteres que representa o prado.
    '''

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


#Alto nivel
def obter_valor_numerico(prado:dict, posicao:tuple) -> int:
    '''
    prado × posicao → int

    Esta função devolve o valor numérico da posição passada como argumento correspondente à ordem de leitura no prado.
    '''
    
    tamanho_x = obter_tamanho_x(prado)

    linha_y = obter_pos_y(posicao)
    coluna_x = obter_pos_x(posicao)

    #atraves da formula
    valor_numerico = (tamanho_x * linha_y) + coluna_x

    return valor_numerico
     
def obter_movimento(prado:dict, posicao:tuple) -> tuple:
    '''
    prado × posicao → posicao

    Esta função devolve a posição seguinte do animal (na posição passada como argumento) dentro do prado de acordo com as regras de movimento dos animais no prado.
    '''

    valor_numerico = obter_valor_numerico(prado, posicao)

    posicoes_adjacentes = obter_posicoes_adjacentes(posicao)

    animal = obter_animal(prado, posicao)

    #se for predador
    if eh_predador(animal):
        
        #posições disponiveis
        posicoes_disponiveis = [posicao_t for posicao_t in posicoes_adjacentes \
        if eh_posicao_livre(prado, posicao_t) or (eh_posicao_animal(prado, posicao_t)\
            and eh_presa(obter_animal(prado, posicao_t)))]

        #se nao houver posicoes disponiveis
        if len(posicoes_disponiveis)  == 0:
            return posicao

        #posicoes com presas
        posicoes_presas = [posicao_t for posicao_t in posicoes_disponiveis \
            if eh_posicao_animal(prado, posicao_t) and eh_presa(obter_animal(prado, posicao_t))]

        #se nao houver presas 
        if len(posicoes_presas) == 0:
            return posicoes_disponiveis[valor_numerico % len(posicoes_disponiveis)]

        '''#Se houver só 1 presa
        if len(posicoes_presas) == 1:
            return posicoes_presas[0]'''
        
        #se houver presas
        return posicoes_presas[valor_numerico % len(posicoes_presas)]

    #se for presa
    else:
        #posições disponiveis
        posicoes_disponiveis = [posicao_t for posicao_t in posicoes_adjacentes \
            if eh_posicao_livre(prado, posicao_t)]

        #se nao houver posicoes livre
        if len(posicoes_disponiveis) == 0:
            return posicao  
        
        #caso contrario escolher 1 delas
        return posicoes_disponiveis[valor_numerico % len(posicoes_disponiveis)]

#-----------------#

#Auxiliar
def geracao(prado:dict) -> dict:
    '''
    prado → prado

    Esta é a função auxiliar que modifica o prado fornecido como argumento de \
    acordo com a evolução correspondente a uma geração completa, e devolve o próprio\
    prado. Isto é, seguindo a ordem de leitura do prado, cada animal (vivo) realiza\
    o seu turno de ação de acordo com as regras descritas.
    '''

    def posicao_in(posicao, lista):
        for pos in lista:
            if posicoes_iguais(pos, posicao):
                return True
        
        return False


    posicoes_animais = obter_posicao_animais(prado)
    animais_mortos = []

    for posicao in posicoes_animais:
        #print(animais_mortos)

        #se o animal tiver sido morto
        if posicao_in(posicao, animais_mortos):
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

#Principal
def simula_ecossistema(file_name: str, geracoes: int, verboso: bool):
    '''
    str × int × booleano → tuplo

    Esta é a função principal que permite simular o ecossistema de um prado.
    A função recebe uma cadeia de caracteres "file_name" correspondente ao nome \
    do ficheiro de configuração, um valor inteiro "geracoes" correspondente ao \
    número de gerações a simular e um valor booleano "verboso" correspondente ao \
    modo (False - quiet e True - verboso),; devolvendo um tuplo de dois elementos\
    correspondentes ao número de predadores e presas no prado no fim da simulação.\
    No modo quiet mostra-se pela saída standard o prado, o número de animais e o \
    número de geração no início da simulação e após a última geração. 
    No modo verboso, após cada geração, mostra-se também o prado, o número de \
    animais e o número de geração, apenas se o número de animais predadores ou \
    presas se tiver alterado.
    '''
    
    with open(file_name, "r") as f:
        linhas = f.readlines()

    tuplo_infd = eval(linhas[0])
    tuplo_rochedos = eval(linhas[1])


    inf_d = cria_posicao(tuplo_infd[0], tuplo_infd[1])
    rochedos = tuple(cria_posicao(pos[0], pos[1]) for pos in tuplo_rochedos)

    #animais
    animais = ()
    posicoes_animais = ()

    for linha in linhas[2:]:
        animal_e_posicao = eval(linha)

        animal = animal_e_posicao[:-1]
        posicao_animal = animal_e_posicao[-1]

        animais += (cria_animal(animal[0], animal[1], animal[2]),)
        posicoes_animais += (cria_posicao(posicao_animal[0], posicao_animal[1]),)

    prado = cria_prado(inf_d, rochedos, animais, posicoes_animais)

    for gen in range(0,geracoes+1):

        gen_presas = obter_numero_presas(prado)
        gen_predadores = obter_numero_predadores(prado)

        if (verboso and (gen == 0 or last_gen_predadores != gen_predadores or \
            last_gen_presas != gen_presas)) or \
            (not verboso and (gen == 0 or gen == geracoes)):

            print(f"Predadores: {gen_predadores} vs Presas: {gen_presas} (Gen. {gen})")
            print(prado_para_str(prado))
        
        last_gen_presas = gen_presas
        last_gen_predadores = gen_predadores

        if gen != geracoes:
            prado = geracao(prado)

    return gen_predadores, gen_presas

