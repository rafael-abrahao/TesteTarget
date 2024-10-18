def main():
    texto = input("Digite um string: ")
    count_a = texto.lower().count('a')

    resposta = 'Esse texto'
    if count_a == 0:
        resposta += ' NAO contem a letra a'
    else:
        resposta += f' contém {count_a} a'
        if count_a > 1:
            resposta += 's'
        
        
    print(resposta)
    
if __name__ == "__main__":
    main()