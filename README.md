# Tax Revenue Projection Machine Learning Model

Language / Bahasa:
* [Bahasa Indonesia](#bahasa-indonesia)
* [English](#english)

---

## Bahasa Indonesia

### 📌 Latar Belakang & Deskripsi Proyek
Proyek ini dikembangkan untuk menjawab tantangan dan kesulitan yang sering dihadapi oleh pegawai/staf keuangan dalam menghitung proyeksi penerimaan pajak bulanan secara akurat dan efisien. Perhitungan manual sering kali memakan waktu serta rentan terhadap bias atau kesalahan estimasi.

Untuk mengatasi permasalahan tersebut, proyek ini menghadirkan model **Machine Learning** yang mengintegrasikan disiplin ilmu statistika. Pemilihan algoritma **Random Forest Regressor** dilakukan secara terstruktur melalui analisis dan evaluasi metrik statistik mendalam pada dataset historis yang telah disiapkan.

### ✨ Fitur Utama
* **Pendekatan Berbasis Statistika & ML**: Memanfaatkan model `RandomForestRegressor` dengan evaluasi performa menyeluruh (MAE, MAPE, MSE, dan $R^2$ Score).
* **Prediksi Otomatis**: Mempermudah pegawai dalam memproyeksikan estimasi penerimaan pajak tiap bulan secara cepat dan terukur.
* **Model Persistence**: Model yang telah dilatih disimpan menggunakan `joblib` untuk mempermudah implementasi (*deployment*) dan pengujian ulang tanpa perlu melatih ulang (*retrain*) dari awal.

### 🛠️ Teknologi & Tools

#### Bahasa & Framework Utama:
* **Python** (via Anaconda Distribution)
* **Jupyter Notebook** (sebagai lingkungan pengembangan dan analisis data)

#### Library yang Digunakan:
* **Pengolahan & Analisis Data**: `pandas`, `numpy`
* **Machine Learning & Evaluasi**: `scikit-learn`
  * Model: `RandomForestRegressor`
  * Metrik Evaluasi: `mean_absolute_error`, `mean_absolute_percentage_error`, `mean_squared_error`, `r2_score`
* **Penyimpanan Model**: `joblib`

---

## English

### 📌 Background & Project Overview
This project was developed to address the common challenges and difficulties faced by financial staff in accurately and efficiently projecting monthly tax revenues. Manual calculation methods are often time-consuming and prone to estimation errors or biases.

To solve this issue, this project delivers a **Machine Learning** model that incorporates rigorous statistical evaluation. The selection of the **Random Forest Regressor** algorithm was guided by in-depth statistical metric evaluations conducted on a prepared historical dataset.

### ✨ Key Features
* **Statistically Driven ML Approach**: Utilizes the `RandomForestRegressor` model backed by comprehensive performance evaluations (MAE, MAPE, MSE, and $R^2$ Score).
* **Automated Projection**: Streamlines the forecasting process for employees to obtain quick and reliable monthly tax revenue estimates.
* **Model Persistence**: The trained model is serialized using `joblib`, enabling easy deployment and quick inference without retraining.

### 🛠️ Tech Stack & Tools

#### Language & Environment:
* **Python** (via Anaconda Distribution)
* **Jupyter Notebook** (Interactive development and data analysis platform)

#### Libraries & Dependencies:
* **Data Processing & Manipulation**: `pandas`, `numpy`
* **Machine Learning & Metrics**: `scikit-learn`
  * Algorithm: `RandomForestRegressor`
  * Evaluation Metrics: `mean_absolute_error`, `mean_absolute_percentage_error`, `mean_squared_error`, `r2_score`
* **Model Serialization**: `joblib`

---

### 🚀 Cara Penggunaan / How to Run

1. **Clone repository:**
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Jalankan Jupyter Notebook / Launch Jupyter Notebook:**
   Pastikan Anda telah menginstal [Anaconda Distribution](https://www.anaconda.com/). Buka Anaconda Prompt / Terminal, lalu jalankan:
   ```bash
   jupyter notebook
   ```

3. **Buka berkas notebook / Open the notebook file:**
   Pilih file notebook (`.ipynb`) utama di direktori proyek dan jalankan *cell* secara berurutan.