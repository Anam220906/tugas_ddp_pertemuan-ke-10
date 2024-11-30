def hitung_luas_segitiga(alas, tinggi):
    """
    Fungsi untuk menghitung luas segitiga
    :param alas: panjang alas segitiga (float)
    :param tinggi: tinggi segitiga (float)
    :return: luas segitiga (float)
    """
    return 0.5 * alas * tinggi

# Fungsi untuk memvalidasi input pengguna
def input_float(prompt):
    while True:
        try:
            nilai = float(input(prompt))
            if nilai <= 0:
                raise ValueError("Nilai harus lebih besar dari 0.")
            return nilai
        except ValueError as e:
            print(f"Input tidak valid: {e}")

# Program utama
if __name__ == "__main__":
    print("Menghitung Luas Segitiga")
    alas = input_float("Masukkan panjang alas (dalam satuan meter): ")
    tinggi = input_float("Masukkan tinggi segitiga (dalam satuan meter): ")

    luas = hitung_luas_segitiga(alas, tinggi)
    print(f"Luas segitiga dengan alas {alas} meter dan tinggi {tinggi} meter adalah {luas} meter persegi.")
