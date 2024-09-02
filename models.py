class NumberSet:
    def __init__(self):
        self.numbers = set(range(1, 101))

    def extract_number(self, numero):
        if numero in self.numero:
            self.numbers.remove(numero)
        else:
            raise ValueError("Número inválido o fuera de rango")

    def find_missing_number(self):
        expected_sum = sum(range(1, 101))
        current_sum = sum(self.numbers)
        return expected_sum - current_sum
