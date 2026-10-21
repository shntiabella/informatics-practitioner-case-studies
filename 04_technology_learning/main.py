"""Studi kasus 4: rekomendasi materi belajar berdasarkan hasil kuis."""
import pandas as pd

def main():
    # Nilai kuis sintetis skala 0–100.
    scores = pd.DataFrame([
        {"materi": "Python dasar", "nilai": 82, "prasyarat": "variabel, tipe data, percabangan"},
        {"materi": "Struktur data", "nilai": 58, "prasyarat": "list, stack, queue, dictionary"},
        {"materi": "Basis data SQL", "nilai": 67, "prasyarat": "SELECT, JOIN, agregasi"},
        {"materi": "Machine learning", "nilai": 43, "prasyarat": "Python, statistik, train-test split"},
        {"materi": "Visualisasi data", "nilai": 76, "prasyarat": "pandas, grafik, interpretasi"},
    ])
    def status(nilai):
        if nilai < 60:
            return "Perlu pengulangan"
        if nilai < 75:
            return "Latihan tambahan"
        return "Lanjut ke materi berikutnya"
    scores["rekomendasi"] = scores["nilai"].apply(status)
    scores = scores.sort_values("nilai")

    print("=== Studi Kasus 4: Teknologi untuk Pembelajaran ===")
    print(scores.to_string(index=False))
    print("\nPrioritas belajar:")
    for _, row in scores.head(2).iterrows():
        print(f"- {row['materi']}: ulangi konsep {row['prasyarat']}.")
    print("\nCatatan: rekomendasi berbasis ambang nilai sederhana, bukan diagnosis kemampuan permanen.")

if __name__ == "__main__":
    main()
