import re
import json
from collections import Counter


def freqAno(processos):
    d = {}
    for key, value in processos.items():
        ano = value['data'].split('-')[0]
        if ano in d:
            d[ano] += 1
        else:
            d[ano] = 1
    return d

def freqNome(processos):
    dProprio = {}
    dApelido = {}

    for key, value in processos.items():

        seculo = (int(value['data'].split('-')[0]) - 1) // 100 + 1

        nome = value['nome']
        proprio, *nomes_meio, apelido = re.search(r'^(.*?)\s+(\S+):?\s+((?:\S*\s)*\S*)$', nome).groups()

        if seculo in dProprio:
            dProprio[seculo].update([proprio])
        else:
            dProprio[seculo] = Counter([proprio])

        if seculo in dApelido:
            dApelido[seculo].update([apelido])
        else:
            dApelido[seculo] = Counter([apelido])

    # mostrar as 5 palavras mais comuns em cada categoria para cada século
    for seculo, freqs in dProprio.items():
        print(f'Século {seculo}:')
        for proprio, freq in freqs.most_common(5):
            print(f'\t{proprio}: {freq}')

    for seculo, freqs in dApelido.items():
        print(f'Século {seculo}:')
        for apelido, freq in freqs.most_common(5):
            print(f'\t{apelido}: {freq}')

    return dProprio, dApelido

def main():
    processos = {}
    with open('processos.txt', 'r') as arquivo:
        for linha in arquivo:
            match = re.search(r'^(\d+)::(\d{4}-\d{2}-\d{2})::(.+)::(.+)::(.*)::(.*)$', linha)
            if match:
                num_processo = match.group(1)
                data = match.group(2)
                nome = match.group(3)
                pai = match.group(4)
                mae = match.group(5)
                obs = match.group(6)

                info_processo = {
                    'data': data,
                    'nome': nome,
                    'pai': pai,
                    'mae': mae,
                    'obs': obs
                }
                processos[num_processo] = info_processo

        dAno = freqAno(processos)
        for ano, freq in dAno.items():
            print(f'Ano {ano}: {freq}')

        print("\n---------------------------------\n")

        dProprio, dApelido = freqNome(processos)
        print(dProprio)
        print(dApelido)

if __name__ == '__main__':
    SystemExit(main())
