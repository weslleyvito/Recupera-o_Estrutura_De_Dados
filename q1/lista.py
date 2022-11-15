class Lista:
    def __init__(self):
        # aqui criamos nossa lista como um tubo de ensaio para os teste da entrada de input, assim poderemos receber um item e returnar True ou Fakse
        self.__items = []
    

    # aqui foi criado uma função para receber um item e adicionar nossa lista passando por uma verificação se ele é valido para ser adicionado ou não e onde vai ocorrer o retorno de false ou true
    def adicionar(self, item):
        #Usaremos um for para pecorrer o item usado na entrada e verificar:
        for i in item:
            # Caso o item da entrada for diferente das condições <(,[,{> e se os items forem maior que zero
            if i != '(' and item != '[' and i != '{' and len(self.__items) > 0:
                # ele cria uma variavel que reecebe a lista com -1 o fazendo ser os ultimos da lista de items
                ultimo = self.__items[-1]
                # Usamos a variavel ultimo para verificar a parte do item de entrada se é valida na sua ultima posição
                if (i == ")" and ultimo == "(") or (i == "]" and ultimo == "[") or (i == "}" and ultimo == "{"):
                    # casp tudo ocorra bem ele vai descartar os itens como uma forma de validação atraves do pop
                    self.__items.pop()
                else:
                    # 
                    return print('esse item é {0}'.format(False))
            else:
                # Se a junção do primeiro com o segundo não for correta ela adiciona o primeiro como diferença de erro, assim validando qual é o certo(retornando True) ou errado(retornando False)

                self.__items.append(i)

        # aqui nesse if é onde vamos fazer a validação com os paramentros acima se a lista tiver vazia então os itens inseridos foram corretos, caso não eles seram adicionados a lista
        if len(self.__items) == 0:
            return print('Esse item é {0}'.format(True))
        else:
            return print('Esse item é {0}'.format(False))
        
    def __repr__(self):
        return  str(self.__items)