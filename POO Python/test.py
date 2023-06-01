a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

soma = sum(range(4))
print(soma)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)

    else:
        print(n, ' a prime number')

i = 256*256
print('The value of i is', i)


@property
def carro(self):
    return self._carro

@carro.setter
def carro(self, value):
    self._carro = value

