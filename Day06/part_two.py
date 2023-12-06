
L = open('input.txt').read().split('\n')
time = int(''.join(L[0].split(':')[1].split()))
distance = int(''.join(L[1].split(':')[1].split()))

cnt = sum(1 for i in range(1, time) if (time - i) * i > distance)

print(f'Solution: {cnt}')
