from textblob import TextBlob
import csv
import json

def analisar_sentimento(texto):
    blob = TextBlob(texto)
    return blob.sentiment.polarity


def read_json(file):
    with open(file) as f:
        return json.load(f)

def main():
    json_file = read_json('tweets.json')

    with open('sentimentos.csv', 'w',) as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['usuario', 'mensagem', 'sentimento'])

    for tweet in json_file:
        usuario = tweet['usuario']
        mensagem = tweet['mensagem']
        sentimento = float(analisar_sentimento(mensagem))
        print(f'Usuário: {usuario}\nMensagem: {mensagem}\nSentimento: {sentimento}\n')

        with open('sentimentos.csv', 'a') as f:
            writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
            writer.writerow([f"{usuario}", f"{mensagem}", f"{sentimento}"])

main()