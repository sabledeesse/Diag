from collections import defaultdict


class Diag(str):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return '\n'.join([' ' * i + char for i, char in enumerate(self.string)])

    def __add__(self, other):
        return Diag((other[::-1] + self.string[::-1]))

    def __sub__(self, other: "Diag") -> "Diag":
        def _append(char: str) -> bool:
            if counter[char]:
                counter[char] -= 1
                return False
            return True

        counter = defaultdict(int)
        for c in super(Diag, other).__iter__():
            counter[c] += 1
        return Diag("".join(list(filter(_append, super().__iter__()))))

    def __mul__(self, other):
        assert other.isdigit()
        return Diag(self.string * int(other))

    def __iter__(self):
        a, b = 1, 1
        while a < len(self):
            yield self[a - 1]
            a, b = b, a + b

    @staticmethod
    def _fibonacci_indices(n):
        fib_indices = [0, 1]
        while fib_indices[-1] < n:
            fib_indices.append(fib_indices[-1] + fib_indices[-2])
        return fib_indices[:-1]



