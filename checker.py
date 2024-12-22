import webbrowser

# Fungsi untuk membaca kode dari file code.txt
def read_codes_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            codes = [line.strip() for line in file if line.strip()]
        return codes
    except FileNotFoundError:
        print(f"File '{file_path}' tidak ditemukan. Pastikan file ada di direktori yang benar.")
        return []
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file: {e}")
        return []

# Fungsi untuk membuka URL berdasarkan kode
def open_urls(codes, base_url):
    if not codes:
        print("Tidak ada kode untuk diproses.")
        return

    for code in codes:
        url = f"{base_url}{code}"
        print(f"Membuka URL: {url}")
        webbrowser.open(url)

file_path = "code.txt"
base_url = "xxx" #Ganti dengan URL yang mau dibuka


codes = read_codes_from_file(file_path)


open_urls(codes, base_url)