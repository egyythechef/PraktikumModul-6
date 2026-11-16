n = int(input())
angka = list(map(int, input().split()))

for i in range(n):
    kali = i + 1
    hasil = angka[i] * kali
    print(hasil, end=" ")