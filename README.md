# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal luas karena reputasinya dalam mencetak lulusan berkualitas. Selama lebih dari dua dekade beroperasi, institusi ini telah meluluskan ribuan mahasiswa dari berbagai program studi, dan berhasil menjalin kepercayaan masyarakat sebagai lembaga pendidikan yang unggul dan berintegritas.

Namun, di balik keberhasilan tersebut, Jaya Jaya Institut menghadapi sebuah tantangan serius yang berulang dari tahun ke tahun yaitu tingginya angka mahasiswa yang tidak menyelesaikan studi atau dropout. Fenomena ini bukan hanya berdampak pada reputasi akademik institusi, tetapi juga memengaruhi efisiensi operasional dan keberlanjutan bisnis secara keseluruhan.

Dropout mahasiswa sering kali dipengaruhi oleh berbagai faktor seperti latar belakang ekonomi, prestasi akademik, kondisi sosial, maupun keterbatasan personal lainnya. Apabila tidak diantisipasi dengan tepat, dropout dapat mengakibatkan kerugian dari sisi finansial (biaya subsidi internal yang sia-sia), menurunkan peringkat institusi di mata publik, dan memperbesar kesenjangan sosial bagi individu yang gagal menyelesaikan pendidikannya.

Oleh karena itu, Jaya Jaya Institut memiliki kebutuhan strategis untuk mendeteksi lebih awal mahasiswa yang berisiko mengalami dropout, agar dapat diberikan intervensi, pendampingan, atau solusi yang tepat sasaran. Dengan memanfaatkan pendekatan data science dan machine learning, diharapkan institusi ini dapat Mengidentifikasi pola-pola yang berkaitan dengan risiko dropout, Mengambil keputusan berbasis data untuk strategi retensi mahasiswa dan Meningkatkan efisiensi program pembinaan dan bimbingan akademik.

Proyek ini merupakan bagian dari upaya transformasi digital dalam bidang pendidikan yang menggabungkan teknologi, analisis data, dan kebijakan kampus untuk menciptakan lingkungan belajar yang lebih inklusif dan adaptif terhadap kebutuhan mahasiswa.

### Permasalahan Bisnis
1. Sekitar 25–35% mahasiswa tidak menyelesaikan studi mereka hingga lulus, yang berdampak signifikan terhadap akreditasi dan kualitas lulusan.
2. Belum tersedia alat untuk mengidentifikasi risiko dropout secara otomatis.
3. Banyaknya faktor membuat analisis manual tidak efektif.
4. Dropout tinggi berdampak negatif pada reputasi kampus.
5. Tidak ada pemetaan risiko yang jelas untuk membimbing mahasiswa.


### Cakupan Proyek
Proyek ini bertujuan untuk membangun sistem prediksi dropout mahasiswa dengan pendekatan data science. Proyek terdiri dari tahapan-tahapan sebagai berikut:

1. Persiapan
  - Mengimpor library yang diperlukan seperti `pandas`, `numpy`, `seaborn`, `matplotlib`, `sklearn`, dan `joblib`.
  - Mengambil dan memuat dataset mahasiswa dari sumber terpercaya (UCI Machine Learning Repository).

2. Data Understanding
  - Menjelaskan struktur dan deskripsi tiap fitur (variabel) dalam dataset.
  - Melakukan analisis deskriptif (univariate dan multivariate).
  - Menampilkan distribusi dan hubungan antar variabel terhadap `Status` (Dropout, Graduate, Enrolled).
  - Menilai outliers, distribusi target, analisis faktor keuangan, faktor akademik, dan faktor beasiswa.

3. Data Preparation / Preprocessing
  - Melakukan label encoding pada fitur kategorikal.
  - Membagi dataset menjadi data latih dan data uji.
  - Menstandarkan fitur numerik menggunakan `StandardScaler`.

4. Modeling
  - Melatih model machine learning (LGBM) dengan data yang telah diproses.
  - Menyimpan model dan scaler ke dalam file `.pkl` menggunakan `joblib`.

5. Evaluation
  - Mengukur performa model menggunakan metrik akurasi, precision, recall, dan confusion matrix.
  - Menilai kemampuan model dalam memprediksi mahasiswa yang berisiko dropout secara tepat.

6. Deployment (Streamlit)
  - Membangun aplikasi berbasis web menggunakan **Streamlit**.
  - Aplikasi mampu menerima input fitur mahasiswa dan memberikan output prediksi status.
  - Model dan scaler dimuat ulang melalui `joblib` dan diintegrasikan dengan antarmuka pengguna.

7. Visualisasi Data dan Monitoring
   - Pembuatan dashboard interaktif untuk monitoring status mahasiswa.
   - Visualisasi indikator penting seperti nilai, usia pendaftaran, status beasiswa, dan pembayaran.

### Persiapan
Dataset yang digunakan dalam proyek ini berasal dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success), dengan judul **"Predict Students Dropout and Academic Success"**. Dataset ini berisi informasi terkait:

- Data demografis mahasiswa (jenis kelamin, usia, status pernikahan)
- Data akademik (nilai masuk, jumlah mata kuliah, hasil evaluasi)
- Informasi administratif (status pembayaran, beasiswa, status utang)
- Label target berupa status akhir mahasiswa: `Graduate`, `Dropout`, atau `Enrolled`

Dataset digunakan dalam format `.csv` dan dimuat langsung menggunakan pustaka `pandas`.

#### Setup environment - Python dengan Virtualenv

1. Membuat virtual environment

    ```python -m venv venv```
2. Mengaktifkan virtual environment

    - Untuk Windows
        ```venv\Scripts\activate```        

    - Untuk MacOS/Linux
        ```source venv/bin/activate```
3. Menginstall dependencies

    ```pip install -r requirements.txt```

## Business Dashboard
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning

Sebagai bagian dari implementasi solusi, telah dikembangkan sebuah **prototype sistem prediksi dropout mahasiswa** berbasis machine learning menggunakan framework **Streamlit**. Sistem ini memungkinkan pengguna untuk menginput data mahasiswa secara manual dan memperoleh prediksi status akademik secara real-time.

### 🛠️ Cara Menjalankan Prototype

Sistem ini dapat dijalankan dengan dua cara:

#### 1. Melalui Hosting Online (Direkomendasikan)
Prototype telah dideploy ke **Streamlit Community Cloud** dan dapat diakses melalui link berikut:

🔗 **[Akses Sistem Prediksi Dropout Mahasiswa](https://bpds-ica-nur-halimah-hmzpx5ver4gwalaccsdgua.streamlit.app/)**

#### 2. Menjalankan Secara Lokal (Opsional)
Jika ingin menjalankan sistem secara lokal:

1. Pastikan telah menginstal semua dependensi:
   
   ```pip install streamlit pandas numpy scikit-learn joblib```
2. Letakkan file berikut dalam satu direktori:
   - app.py (file Streamlit utama)
   - model.pkl (model machine learning Random Forest)
   - scaler.pkl (standarisasi fitur numerik)
3. Jalankan dengan perintah:

   ```streamlit run app.py```

## Conclusion
Proyek ini bertujuan untuk membantu Jaya Jaya Institut dalam mengidentifikasi mahasiswa yang berisiko tinggi mengalami dropout sejak dini. Dengan memanfaatkan pendekatan data science dan machine learning, institusi kini memiliki landasan analitis untuk memahami pola-pola yang terkait dengan kegagalan studi.

Beberapa kesimpulan utama yang diperoleh:
1. 

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
