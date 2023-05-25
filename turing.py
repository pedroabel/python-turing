class TuringMachine:
    def __init__(self, fita, transicoes):
        self.fita = fita
        self.posicao = 0
        self.estado_atual = 'q0'
        self.transicoes = transicoes

    def movimento(self, direcao):
        if direcao == 'D':
            self.posicao += 1
        elif direcao == 'E':
            self.posicao -= 1

    def run(self):
        while True:
            if self.estado_atual == 'qf':
                print("Aceito")
                break

            if self.posicao >= len(self.fita) or self.posicao < 0:
                print(
                    "Ação: {} Rejeitado - Ação inválida: transição não definida.".format(self.estado_atual))
                break

            valor = self.fita[self.posicao]

            if (self.estado_atual, valor) not in self.transicoes:
                print(
                    "Ação: {} Rejeitado - Ação inválida: transição não definida.".format(self.estado_atual))
                break

            novo_estado, novo_valor, direcao = self.transicoes[(
                self.estado_atual, valor)]

            self.fita[self.posicao] = novo_valor
            self.estado_atual = novo_estado
            self.movimento(direcao)


# Cadastro da fita
fita_input = input(
    "Digite os valores da fita separados por espaço (máximo de 100): ")

fita_input = fita_input.split()[:100]
fita = fita_input + ['_'] * (100 - len(fita_input))
fita_inicial = fita.copy()

# Definição das quintuplas de transição
transicoes = {
    # (estado atual, simbolo lido) : (Novo estado, simbolo escrito, movimento)
    #  ('q0', '0'): ('q1', '1', 'D'),
    #  ('q0', '1'): ('q1', '0', 'D'),
    #  ('q1', '0'): ('q2', '1', 'D'),
    #  ('q1', '1'): ('q2', '0', 'D'),
    #  ('q2', '0'): ('q3', '1', 'D'),
    #  ('q2', '1'): ('q3', '0', 'D'),
    #  ('q3', '0'): ('q4', '1', 'D'),
    #  ('q3', '1'): ('q4', '0', 'D'),
    #  ('q4', '0'): ('q5', '1', 'D'),
    #  ('q4', '1'): ('q5', '0', 'D'),
    #  ('q5', '0'): ('qf', '1', 'D'),
    #  ('q5', '1'): ('qf', '0', 'D'),

    # VALOR PADRAO DA FITA - 1 2 3 4 5 6 7 8 9
    # Primeiro teste - inverter todos os numeros para letras
    ('q0', '1'): ('q1', 'A', 'D'),
    ('q1', '2'): ('q2', 'B', 'D'),
    ('q2', '3'): ('q3', 'C', 'D'),
    ('q3', '4'): ('q4', 'D', 'D'),
    ('q4', '5'): ('q5', 'E', 'D'),
    ('q5', '6'): ('q6', 'F', 'D'),
    ('q6', '7'): ('q7', 'G', 'D'),
    ('q7', '8'): ('q8', 'H', 'D'),
    ('q8', '9'): ('q10', '1', 'E'),
    # Segundo teste - pegar as letras e inverter para nuemeros
    # ('q10', 'H'): ('q11', '2', 'E'),
    # ('q11', 'G'): ('q12', '3', 'E'),
    # ('q12', 'F'): ('q13', '4', 'E'),
    # ('q13', 'E'): ('q14', '5', 'E'),
    # ('q14', 'D'): ('q15', '6', 'E'),
    # ('q15', 'C'): ('q16', '7', 'E'),
    # ('q16', 'B'): ('q17', '8', 'E'),
    # ('q17', 'A'): ('q18', '9', 'E'),

    # Modelo de rejeição - Fora da fita
    # ('q18', '9'): ('qf', '9', 'E'),

}

tm = TuringMachine(fita, transicoes)
tm.run()

print("\nFita inicial:", ' '.join(fita_inicial[:len(fita_input)]).strip())
print("Fita alterada:", ' '.join(tm.fita[:len(fita_input)]).strip())
