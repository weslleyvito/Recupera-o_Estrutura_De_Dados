class Pilhas_codificadas:
    def __init__(self):
        # de praste aqui está a pilha que iremos receber as strings codificada
        self.__pilha = []

    def decifrar_string(self, elemento):
        # Aqui usamor um for para percorrer todo o elemento adicionado ana entrada
        for i in range(len(elemento)):
            # Se o meu elemento tiver o i igual a ']'
            if elemento[i] == "]":
                # ele vai retorna a saida vaazio
                saida = ''
                # Agora dou um trigger num while
                while self.__pilha:
                    # agr com a variavel incicio atribuo o pop a ela
                    inicio = self.__pilha.pop()
                    # Caso meu inicio seja igual a '[' eu paro meu while com um break
                    if inicio == "[":
                        break
                    # E agora digo que a forma da minha saida dizendo que ela recebe inicio + saida
                    saida = inicio + saida
                # Declaro minha variavel quantidade sem nada
                quantidade = ''
                # Um trigger no while pra pecorrer a minha pilha e seu ultimo elemento e certifico se ele é um digito
                while self.__pilha and self.__pilha[-1].isdigit():
                    # Agora declaro a minha quantidade com um pop na lista somado com a quantidade
                    quantidade = self.__pilha.pop() + quantidade
                #Agora adiciona a minha pilha a quantidade vezes a minha saida 
                self.__pilha.append(int(quantidade) * saida)
            # agora se o item não diferente do [], ele será adicionado a pilha
            else:
                self.__pilha.append(elemento[i])
        return print(''.join(self.__pilha))