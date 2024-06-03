import csv
import json
import pandas as pd

def levenshtein_distance(s1, s2):

    matrix = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        matrix[i][0] = i
    for j in range(len(s2) + 1):
        matrix[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            is_igual = s1[i - 1] == s2[j - 1]
            custo = 0 if is_igual else 1

            remocao = matrix[i - 1][j] + 1
            insercao = matrix[i][j - 1] + 1
            substituicao = matrix[i - 1][j - 1] + custo

            matrix[i][j] = min(remocao, insercao, substituicao)

    return matrix[len(s1)][len(s2)]

with open('palavroes.txt', 'r',) as f:
    s1 = f.readlines()


#s1 = ["Porra", "Foda", "Caralho", "Cuzão", "Buceta", "Puta", "Foda-se", "Merda", "Cacete", "Pau", "Arrombado"]

list_msgs_tweets = []

list_msgs_tratadas = []

#list_msgs_tratadas.append("mensagem_tratada")

with open('sentimentos.csv', 'r',) as f:
    reader = csv.reader(f, delimiter=";", quotechar='"')

    next(reader, None)

    for x in reader:
        list_msgs_tweets.append(x[1])

for x in list_msgs_tweets:
    print(f"{x}\n")
    lista_palavras = x.split()
    indice = 0
    for i in lista_palavras:
        for y in s1:
            res = levenshtein_distance(i.lower(), y.lower())
            if res > 2 or len(i) <= 3:
                continue

            lista_palavras[indice] = "BADWORD"
        indice+=1

    frase = ""

    for p in lista_palavras:
        frase += f'{p} '

    print(frase)

    list_msgs_tratadas.append(frase)

    print('\n\n=====================')

print(f"lenght antigo: {len(list_msgs_tweets)}")
print(f"lenght novo: {len(list_msgs_tratadas)}")


csv_atual = pd.read_csv("sentimentos.csv", quotechar='"', sep=";")
csv_atual["mensagem_tratada"] = list_msgs_tratadas
csv_atual.to_csv("tweets_classificados.csv", sep=";", quotechar='"', quoting=csv.QUOTE_ALL, index=False)