import tkinter as tk
from tkinter import messagebox
import joblib
import os
import sys
import joblib
import sklearn  # <--- TAMBAHKAN BARIS INI
from sklearn.ensemble import RandomForestRegressor  # <--- ATAU TAMBAHKAN INI


# Fungsi untuk mendeteksi path saat dibungkus PyInstaller
def resource_path(relative_path):
    try:
        # PyInstaller membuat folder temporary _MEIPASS saat runtime
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Muat model menggunakan resource_path
model_path = resource_path("model_pajak.pkl")
model = joblib.load(model_path)


def prediksi():
    try:
        bulan = int(entry_bulan.get())
        tahun = int(entry_tahun.get())
        lag1 = float(entry_lag1.get())
        lag12 = float(entry_lag12.get())

        hasil = model.predict([[bulan, tahun, lag1, lag12]])[0]
        label_hasil.config(text=f"Prediksi Penerimaan: Rp {hasil:,.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Input tidak valid: {e}")


root = tk.Tk()
root.title("Aplikasi Prediksi Penerimaan Pajak")
root.geometry("400x300")

tk.Label(root, text="Bulan (1-12):").pack()
entry_bulan = tk.Entry(root)
entry_bulan.pack()

tk.Label(root, text="Tahun:").pack()
entry_tahun = tk.Entry(root)
entry_tahun.pack()

tk.Label(root, text="Penerimaan Bulan Lalu (Rp):").pack()
entry_lag1 = tk.Entry(root)
entry_lag1.pack()

tk.Label(root, text="Penerimaan Bulan Sama Tahun Lalu (Rp):").pack()
entry_lag12 = tk.Entry(root)
entry_lag12.pack()

tk.Button(root, text="Hitung Prediksi", command=prediksi).pack(pady=10)
label_hasil = tk.Label(root, text="", font=("Arial", 12, "bold"))
label_hasil.pack()

root.mainloop()