baris, kolom = map(int, input().split())
angka = list(map(int, input().split()))
matriks = []
index = 0

for i in range(baris):
    baris_data = []
    for j in range(kolom):
        baris_data.append(angka[index])
        index += 1
    matriks.append(baris_data)

print()
for row in matriks:
    print(' '.join(map(str, row)))