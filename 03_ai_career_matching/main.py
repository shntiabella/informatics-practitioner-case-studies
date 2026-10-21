"""Studi kasus 3: pencocokan CV sederhana dengan lowongan kerja."""
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

OUT = Path(__file__).resolve().parent

def main():
    cv = """
    Mahasiswa Informatika memiliki pengalaman Python, analisis data, SQL,
    pengembangan aplikasi web, Git, dan pemetaan geospasial menggunakan QGIS.
    """
    vacancies = [
        ("Junior Data Analyst", "Python SQL statistik dashboard analisis data Excel"),
        ("Python Backend Intern", "Python API database SQL Git testing"),
        ("GIS Intern", "GIS QGIS remote sensing peta geospasial Python"),
        ("UI Designer", "Figma user research wireframe prototyping design system"),
    ]
    documents = [cv] + [description for _, description in vacancies]
    matrix = TfidfVectorizer(stop_words=None).fit_transform(documents)
    scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
    ranked = sorted(zip(vacancies, scores), key=lambda item: item[1], reverse=True)

    print("=== Studi Kasus 3: AI untuk Karier ===")
    print("Pencocokan berbasis kemiripan teks. Ini bukan penilaian kelayakan atau keputusan rekrutmen.")
    for rank, ((title, description), score) in enumerate(ranked, start=1):
        print(f"{rank}. {title}: skor kemiripan {score:.3f}")
        print(f"   Keterampilan pada iklan: {description}")

    best_title = ranked[0][0][0]
    print(f"\nLowongan dengan kemiripan teks tertinggi: {best_title}")
    print("Saran: sesuaikan CV dengan pengalaman yang benar-benar dimiliki; jangan menambahkan keterampilan palsu.")

if __name__ == "__main__":
    main()
