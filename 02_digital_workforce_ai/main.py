"""Studi kasus 2: mencari kesenjangan keterampilan tenaga kerja digital."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

OUT = Path(__file__).resolve().parent

def main():
    jobs = pd.DataFrame([
        {"jabatan": "Data Analyst", "keterampilan": "Python SQL Excel statistik visualisasi data"},
        {"jabatan": "Web Developer", "keterampilan": "HTML CSS JavaScript React API Git"},
        {"jabatan": "AI Engineer", "keterampilan": "Python machine learning deep learning statistik"},
        {"jabatan": "GIS Analyst", "keterampilan": "Python GIS QGIS geospatial remote sensing SQL"},
    ])
    kandidat = "Python SQL dasar Excel dasar visualisasi data Git"
    corpus = jobs["keterampilan"].tolist() + [kandidat]
    matrix = TfidfVectorizer().fit_transform(corpus)
    scores = cosine_similarity(matrix[-1], matrix[:-1]).flatten()
    jobs["kemiripan_kandidat"] = scores
    jobs = jobs.sort_values("kemiripan_kandidat", ascending=False)

    # Demonstrasi sederhana: token keterampilan yang belum muncul di profil kandidat.
    candidate_tokens = set(kandidat.lower().split())
    jobs["keterampilan_yang_perlu_dipelajari"] = jobs["keterampilan"].apply(
        lambda s: ", ".join([w for w in s.split() if w.lower() not in candidate_tokens])
    )

    print("=== Studi Kasus 2: AI & Kesiapan Tenaga Kerja Digital ===")
    print("Profil keterampilan kandidat:", kandidat)
    print("\nKecocokan terhadap bidang pekerjaan (skor kemiripan teks, bukan peluang diterima):")
    print(jobs[["jabatan", "kemiripan_kandidat", "keterampilan_yang_perlu_dipelajari"]].to_string(
        index=False, formatters={"kemiripan_kandidat": "{:.3f}".format}
    ))

    plt.figure(figsize=(8, 4))
    plt.bar(jobs["jabatan"], jobs["kemiripan_kandidat"])
    plt.title("Kemiripan Profil Kandidat dengan Keterampilan Pekerjaan")
    plt.ylabel("Cosine similarity")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    path = OUT / "kesenjangan_keterampilan.png"
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"\nGrafik disimpan: {path}")

if __name__ == "__main__":
    main()
