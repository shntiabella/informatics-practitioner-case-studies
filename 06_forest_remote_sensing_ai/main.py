"""Studi kasus 6: klasifikasi gangguan hutan dari fitur satelit sintetis.

Demo ini memakai fitur tabular buatan, bukan citra Sentinel asli.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, ConfusionMatrixDisplay, accuracy_score

OUT = Path(__file__).resolve().parent

def main():
    rng = np.random.default_rng(24)
    classes = ["pertanian", "penebangan", "pertambangan", "kebakaran", "gangguan_alami"]
    centers = {
        "pertanian": [0.35, 0.55, 0.20, 0.15],
        "penebangan": [0.55, 0.40, 0.30, 0.20],
        "pertambangan": [0.20, 0.25, 0.75, 0.60],
        "kebakaran": [0.25, 0.20, 0.65, 0.35],
        "gangguan_alami": [0.45, 0.35, 0.40, 0.30],
    }
    rows = []
    for label in classes:
        for _ in range(100):
            values = np.clip(np.array(centers[label]) + rng.normal(0, 0.12, 4), 0, 1)
            rows.append([*values, label])
    data = pd.DataFrame(rows, columns=[
        "vegetation_change", "radar_backscatter_change",
        "bare_soil_signal", "burn_signal", "driver"
    ])
    X = data.drop(columns="driver")
    y = data["driver"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    print("=== Studi Kasus 6: Remote Sensing & AI untuk Pemantauan Hutan ===")
    print(f"Akurasi data uji sintetis: {accuracy_score(y_test, pred):.3f}")
    print("\nLaporan klasifikasi:\n", classification_report(y_test, pred, zero_division=0))
    print("\nPenting: nilai evaluasi ini hanya mengukur data sintetis dan tidak mewakili akurasi satelit dunia nyata.")

    ConfusionMatrixDisplay.from_predictions(y_test, pred, xticks_rotation=30)
    plt.title("Confusion Matrix — Data Sintetis")
    plt.tight_layout()
    cm_path = OUT / "confusion_matrix.png"
    plt.savefig(cm_path, dpi=150)
    plt.close()

    importance = pd.Series(model.feature_importances_, index=X.columns).sort_values()
    importance.plot(kind="barh", title="Feature Importance — Data Sintetis")
    plt.tight_layout()
    fi_path = OUT / "feature_importance.png"
    plt.savefig(fi_path, dpi=150)
    plt.close()
    print(f"Grafik disimpan: {cm_path} dan {fi_path}")

if __name__ == "__main__":
    main()
