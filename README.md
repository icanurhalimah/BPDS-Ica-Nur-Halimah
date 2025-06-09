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
Sebagai bagian dari proyek prediksi dropout mahasiswa di Jaya Jaya Institut, telah dibuat sebuah **dashboard interaktif** menggunakan **Google Looker Studio**. Dashboard ini berfungsi sebagai alat bantu visualisasi data yang memudahkan tim akademik dan manajemen dalam memantau tren dropout serta melakukan intervensi berbasis data.

<img src="https://github.com/user-attachments/assets/59ffdf5b-e51f-4855-b384-aa49c2e28779" alt="Dashboard" title="Dashboard">

### Tujuan Dashboard
- Menyediakan **gambaran visual menyeluruh** tentang status akhir mahasiswa.
- Membantu **mengidentifikasi pola dropout** berdasarkan berbagai faktor.
- Mempermudah pengambilan keputusan dalam strategi **retensi mahasiswa**.

### Fitur-Fitur Utama

1. **Dropdown Filter**  
   Pengguna dapat memfilter tampilan data berdasarkan variabel penting seperti:
   - Gender
   - Marital Status
   - Status Debtor (utang pendidikan)

2. **Visualisasi Dropout Berdasarkan Faktor-Faktor Penting**  
   - **Dropout Rate by Status**: Distribusi jumlah mahasiswa yang lulus, dropout, dan masih aktif.
   - **Dropout by Age at Enrollment**: Menunjukkan bahwa mahasiswa berusia muda (18–24 tahun) memiliki angka dropout yang tinggi.
   - **Dropout by Course**: Diagram pie yang menyoroti jurusan dengan tingkat dropout tertinggi.
   - **Dropout by Application Order**: Mayoritas dropout berasal dari mahasiswa yang menempatkan program studi tersebut sebagai pilihan utama.
   - **Status by Scholarship and Debtor**: Tabel komparatif status akhir mahasiswa berdasarkan status beasiswa dan utang.
   - **Dropout by Curricular Units Evaluations**: Mahasiswa yang tidak aktif mengikuti evaluasi semester 1 cenderung lebih berisiko dropout.
   - **Heatmap by Age at Enrollment**: Visualisasi intensitas dropout per kelompok usia.

### Akses Dashboard
Dashboard ini dibuat menggunakan **Google Looker Studio** dan dapat diakses secara online melalui tautan berikut:

**[Tautan Looker Studio](https://lookerstudio.google.com/reporting/590c356b-ef78-4ff7-9688-a6c2a51417a1/page/2mPNF)**

Dashboard ini diharapkan menjadi alat bantu penting dalam **transformasi digital bidang akademik**, memungkinkan pengambilan kebijakan yang **lebih cepat, tepat, dan berbasis data real-time**.

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

Proyek ini berhasil membuktikan bahwa pendekatan berbasis data science dapat digunakan secara efektif untuk membantu institusi pendidikan mendeteksi risiko mahasiswa yang berpotensi mengalami dropout sejak dini.

Beberapa poin kesimpulan utama:

1. **Model klasifikasi yang dibangun (LightGBM)** mampu mengidentifikasi mahasiswa dropout dengan tingkat akurasi yang baik, serta menyoroti fitur-fitur kunci seperti nilai semester awal, usia saat masuk, status keuangan, dan aktivitas perkuliahan.

2. **Dashboard interaktif berbasis Looker Studio** memungkinkan visualisasi tren dropout secara real-time dan dapat digunakan oleh pihak akademik tanpa latar belakang teknis yang kuat.

3. Institusi kini memiliki **alat bantu pengambilan keputusan berbasis data** yang bisa dimanfaatkan untuk:
   - Memberikan bimbingan akademik secara tepat sasaran,
   - Menyusun kebijakan pembinaan dan intervensi dini,
   - Meningkatkan efisiensi alokasi sumber daya,
   - Meningkatkan angka kelulusan dan citra institusi secara keseluruhan.

4. Proyek ini membuka peluang untuk pengembangan lanjutan, seperti integrasi ke sistem informasi akademik kampus dan penerapan sistem peringatan dini berbasis model prediktif.

Dengan ini, Jaya Jaya Institut mengambil langkah maju dalam **transformasi digital pendidikan** untuk membangun ekosistem akademik yang lebih adaptif, prediktif, dan proaktif.

### Rekomendasi Action Items
Berikut beberapa rekomendasi strategis yang dapat dilakukan oleh Jaya Jaya Institut untuk menindaklanjuti hasil proyek dan mengatasi permasalahan dropout mahasiswa:

- **Action Item 1: Implementasi Sistem Prediksi Dropout di Sistem Akademik**  
  Integrasikan model machine learning ke dalam sistem informasi akademik kampus (SIAKAD) untuk mendeteksi mahasiswa berisiko tinggi secara otomatis setiap awal semester.

- **Action Item 2: Buat Program Intervensi Khusus bagi Mahasiswa Berisiko**  
  Sediakan program pendampingan akademik dan psikologis, seperti mentoring, konseling, atau kelas remedial bagi mahasiswa yang terdeteksi berisiko tinggi berdasarkan output model.

- **Action Item 3: Monitoring dan Evaluasi Berkala Melalui Dashboard**  
  Gunakan dashboard Looker Studio secara aktif dalam rapat akademik untuk memantau perkembangan dropout secara real-time dan mengambil kebijakan berbasis data.

- **Action Item 4: Penguatan Sosialisasi dan Orientasi Mahasiswa Baru**  
  Berikan program orientasi yang lebih intensif kepada mahasiswa baru untuk memperkuat kesiapan akademik dan sosial, khususnya bagi mahasiswa dengan profil risiko tinggi.

- **Action Item 5: Kolaborasi Antara Bagian Akademik dan Biro Kemahasiswaan**  
  Bentuk tim lintas unit untuk menindaklanjuti output sistem prediksi dengan cepat dan menyusun strategi intervensi berbasis latar belakang individual mahasiswa.

- **Action Item 6: Evaluasi dan Pelatihan Berbasis Data untuk Dosen Wali**  
  Libatkan dosen wali dalam pelatihan analisis data sederhana dan cara membaca output sistem prediksi untuk meningkatkan efektivitas pendampingan akademik.
