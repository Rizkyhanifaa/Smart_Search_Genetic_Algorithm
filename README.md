# Smart_Search_Genetic_Algorithm
Sebuah proyek implementasi algoritma genetika (Genetic Algorithm/GA) untuk mencari nilai minimum dari fungsi matematis dua variabel dalam domain [-10, 10]. Proyek ini dibuat sebagai tugas pencarian berbasis kasus (Case-Based Searching) dengan pendekatan optimasi.

## 📌 Tujuan
Mencari nilai terbaik dari pasangan variabel (x₁, x₂) yang meminimalkan fungsi berikut:
f(x₁, x₂) = - (sin(x₁) * cos(x₂) * tan(x₁ + x₂) + ¾ * e^(1 - √(x₁²)))

## 🧠 Metodologi Algoritma Genetika
- **Representasi Kromosom**: 20-bit string biner (10 bit untuk x₁ dan 10 bit untuk x₂)
- **Dekode**: Mengubah biner ke nilai riil dalam rentang [-10, 10]
- **Fitness Function**: Nilai fungsi f(x₁, x₂), semakin kecil berarti semakin baik
- **Seleksi**: Tournament selection (ukuran 3)
- **Crossover**: One-point crossover (probabilitas 𝑃𝑐 = 0.8)
- **Mutasi**: Flip bit mutation (probabilitas 𝑃𝑚 = 0.1)
- **Elitisme**: Menyimpan individu terbaik ke generasi berikutnya
- **Kriteria Berhenti**: 100 generasi

## ⚙️ Cara Menjalankan
1. Pastikan Python 3.x telah terpasang.
2. Jalankan `python searching.py` di terminal 
