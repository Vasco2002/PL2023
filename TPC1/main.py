import csv

# Função que calcula a distribuição da doença por sexo
def sexo(lista, counter):
    d = {('M', 0): 0, ('M', 1): 0, ('F', 0): 0, ('F', 1): 0}
    for linha in lista:
        d[(linha[1], int(linha[5]))] += 1;
    print("--------------------Distribuição da doença por sexo-------------------------")
    print("%Homens sem doença: " + str(round((d[('M', 0)] / counter) * 100)) + "%")
    print("%Homens com doença: " + str(round((d[('M', 1)] / counter) * 100)) + "%")
    print("%Mulheres sem doença: " + str(round((d[('F', 0)] / counter) * 100)) + "%")
    print("%Mulheres com doença: " + str(round((d[('F', 1)] / counter) * 100)) + "%")


# Função que calcula a distribuição da doença por escalões etários
def idade(lista, counter):
    d = {}
    lista.sort()
    i = int(lista[0][0])
    lista.reverse()
    maior = int(lista[0][0])
    while i <= maior:
        d.update({(i, i + 4, 0): 0})
        d.update({(i, i + 4, 1): 0})
        i += 5

    for linha in lista:
        for faixa in d.keys():
            if faixa[0] <= int(linha[0]) <= faixa[1]:
                d[(faixa[0], faixa[1], int(linha[5]))] += 1;
                break;
    print("--------------------Distribuição da doença por escalões etários-------------------------")
    for faixa in d.keys():
        if faixa[2] == 0:
            print("%[" + str(faixa[0]) + "-" + str(faixa[1]) + "] sem doença: " + str(round((d[faixa] / counter) * 100)) + "%")
        else:
            print("%[" + str(faixa[0]) + "-" + str(faixa[1]) + "] com doença: " + str(round((d[faixa] / counter) * 100)) + "%")

#Função que calcula a distribuição da doença por níveis de colesterol
def colesterol(lista, counter):
    d = {}
    # Ordenando a lista pelos niveis de colestrol dá-me como o último resultado 85 e como penúltimo 603(que é o maior nivel de colestrol)
    # não sei porquê mas só o 85 está errado
    lista.sort(key=lambda x: x[3])
    i = int(lista[0][3])
    lista.reverse()
    maior = int(lista[1][3])
    while i <= maior:
        d.update({(i, i + 9, 0): 0})
        d.update({(i, i + 9, 1): 0})
        i += 10

    for linha in lista:
        for faixa in d.keys():
            if faixa[0] <= int(linha[3]) <= faixa[1]:
                d[(faixa[0], faixa[1], int(linha[5]))] += 1;
                break;
    print("--------------------Distribuição da doença por níveis de colesterol-------------------------")
    for faixa in d.keys():
        if faixa[2] == 0:
            print("%[" + str(faixa[0]) + "-" + str(faixa[1]) + "] sem doença: " + str((d[faixa] / counter) * 100) + "%")
        else:
            print("%[" + str(faixa[0]) + "-" + str(faixa[1]) + "] com doença: " + str((d[faixa] / counter) * 100) + "%")



def main():
    # Lista que guarda os dados de myheart.csv
    lista = []
    # Conta o número de linhas no ficheiro myheart.csv
    counter = 0;
    # Função que lê a informação do ficheiro para um modelo, previamente pensado em memória (sendo o modelo "lista")
    print("--------------------Informação do Ficheiro-------------------------")
    with open('myheart.csv', mode='r') as file:
        ficheiro = csv.reader(file)
        next(ficheiro)
        for linha in ficheiro:
            counter += 1;
            lista.append(linha)
            print(linha)

        sexo(lista, counter)

        idade(lista, counter)

        colesterol(lista, counter)



if __name__ == '__main__':
    main()
