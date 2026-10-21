"""Studi kasus 5: evaluasi usability dan visualisasi data HCI."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent

def main():
    # Contoh survei sintetis skala 1–5.
    survey = pd.DataFrame([
        {"responden": "P1", "mudah_digunakan": 4, "navigasi_jelas": 4, "informasi_mudah_dicari": 5},
        {"responden": "P2", "mudah_digunakan": 3, "navigasi_jelas": 2, "informasi_mudah_dicari": 3},
        {"responden": "P3", "mudah_digunakan": 4, "navigasi_jelas": 3, "informasi_mudah_dicari": 4},
        {"responden": "P4", "mudah_digunakan": 2, "navigasi_jelas": 2, "informasi_mudah_dicari": 3},
        {"responden": "P5", "mudah_digunakan": 5, "navigasi_jelas": 4, "informasi_mudah_dicari": 4},
        {"responden": "P6", "mudah_digunakan": 3, "navigasi_jelas": 3, "informasi_mudah_dicari": 2},
    ])
    metrics = ["mudah_digunakan", "navigasi_jelas", "informasi_mudah_dicari"]
    means = survey[metrics].mean().sort_values(ascending=False)

    print("=== Studi Kasus 5: HCI & Data Visualization ===")
    print("Rata-rata penilaian (skala 1–5):")
    print(means.round(2).to_string())
    weakest = means.idxmin()
    label = {
        "mudah_digunakan": "kemudahan penggunaan",
        "navigasi_jelas": "kejelasan navigasi",
        "informasi_mudah_dicari": "kemudahan menemukan informasi"
    }[weakest]
    print(f"\nPrioritas perbaikan antarmuka: {label}.")
    print("Gunakan hasil ini sebagai petunjuk awal; lakukan wawancara/pengujian lanjutan dengan pengguna.")

    plt.figure(figsize=(8, 4))
    means.sort_values().plot(kind="barh")
    plt.xlim(0, 5)
    plt.xlabel("Rata-rata skor (1–5)")
    plt.title("Hasil Survei Usability Sintetis")
    plt.tight_layout()
    path = OUT / "hasil_usability.png"
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"Grafik disimpan: {path}")

if __name__ == "__main__":
    main()
