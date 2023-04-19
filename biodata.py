# Membuat kamus berisi biodata mahasiswa dan nilai matakuliah
mahasiswa = {
    "laela elsa putri": {
        "nim": "TI9220011",
        "alamat": "jonggat",
        "prodi": "teknik informatika",
        "semester": 2,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "Pemrograman Dasar": 92,
            "Kalkulus": 88,
            "Fisika Dasar": 90
        }
    },
    "nora ananda putri": {
        "nim": "TI19220015",
        "alamat": "Ganti",
        "prodi": "tenik informatika",
        "semester": 2,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "Pemrograman Lanjut": 90,
            "Algoritma dan Struktur Data": 87,
            "Basis Data": 92
        }
    },
    "melina": {
        "nim": "TI19220009",
        "alamat": "Bodak",
        "prodi": "teknik informatika",
        "semester": 2,
        "ipk": 3.6,
        "nilai_matakuliah": {
            "Jaringan Komputer": 85,
            "Sistem Digital": 80,
            "Manajemen Basis Data": 90
        }
    },
    "dwi zahira": {
        "nim": "TI19220001",
        "alamat": "sembalun",
        "prodi": "Teknik Informatika",
        "semester": 2,
        "ipk": 3.7,
        "nilai_matakuliah": {
            "Kimia Fisika": 88,
            "Rekayasa Proses Kimia": 85,
            "Termokimia": 92
        }
    },
    "rial husne": {
        "nim": "TI19220005",
        "alamat": "darmaji",
        "prodi": "Teknik Informatika",
        "semester": 2,
        "ipk": 3.7,
        "nilai_matakuliah": {
            "Jaringan Komputer": 80,
            "Aljabar Linier": 80,
            "Konstruksi Beton": 90
        }
    }
}

# Menampilkan biodata mahasiswa dan nilai akumulasi tiga matakuliah
for nama, data in mahasiswa.items():
    print("Biodata Mahasiswa")
    print("Nama          :", nama)
    print("NIM           :", data["nim"])
    print("Alamat        :", data["alamat"])
    print("Program Studi :", data["prodi"])
    print("Semester      :", data["semester"])
    print("IPK           :", data["ipk"])
    print("Nilai Akumulasi Matakuliah:")
    total_nilai = 0
    for matakuliah, nilai in data["nilai_matakuliah"].items():
        print("-", matakuliah, ":", nilai)
        total_nilai += nilai
    print("Total Nilai:", total_nilai)
    print("")
