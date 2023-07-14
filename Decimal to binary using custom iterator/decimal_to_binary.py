class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


def dec_to_bin(num):
    rem = ''
    ini = num
    while num != 0:
        rem += str(num % 2)
        num = num // 2

    binary = ''
    for i in Reverse(rem):
        binary+=i
    print(str(ini) + " in binary is " + binary)
    


dec_to_bin(6)
