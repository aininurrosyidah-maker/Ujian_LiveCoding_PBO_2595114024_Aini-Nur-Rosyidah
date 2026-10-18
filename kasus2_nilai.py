class PenilaianMahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        
    def nilai_akhir(self):
        return self.tugas * 0.3 + self.uts * 0.3 + self.uas * 0.4
    
    def grade(self):
        nilai = self.nilai_akhir()
        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 50:
            return "D"
        return "E"
    
    def tampilkan_hasil(self):
        nilai = self.nilai_akhir()
        status = "LULUS" if nilai >= 65 else "TIDAK LULUS"
        
        print("HASIL AKADEMIK")
        print("NIM:", self.nim)
        print("Nama:", self.nama)
        print(f"Nilai akhir: {nilai:.2f}")
        print("Grade:", self.grade())
        print("Status:", status)
        
try: 
    print("SISTEM PENILAIAN")
    
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    if not nim.strip() or not nama.strip():
        raise ValueError("NIM dan nama wajib diisi.")
    if any(n < 0 or n > 100 for n in [tugas, uts, uas]):
        raise ValueError("Nilai harus 0 sampai 100.")
    
    mahasiswa = PenilaianMahasiswa(nim, nama, tugas, uts, uas)
    mahasiswa.tampilkan_hasil()
    
except ValueError as e:
    print("Input salah:", e)
        