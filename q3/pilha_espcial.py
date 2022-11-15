class Pilha_Especial:
    def __init__(self):
        # a pilha especial para adiconar os itens
        self.__pilha_Especial = []

    # função que adiona um elemento a pilha
    def push(self, elemento):
        self.__pilha_Especial.append(elemento)

    # Aqui ele mostra o elemento que está no top da pilha
    def top(self):
        print(''.format(self.__pilha_Especial[-1]))

    # Nessa função vamos realizar o retorno do menor elemento da pilha
    def getMin(self):
        # aqui tratamos a verificação se a lista está vazia caso o pedido seja feito antes de adicionarmos algo a lista
        if len(self.__pilha_Especial) == 0:
            return print('A pilha se encontra vazia no momento, realize uma adição a pilha!')
        #Agora realizo a atribuição de variavel chamada menor e digo q ela é igual a o index 0 da lista
        minimo = self.__pilha_Especial[0]
        # agora vamos percorrer a lista e ver quan item é igual ou menor que a variavel minimo usando o for
        for i in self.__pilha_Especial:
            # Verifico se os itens da pilha, na linha abaixo verifico se ele é menor que o primeiro item da lista
            if i < minimo:
                # Caso a condição seja verdadeira declaro q esse item é o menor da lista
                minimo = i
        # logo após o tratamento do dado eu retorno num print o minimo item
        print(minimo)

    # apaga um elemento no topo da lista
    def pop(self):
        self.__pilha_Especial.pop()

    def __str__(self):
        ret = ' '.join(str(element) for element in self.__pilha_Especial)
        return ret