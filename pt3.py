print ("NIM     :241011700899")
print ("NAMA    :RATNA NIKEN PUSPORINI")
print ("KELAS   :02SIFE006")

print ("=========================================================================================")
print ("Program Menghitung Rumus Pythagoras")
print("Pilih jenis perhitungan:")
print("1. Menghitung panjang hipotenusa (c) jika diketahui a dan b")
print("2. Menghitung panjang sisi a atau b jika diketahui hipotenusa (c) dan sisi lainnya")

import math 
pilihan = input("Masukkan pilihan (1/2): ")

if pilihan == "1":
    a = float(input("Masukkan panjang sisi a: "))
    b = float(input("Masukkan panjang sisi b: "))
    
    # Menghitung panjang hipotenusa
    c = math.sqrt(a**2 + b**2)
    
    # hasil
    print(f"Panjang sisi hipotenusa (c) adalah: {c}")
    
elif pilihan == "2":
    # Input sisi yang diketahui
    c = float(input("Masukkan panjang sisi hipotenusa c: "))
    pilih_sisi = input("Apakah kamu ingin mencari sisi a atau b? (a/b): ").lower()

    if pilih_sisi == "a":
        b = float(input("Masukkan panjang sisi b: "))
        a = math.sqrt(c**2 - b**2)
        print(f"Panjang sisi a adalah: {a}")
    elif pilih_sisi == "b":
        a = float(input("Masukkan panjang sisi a: "))
        b = math.sqrt(c**2 - a**2)
        print(f"Panjang sisi b adalah: {b}")
    else:
        print("Pilihan tidak valid!")
else:
    print("Pilihan tidak valid!")
