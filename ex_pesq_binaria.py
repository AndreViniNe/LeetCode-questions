def pesquisa_binaria(lista_ordenada, item):
    baixo = 0  #primeiro item da lista
    alto = len(lista_ordenada) - 1  #ultimo item da lista

    #cada tentativa é testada para o elemento central
    while baixo <= alto:
        meio = (baixo + alto)//2  #será arredondado para baixo pelo Python se a soma não for par
        chute = lista_ordenada[meio]

        if chute == item: #se o chute for igual ao valor procurado, retorna a posição dele
            return f"Posição: {meio}"
        if chute > item: #se o chute for maior que o valor procurado, a posição do alto vira o meio
            alto = meio - 1
        else:   #se o chute for menor, a posição de baixo vira o meio
            baixo = meio + 1
    return None
    
if __name__ == "__main__":
    lista = [0,2,4,6,8,10]
    print(pesquisa_binaria(lista, 6))
    print(pesquisa_binaria(lista, 5))
