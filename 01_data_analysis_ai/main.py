"""Studi kasus 1: analisis dan prediksi kelulusan mahasiswa dengan data sintetis."""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

OUT = Path(__file__).resolve().parent
rng = np.random.default_rng(7)

def main():
    n = 240
    data = pd.DataFrame({
        "jam_belajar_per_minggu": rng.integers(1, 21, n),
        "kehadiran_persen": rng.integers(50, 101, n),
        "tugas_selesai_persen": rng.integers(40, 101, n),
    })
    # Label sintetis untuk demonstrasi, bukan kriteria akademik resmi.
    score = (data.jam_belajar_per_minggu * 1.5
             + data.kehadiran_persen * 0.35
             + data.tugas_selesai_persen * 0.25
             + rng.normal(0, 8, n))
    data["lulus"] = (score >= 65).astype(int)

    X = data[["jam_belajar_per_minggu", "kehadiran_persen", "tugas_selesai_persen"]]
    y = data["lulus"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("=== Studi Kasus 1: Data Analysis & AI ===")
    print("\nRingkasan data:\n", data.describe().round(2))
    print(f"\nAkurasi pada data uji: {accuracy_score(y_test, pred):.3f}")
    print("\nLaporan klasifikasi:\n", classification_report(y_test, pred, zero_division=0))
    print("\nContoh prediksi 1 mahasiswa:")
    example = pd.DataFrame([{
        "jam_belajar_per_minggu": 10,
        "kehadiran_persen": 85,
        "tugas_selesai_persen": 90
    }])
    print("Data:", example.to_dict(orient="records")[0])
    print("Prediksi:", "Lulus" if model.predict(example)[0] else "Perlu dukungan akademik")

    data.groupby("lulus")["jam_belajar_per_minggu"].mean().plot(kind="bar")
    plt.title("Rata-rata Jam Belajar Berdasarkan Label Sintetis")
    plt.xlabel("Label (0 = tidak lulus, 1 = lulus)")
    plt.ylabel("Jam belajar per minggu")
    plt.tight_layout()
    path = OUT / "analisis_kelulusan.png"
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"\nGrafik disimpan: {path}")

if __name__ == "__main__":
    main()
