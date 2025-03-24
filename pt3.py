import math  # Import library math untuk menggunakan fungsi matematika (sqrt)

# Menampilkan identitas mahasiswa
print("NIM     :241011700899")
print("NAMA    :RATNA NIKEN PUSPORINI")
print("KELAS   :02SIFE006")

# Menampilkan garis pemisah
print("=========================================================================================")
print("Program Menghitung Rumus Pythagoras")  # Judul program

# Looping agar program bisa berjalan berulang kali
while True:
    # Menampilkan menu pilihan perhitungan
    print("\nPilih jenis perhitungan:")
    print("1. Menghitung panjang hipotenusa (c) jika diketahui a dan b")
    print("2. Menghitung panjang sisi a atau b jika diketahui hipotenusa (c) dan sisi lainnya")
    print("3. Keluar dari program")

    # Meminta input dari user untuk memilih jenis perhitungan
    pilihan = input("Masukkan pilihan (1/2/3): ")

    # Cek apakah user memilih perhitungan hipotenusa
    if pilihan == "1":
        # Meminta input panjang sisi a dan b
        a = float(input("Masukkan panjang sisi a: "))
        b = float(input("Masukkan panjang sisi b: "))

        # Menghitung hipotenusa (c) menggunakan rumus Pythagoras
        # Rumus: c = √(a² + b²)
        c = math.sqrt(a**2 + b**2)

        # Menampilkan hasil perhitungan hipotenusa dengan 2 desimal
        print(f"Panjang sisi hipotenusa (c) adalah: {c:.2f}")

    # Cek apakah user memilih perhitungan sisi a atau b
    elif pilihan == "2":
        # Meminta input panjang hipotenusa (c)
        c = float(input("Masukkan panjang sisi hipotenusa c: "))
        # Meminta user memilih sisi yang ingin dicari (a atau b)
        pilih_sisi = input("Apakah kamu ingin mencari sisi a atau b? (a/b): ").lower()

        # Jika user ingin mencari sisi a
        if pilih_sisi == "a":
            # Meminta input panjang sisi b
            b = float(input("Masukkan panjang sisi b: "))
            
            # Validasi: Hipotenusa harus lebih besar dari sisi b
            if c > b:
                # Rumus: a = √(c² - b²)
                a = math.sqrt(c**2 - b**2)
                # Menampilkan hasil perhitungan sisi a
                print(f"Panjang sisi a adalah: {a:.2f}")
            else:
                # Menampilkan pesan error jika input tidak valid
                print("Error: Nilai c harus lebih besar dari b!")

        # Jika user ingin mencari sisi b
        elif pilih_sisi == "b":
            # Meminta input panjang sisi a
            a = float(input("Masukkan panjang sisi a: "))
            
            # Validasi: Hipotenusa harus lebih besar dari sisi a
            if c > a:
                # Rumus: b = √(c² - a²)
                b = math.sqrt(c**2 - a**2)
                # Menampilkan hasil perhitungan sisi b
                print(f"Panjang sisi b adalah: {b:.2f}")
            else:
                # Menampilkan pesan error jika input tidak valid
                print("Error: Nilai c harus lebih besar dari a!")
        else:
            # Menampilkan pesan error jika input bukan a atau b
            print("Pilihan tidak valid!")

    # Cek apakah user memilih untuk keluar dari program
    elif pilihan == "3":
        # Menampilkan pesan keluar dan menghentikan loop
        print("Anda keluar dari program")
        break  # Keluar dari loop

    # Menampilkan pesan error jika input menu tidak valid
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
