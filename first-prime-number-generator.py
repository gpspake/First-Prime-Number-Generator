# Return First Prime Number
class first_prime_number:
    def __init__(self):
        self.n = 2

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        return self.n

generator = first_prime_number()
print(generator.next())
