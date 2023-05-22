class TuringMachine:
    def __init__(self, tape, transitions):
        self.tape = tape
        self.head_position = 0
        self.current_state = 'q0'
        self.transitions = transitions

    def move_head(self, direction):
        if direction == 'D':
            self.head_position += 1
        elif direction == 'E':
            self.head_position -= 1

    def run(self):
        while True:
            if self.current_state == 'qf':
                print("Aceito")
                break

            if self.head_position >= len(self.tape) or self.head_position < 0:
                print(
                    "Ação: {} Rejeitado - Ação inválida: transição não definida.".format(self.current_state))
                break

            symbol = self.tape[self.head_position]

            if (self.current_state, symbol) not in self.transitions:
                print(
                    "Ação: {} Rejeitado - Ação inválida: transição não definida.".format(self.current_state))
                break

            new_state, new_symbol, direction = self.transitions[(
                self.current_state, symbol)]

            self.tape[self.head_position] = new_symbol
            self.current_state = new_state
            self.move_head(direction)


# Cadastro da fita
tape_input = input(
    "Digite os valores da fita separados por espaço (máximo de 100): ")
tape_input = tape_input.split()[:100]
tape = tape_input + ['_'] * (100 - len(tape_input))
initial_tape = tape.copy()

# Definição das quintuplas de transição
transitions = {
    # (estado atual, simbolo lido) : (Novo estado, simbolo escrito, movimento)

    # VALOR PADRAO DA FITA - 1 2 3 4 5 6 7 8 9
    # Primeiro teste - inverter todos os numeros para letras
    # Resultado esperado - A B C D E F G H 1
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
    # Resultado esperado - 9 8 7 6 5 4 3 2 1
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

tm = TuringMachine(tape, transitions)
tm.run()

print("\nFita inicial:", ' '.join(initial_tape[:len(tape_input)]).strip())
print("Fita alterada:", ' '.join(tm.tape[:len(tape_input)]).strip())
