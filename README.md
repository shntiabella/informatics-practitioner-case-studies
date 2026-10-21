# 6 Studi Kasus Informatika — Python

Repositori ini berisi enam mini-project yang terinspirasi dari topik pada poster *Informatics Practitioner Lecture Series*. Setiap studi kasus memiliki contoh data sintetis agar dapat dijalankan tanpa mengunduh dataset eksternal.

## Daftar studi kasus

1. **Data Analysis & AI** — analisis dan prediksi kelulusan mahasiswa.
2. **AI untuk Kesiapan Tenaga Kerja Digital** — analisis kesenjangan keterampilan lowongan kerja.
3. **AI, Karier, dan Persaingan Industri** — pencocokan CV sederhana dengan deskripsi pekerjaan.
4. **Teknologi untuk Pembelajaran** — rekomendasi materi belajar berdasarkan hasil kuis.
5. **Human-Computer Interaction & Data Visualization** — evaluasi usability sederhana dan visualisasi hasil.
6. **Remote Sensing & AI untuk Pemantauan Hutan** — klasifikasi contoh gangguan hutan dari fitur satelit.

> Catatan: judul/topik nomor 1–4 dirumuskan dari teks yang terbaca pada poster. Implementasi adalah studi kasus pembelajaran, bukan reproduksi sistem atau hasil riset pembicara. Data yang digunakan sintetis. Studi kasus nomor 6 tidak menggunakan citra Sentinel asli dan bukan sistem operasional deteksi kebakaran/deforestasi.

## Struktur folder

```text
6-studi-kasus-python/
├── README.md
├── requirements.txt
├── 01_data_analysis_ai/
│   └── main.py
├── 02_digital_workforce_ai/
│   └── main.py
├── 03_ai_career_matching/
│   └── main.py
├── 04_technology_learning/
│   └── main.py
├── 05_hci_data_visualization/
│   └── main.py
└── 06_forest_remote_sensing_ai/
    └── main.py
```

## Instalasi

Disarankan menggunakan Python 3.10 atau lebih baru.

```bash
python -m venv .venv
```

Aktifkan environment:
- Windows PowerShell: `.venv\\Scripts\\Activate.ps1`
- Windows CMD: `.venv\\Scripts\\activate.bat`
- macOS/Linux: `source .venv/bin/activate`

Lalu instal dependensi:

```bash
pip install -r requirements.txt
```

## Menjalankan studi kasus

Jalankan perintah dari folder utama repositori:

```bash
python 01_data_analysis_ai/main.py
python 02_digital_workforce_ai/main.py
python 03_ai_career_matching/main.py
python 04_technology_learning/main.py
python 05_hci_data_visualization/main.py
python 06_forest_remote_sensing_ai/main.py
```

Grafik yang dibuat akan disimpan sebagai file PNG di folder studi kasus terkait.

## Ringkasan metode

| No. | Studi kasus | Metode Python |
|---|---|---|
| 1 | Prediksi kelulusan | pandas, scikit-learn, Logistic Regression |
| 2 | Kesenjangan keterampilan kerja | pandas, TF-IDF, cosine similarity |
| 3 | Pencocokan CV dan lowongan | TF-IDF, cosine similarity |
| 4 | Rekomendasi materi belajar | pandas, aturan berbasis skor |
| 5 | Evaluasi HCI dan visualisasi | pandas, matplotlib |
| 6 | Klasifikasi gangguan hutan | pandas, Random Forest, evaluasi model |

## Pengembangan lanjutan

- Ganti data sintetis dengan data nyata yang legal dan sudah dianonimkan.
- Pisahkan data latih dan data uji serta lakukan validasi lebih lanjut.
- Simpan konfigurasi dan hasil eksperimen agar dapat direproduksi.
- Untuk studi kasus nomor 6, gunakan label hasil verifikasi dan fitur citra Sentinel-1/Sentinel-2. Untuk CNN berbasis citra, diperlukan patch citra berlabel dan sumber daya komputasi yang memadai.
