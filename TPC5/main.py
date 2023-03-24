import re
import sys
import math


def montante(moeda):
    valor = 0
    valores = {"50c": 0.5, "20c": 0.2, "10c": 0.1, "5c": 0.05, "1e": 1.0, "2e": 2.0}
    moeda = moeda.strip(";,.\n")
    if valores.get(moeda):
        valor = valores.get(moeda)
    return valor


def saldo_format(saldo):
    ret = ""
    frac, whole = math.modf(saldo)
    if whole > 0:
        ret = f"{int(whole)}e{int(frac * 100)}c"
    else:
        ret = f"{frac}c"

    return ret


def custo_chamada(indicador):
    valor = 0

    if indicador == "601" or indicador == "641":
        valor = -1  # chamada bloqueada
    elif indicador[:2] == "00":
        valor = 1.5
    elif indicador[0] == "2":
        valor = 0.25
    elif indicador == "800":
        valor = 0
    elif indicador == "808":
        valor = 0.1
    else:
        valor = -2

    return valor


class Telefone:
    numero = "000000000"
    custo = 0
    moedas = []
    saldo = 0
    levantado = False

    def levantar(self):
        self.levantado = True
        input_moedas = input("Introduza moedas.\n").strip().split(" ")
        if input_moedas[0] == "MOEDA":
            for moeda in input_moedas[1:len(input_moedas)]:
                self.moedas.append(moeda)
            self.calc_saldo()

    def calc_saldo(self):
        moedas_invalidas = []
        for moeda in self.moedas:
            if montante(moeda) == 0:
                moedas_invalidas.append(moeda)
            else:
                self.saldo += montante(moeda)

        if len(moedas_invalidas) > 0:
            print(f"{moedas_invalidas} - moedas inválida; saldo = {saldo_format(self.saldo)}")
        else:
            print(f"saldo = {saldo_format(self.saldo)}")

    def pousar(self):
        troco = self.saldo - self.custo
        print(f"troco={saldo_format(troco)}; Volte sempre!")
        self.levantado = False
        self.moedas = []
        self.saldo = 0
        self.custo = 0

    def insere_moedas(self, input_moedas):
        for moeda in input_moedas[1:len(input_moedas)]:
            self.moedas.append(moeda)
        self.calc_saldo()

    def telefonar(self, numero):
        self.custo = custo_chamada(numero[:3])
        if self.custo == -1:
            print("Esse número não é permitido neste telefone. Queira discar novo número!")
        elif self.custo == -2:
            print("Esse número é inválido!")
        else:
            troco = self.saldo - self.custo
            if troco < 0:
                print(f"Saldo insuficiente. Insira {saldo_format(abs(troco))}")
            else:
                print(f"saldo = {saldo_format(self.saldo)}")


def main():
    t = Telefone()

    for line in sys.stdin:
        tokens = line.strip().split(" ")
        if tokens[0] == "LEVANTAR":
            t.levantar()
        else:
            if t.levantado:
                if tokens[0] == "MOEDA":
                    t.insere_moedas(tokens[1:len(tokens)])
                elif tokens[0].split("=")[0] == "T":
                    t.telefonar(tokens[0].split("=")[1].strip())
                elif tokens[0] == "POUSAR":
                    t.pousar()


if __name__ == "__main__":
    main()
