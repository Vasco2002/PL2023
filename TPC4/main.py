import re
import json

keys = ["Número", "Nome", "Curso", "Notas", "Notas_"]

def csv_to_list(line, func):
    aluno_list = re.split(r',', line, maxsplit=3)

    aluno_dict = {}

    for i in range(len(aluno_list)):
        aluno_dict[keys[i]] = aluno_list[i]

    if len(aluno_list) == 4:
        aluno_dict['Notas'] = str_to_list(aluno_list[3])

    if func:
        if func == 'sum':
            aluno_dict['Notas_' + func] = soma(aluno_list[3])
            del aluno_dict['Notas']

        if func == 'media':
            aluno_dict['Notas_' + func] = media(aluno_list[3])
            del aluno_dict['Notas']

    return aluno_dict


def media(aluno_list):
    num_list = str_to_list(aluno_list)

    media_notas = sum(num_list) / len(num_list)

    return media_notas


def soma(aluno_list):
    num_list = str_to_list(aluno_list)

    soma_notas = sum(num_list)

    return soma_notas


def str_to_list(aluno_list):
    notas_str = aluno_list.split(',')
    return [int(num_str) for num_str in notas_str if num_str]


def check_func(first_line):

    x = re.search(r'::(\w+),', first_line)
    if (x):
        func = x.group(1)
    else:
        func = None

    return func

def main():
    lista_alunos = []

    path = "alunos4.csv"

    with open(path) as f:

        first_line = f.readline()
        func = check_func(first_line)

        content = f.read()

        for line in content.splitlines():
            lista_alunos.append(csv_to_list(line, func))


        filename= path.replace(".csv", ".json")
        with open(filename, "w", encoding="utf-8") as jsonfile:
            json.dump(lista_alunos, jsonfile, indent=4, ensure_ascii=False)

main()