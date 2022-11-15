class Pilha:
    def __init__(self):
        # aqui vai ficar nossos itens colocados na entrada S
        self.__pilha_S = []
        # aqui vai ficar nossos itens colocados na entrada T
        self.__pilha_T = []
        # contagem total de cada backspace usado na entrada S
        self.__total_de_BackSpace_S = 0
        # contagem total de cada backspace usado na entrada T
        self.__total_de_BackSpace_T = 0

    def adicionar(self, pilha_S, pilha_T):
        pilha_S_Reversa = []
        pilha_T_Reversa = []

        # Os for aqui são usados para dividir e armazenar em suas pilhas 
        for entrada in pilha_S:
            self.__pilha_S.append(entrada)

        for entrada in pilha_T:
            self.__pilha_T.append(entrada)

        # Agora dentro da pilha que recebe itens da entrada de variavel S, usando o while para verificar se o tamanho são maior que 0:
        while len(self.__pilha_S) > 0:
            # caso ele for ele dar um trigger num for para dar reverse na pilha do S
            for i in reversed(self.__pilha_S):
                # Dentro desse for ele vai verificar se cada item é #(backspace)
                if i == "#":
                    # primeiro passo é se for backspace ele vai adicionar no toal de backspace do S +1
                    self.__total_de_BackSpace_S += 1
                    # no segundo passo  ele faz a função do backspace, apagando da lista
                    self.__pilha_S.pop()
                # Se o total de backSpace for maior que zero e o i for diferente do #(backspace)
                elif self.__total_de_BackSpace_S > 0 and i != "#":
                    # ele vai dar um trigger num for percorrendo o total de backspace
                    for e in range(self.__total_de_BackSpace_S):
                        self.__pilha_S.pop()
                        # e aqui dentro do for faço uma condição caso o tamanho da minha Pilha S seja 0 eu passo break para quebrar/parar o while
                        if len(self.__pilha_S) == 0:
                            break
                    self.__total_de_BackSpace_S = 0
                # Se meu i não for adcionar na pilha, a entrada vai sofrer um pop
                else:
                    pilha_S_Reversa.append(i)
                    self.__pilha_S.pop()
        # Então aqui reverto para a ordem original os itens e adiciono na minha Pilha S
        for Reverter in reversed(pilha_S_Reversa):
            self.__pilha_S.append(Reverter)


        # Fazendo novamente essa verificação e tratamento do backspace agora com a pilha_T
        while len(self.__pilha_T) > 0:          
            for i in reversed(self.__pilha_T):  
                if i == "#":
                    self.__total_de_BackSpace_T += 1
                    self.__pilha_T.pop()
                elif self.__total_de_BackSpace_T > 0 and i != "#":
                    for _ in range(self.__total_de_BackSpace_T):
                        self.__pilha_T.pop()
                        if len(self.__pilha_T) == 0:
                            break
                    self.__total_de_BackSpace_T = 0
                else:
                     if i != "#" and self.__total_de_BackSpace_T == 0:
                        pilha_T_Reversa.append(i)
                        self.__pilha_T.pop()
        for Reverter in reversed(pilha_T_Reversa):
            self.__pilha_T.append(Reverter)

        # agora que ocorre a magia de comparar se as duas são iguais e retorna false ou true
        if self.__pilha_S == self.__pilha_T:
            print('esse item é {0}'.format(True))
        else:
            print('esse item é {0}'.format(False))

    def __repr__(self):
        return str(self.__pilha_S), str(self.__pilha_T)