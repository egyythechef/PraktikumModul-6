n1, n2 = map(int, input().split())
if n1 != n2:
    print("Jumlah tidak sama")
else:
    baris1 = list(map(int, input().split()))
    baris2 = list(map(int, input().split()))
    list_hasil = []
    for k in range(n1):
        hasil = baris1[k] * baris2[k]
        list_hasil.append(hasil)
        print(hasil, end=' ')