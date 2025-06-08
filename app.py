import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Prediktor Status Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# --- PEMUATAN MODEL DAN SCALER ---
try:
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
except FileNotFoundError:
    st.error(
        "File 'model.pkl' atau 'scaler.pkl' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama.")
    st.stop()

# --- MAPPING DATA (Tidak diubah) ---
marital_status_map = {
    1: "Lajang", 2: "Menikah", 3: "Duda/Janda", 4: "Cerai", 5: "Kohabitasi", 6: "Pisah Hukum"
}
application_mode_map = {
    1: "Fase 1 - Umum", 2: "Peraturan 612/93", 5: "Khusus Azores", 7: "Lulusan PT lain",
    10: "Peraturan 854-B/99", 15: "Mahasiswa Internasional", 16: "Khusus Madeira",
    17: "Fase 2 - Umum", 18: "Fase 3 - Umum", 26: "Rencana Berbeda", 27: "Institusi Lain",
    39: "Usia >23 tahun", 42: "Transfer", 43: "Ganti jurusan", 44: "Spesialis Teknologi",
    51: "Ganti kampus/jurusan", 53: "Diploma Siklus Pendek", 57: "Transfer Internasional"
}
course_map = {
    33: "Biofuel", 171: "Desain Multimedia", 8014: "Sosial (malam)", 9003: "Agronomi",
    9070: "Desain Komunikasi", 9085: "Keperawatan Hewan", 9119: "Teknik Informatika",
    9130: "Ilmu Kuda", 9147: "Manajemen", 9238: "Pelayanan Sosial", 9254: "Pariwisata",
    9500: "Keperawatan", 9556: "Kebersihan Gigi", 9670: "Iklan & Marketing",
    9773: "Jurnalisme", 9853: "Pendidikan Dasar", 9991: "Manajemen (malam)"
}
nationality_map = {
    1: "Portugal", 2: "Jerman", 6: "Spanyol", 11: "Italia", 13: "Belanda", 14: "Inggris",
    17: "Lithuania", 21: "Angola", 22: "Cape Verde", 24: "Guinea", 25: "Mozambik",
    26: "Santome", 32: "Turki", 41: "Brasil", 62: "Romania", 100: "Moldova",
    101: "Meksiko", 103: "Ukraina", 105: "Rusia", 108: "Kuba", 109: "Kolombia"
}
mother_qual_map = {
    1: "Pendidikan Menengah - Tahun ke-12 atau Setara", 2: "Pendidikan Tinggi - Sarjana",
    3: "Pendidikan Tinggi - Gelar",
    4: "Pendidikan Tinggi - Master", 5: "Pendidikan Tinggi - Doktor", 6: "Frekuensi Pendidikan Tinggi",
    9: "Tahun ke-12 Sekolah - Tidak Selesai", 10: "Tahun ke-11 Sekolah - Tidak Selesai", 11: "Tahun ke-7 (Lama)",
    12: "Lainnya - Tahun ke-11 Sekolah", 14: "Tahun ke-10 Sekolah", 18: "Kursus dagang umum",
    19: "Pendidikan Dasar Siklus ke-3 (Tahun ke-9/10/11) atau Setara", 22: "Kursus teknis-profesional",
    26: "Tahun ke-7 sekolah", 27: "Siklus ke-2 kursus SMA umum", 29: "Tahun ke-9 Sekolah - Tidak Selesai",
    30: "Tahun ke-8 sekolah", 34: "Tidak Diketahui", 35: "Tidak bisa membaca atau menulis",
    36: "Bisa membaca tanpa memiliki ijazah tahun ke-4", 37: "Pendidikan Dasar Siklus ke-1 (Tahun ke-4/5) atau setara",
    38: "Pendidikan Dasar Siklus ke-2 (Tahun ke-6/7/8) atau Setara", 39: "Kursus spesialisasi teknologi",
    40: "Pendidikan Tinggi - gelar (siklus ke-1)", 41: "Kursus studi tinggi khusus",
    42: "Kursus teknis tinggi profesional",
    43: "Pendidikan Tinggi - Master (siklus ke-2)", 44: "Pendidikan Tinggi - Doktor (siklus ke-3)"
}
father_qual_map = mother_qual_map.copy()
father_qual_map.update({
    13: "Kursus SMA pelengkap tahun ke-2", 20: "Kursus SMA Pelengkap", 25: "Kursus SMA Pelengkap - tidak selesai",
    31: "Kursus Umum Administrasi dan Perdagangan", 33: "Akuntansi dan Administrasi Tambahan"
})

mother_occ_map = {
    0: "Mahasiswa", 1: "Manajer Legislatif/Eksekutif", 2: "Aktivitas Intelektual & Ilmiah",
    3: "Teknisi Menengah", 4: "Staf administrasi", 5: "Jasa Pribadi/Keamanan/Penjual",
    6: "Petani/Nelayan/Kehutanan", 7: "Pekerja Industri/Konstruksi", 8: "Operator Mesin",
    9: "Pekerja Tidak Terampil", 10: "Angkatan Bersenjata", 90: "Situasi Lain", 99: "(kosong)",
    122: "Tenaga kesehatan", 123: "Guru", 125: "Spesialis TIK",
    131: "Teknisi Sains/Teknik", 132: "Teknisi Kesehatan", 134: "Teknisi Hukum/Sosial/Budaya",
    141: "Sekretaris/Operator Data", 143: "Operator Keuangan/Registri", 144: "Dukungan Admin",
    151: "Pekerja Jasa", 152: "Penjual", 153: "Perawatan Pribadi", 171: "Pekerja Konstruksi",
    173: "Percetakan/Pengrajin", 175: "Pekerja Makanan/Tekstil/Kerajinan", 191: "Pekerja Kebersihan",
    192: "Pekerja Pertanian Tidak Terampil", 193: "Pekerja Industri Tidak Terampil", 194: "Asisten Persiapan Makanan"
}

father_occ_map = mother_occ_map.copy()
father_occ_map.update({
    101: "Perwira Angkatan Bersenjata", 102: "Sersan Angkatan Bersenjata", 103: "Angkatan Bersenjata Lainnya",
    112: "Direktur Admin/Komersial", 114: "Direktur Hotel/Katering", 121: "Spesialis Ilmu Fisika",
    124: "Spesialis Keuangan/Admin", 135: "Teknisi TIK", 154: "Jasa Keamanan",
    161: "Petani Pasar", 163: "Petani/Nelayan Subsisten", 172: "Pekerja Logam",
    174: "Pekerja Listrik", 181: "Operator Pabrik", 182: "Pekerja Perakitan",
    183: "Pengemudi", 195: "Pedagang Kaki Lima"
})

# --- UI APLIKASI (Tidak diubah) ---
st.title("🎓 Prediktor Status Kelulusan Mahasiswa")
st.caption(
    "Aplikasi ini menggunakan Machine Learning untuk memprediksi apakah seorang mahasiswa berisiko 'Dropout' atau akan 'Lulus' berdasarkan data sosio-demografis dan akademik.")
st.markdown("---")
with st.form("dropout_prediction_form"):
    tab1, tab2, tab3, tab4 = st.tabs(["👤 Data Pribadi", "👨‍👩‍👧 Latar Belakang", "📚 Akademik", "📈 Ekonomi"])
    with tab1:
        st.header("Informasi Pribadi & Pendaftaran")
        col1, col2 = st.columns(2)
        with col1:
            gender = st.radio("Jenis Kelamin", ["Wanita", "Pria"], horizontal=True)
            age_enroll = st.slider("Usia Saat Mendaftar", 17, 70, 20)
            marital_status = st.selectbox("Status Pernikahan", list(marital_status_map.keys()),
                                          format_func=lambda x: marital_status_map[x])
            nationality = st.selectbox("Kebangsaan", list(nationality_map.keys()),
                                       format_func=lambda x: nationality_map[x])
            international = st.radio("Mahasiswa Internasional?", [0, 1],
                                     format_func=lambda x: "Ya" if x == 1 else "Tidak", horizontal=True,
                                     help="Pilih 'Ya' jika bukan warga negara Portugal.")
        with col2:
            course = st.selectbox("Program Studi Pilihan", list(course_map.keys()), format_func=lambda x: course_map[x])
            application_mode = st.selectbox("Jalur Pendaftaran", list(application_mode_map.keys()),
                                            format_func=lambda x: application_mode_map[x])
            application_order = st.slider("Urutan Pilihan Prodi", 0, 9, 1,
                                          help="Urutan prioritas program studi saat mendaftar.")
            daytime_evening = st.radio("Waktu Kuliah", [1, 0],
                                       format_func=lambda x: "Pagi/Siang" if x == 1 else "Malam", horizontal=True)
    with tab2:
        st.header("Latar Belakang Keluarga & Kualifikasi Sebelumnya")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Kualifikasi Akademik")
            prev_qualification = st.number_input("Kode Kualifikasi Sebelumnya", min_value=1, max_value=43, value=1,
                                                 help="Input kode kualifikasi. Lihat 'Daftar Kode Kualifikasi' di bawah jika tidak yakin.")
            prev_qualification_grade = st.number_input("Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=200.0,
                                                       value=130.0)
            admission_grade = st.number_input("Nilai Tes Masuk", min_value=0.0, max_value=200.0, value=125.0,
                                              help="Nilai saat diterima di institusi.")
        with col2:
            st.subheader("Pendidikan & Pekerjaan Orang Tua")
            mother_qual_options = list(mother_qual_map.keys())
            mother_qual_default_index = mother_qual_options.index(34)
            mother_qual = st.selectbox("Pendidikan Terakhir Ibu", mother_qual_options,
                                       format_func=lambda x: f"{x} - {mother_qual_map[x]}",
                                       index=mother_qual_default_index)
            father_qual_options = list(father_qual_map.keys())
            father_qual_default_index = father_qual_options.index(34)
            father_qual = st.selectbox("Pendidikan Terakhir Ayah", father_qual_options,
                                       format_func=lambda x: f"{x} - {father_qual_map[x]}",
                                       index=father_qual_default_index)
            mother_occ = st.selectbox("Pekerjaan Ibu", list(mother_occ_map.keys()),
                                      format_func=lambda x: f"{x} - {mother_occ_map[x]}", index=12)
            father_occ = st.selectbox("Pekerjaan Ayah", list(father_occ_map.keys()),
                                      format_func=lambda x: f"{x} - {father_occ_map[x]}", index=12)
    with tab3:
        st.header("Informasi Perkuliahan per Semester")
        st.info("Isi data terkait jumlah SKS (Satuan Kredit Semester) dan nilai rata-rata untuk dua semester pertama.")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Semester 1")
            c1_credited = st.number_input("SKS Diakui (Sem 1)", min_value=0, value=0)
            c1_enrolled = st.number_input("SKS Diambil (Sem 1)", min_value=0, value=6)
            c1_approved = st.number_input("SKS Lulus (Sem 1)", min_value=0, value=6)
            c1_eval = st.number_input("Jumlah Evaluasi (Sem 1)", min_value=0, value=8)
            c1_grade = st.number_input("Nilai Rata-rata (Sem 1)", min_value=0.0, max_value=20.0, value=14.0)
            c1_wo_eval = st.number_input("SKS Tanpa Evaluasi (Sem 1)", min_value=0, value=0)
        with col2:
            st.subheader("Semester 2")
            c2_credited = st.number_input("SKS Diakui (Sem 2)", min_value=0, value=0)
            c2_enrolled = st.number_input("SKS Diambil (Sem 2)", min_value=0, value=6)
            c2_approved = st.number_input("SKS Lulus (Sem 2)", min_value=0, value=5)
            c2_eval = st.number_input("Jumlah Evaluasi (Sem 2)", min_value=0, value=9)
            c2_grade = st.number_input("Nilai Rata-rata (Sem 2)", min_value=0.0, max_value=20.0, value=13.0)
            c2_wo_eval = st.number_input("SKS Tanpa Evaluasi (Sem 2)", min_value=0, value=0)
    with tab4:
        st.header("Status Finansial & Ekonomi")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Status Mahasiswa")
            tuition_up_to_date = st.radio("Uang Kuliah Lunas?", [1, 0],
                                          format_func=lambda x: "Ya" if x == 1 else "Tidak", horizontal=True)
            debtor = st.radio("Memiliki Tunggakan?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak",
                              horizontal=True)
            scholarship = st.radio("Penerima Beasiswa?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak",
                                   horizontal=True)
            displaced = st.radio("Mahasiswa Pengungsi?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak",
                                 horizontal=True)
            special_needs = st.radio("Berkebutuhan Khusus?", [0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak",
                                     horizontal=True)
        with col2:
            st.subheader("Indikator Makroekonomi")
            unemployment = st.number_input("Tingkat Pengangguran (%)", min_value=-10.0, max_value=50.0, value=12.4)
            inflation = st.number_input("Tingkat Inflasi (%)", min_value=-10.0, max_value=50.0, value=0.5)
            gdp = st.number_input("Pertumbuhan GDP (%)", min_value=-20.0, max_value=20.0, value=1.79)
    st.markdown("---")
    submitted = st.form_submit_button("🔍 Lakukan Prediksi", use_container_width=True)

# --- BAGIAN YANG DIPERBAIKI ---
if submitted:
    input_dict = {
        'Marital_status': marital_status, 'Application_mode': application_mode,
        'Application_order': application_order, 'Course': course,
        'Daytime_evening_attendance': daytime_evening, 'Previous_qualification': prev_qualification,
        'Previous_qualification_grade': prev_qualification_grade, 'Nacionality': nationality,
        'Mothers_qualification': mother_qual, 'Fathers_qualification': father_qual,
        'Mothers_occupation': mother_occ, 'Fathers_occupation': father_occ,
        'Admission_grade': admission_grade, 'Displaced': displaced,
        'Educational_special_needs': special_needs, 'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_up_to_date, 'Gender': 1 if gender == "Pria" else 0,
        'Scholarship_holder': scholarship, 'Age_at_enrollment': age_enroll,
        'International': international, 'Curricular_units_1st_sem_credited': c1_credited,
        'Curricular_units_1st_sem_enrolled': c1_enrolled, 'Curricular_units_1st_sem_evaluations': c1_eval,
        'Curricular_units_1st_sem_approved': c1_approved, 'Curricular_units_1st_sem_grade': c1_grade,
        'Curricular_units_1st_sem_without_evaluations': c1_wo_eval,
        'Curricular_units_2nd_sem_credited': c2_credited, 'Curricular_units_2nd_sem_enrolled': c2_enrolled,
        'Curricular_units_2nd_sem_evaluations': c2_eval, 'Curricular_units_2nd_sem_approved': c2_approved,
        'Curricular_units_2nd_sem_grade': c2_grade,
        'Curricular_units_2nd_sem_without_evaluations': c2_wo_eval,
        'Unemployment_rate': unemployment, 'Inflation_rate': inflation, 'GDP': gdp
    }

    # Membuat DataFrame dari input
    df_input = pd.DataFrame([input_dict])

    # 1. Buat salinan DataFrame untuk diproses agar data asli tidak berubah
    df_processed = df_input.copy()

    # 2. Ambil daftar fitur numerik yang dikenali oleh scaler
    numerical_features = scaler.feature_names_in_

    # 3. Lakukan scaling HANYA pada fitur numerik
    df_processed[numerical_features] = scaler.transform(df_processed[numerical_features])

    # 4. Ambil urutan fitur yang benar dari model yang sudah dilatih
    model_feature_order = model.feature_name_

    # 5. Susun ulang DataFrame sesuai urutan yang diharapkan model
    final_df_for_prediction = df_processed[model_feature_order]

    # 6. Lakukan prediksi dengan data yang sudah siap
    prediction = model.predict(final_df_for_prediction)[0]
    prediction_proba = model.predict_proba(final_df_for_prediction)[0]

    status_map = {0: "Lulus", 1: "Dropout"}
    label = "Dropout" if prediction == 1 else "Graduate"
    probability = prediction_proba[prediction]

    # Menampilkan hasil
    st.markdown("---")
    st.header("✅ Hasil Prediksi")

    if label == "Dropout":
        st.error(f"**Status: {label}**", icon="⚠️")
        st.warning(f"Model memprediksi mahasiswa ini memiliki kecenderungan **{probability:.2%}** untuk **dropout**.")
        st.markdown(
            "**Rekomendasi:** Pertimbangkan untuk memberikan perhatian atau bimbingan khusus kepada mahasiswa ini untuk mengidentifikasi dan mengatasi potensi masalah yang dihadapi.")
    else:
        st.success(f"**Status: {label}**", icon="🎉")
        st.info(f"Model memprediksi mahasiswa ini memiliki probabilitas **{probability:.2%}** untuk dapat **lulus**.")
        st.markdown(
            "**Rekomendasi:** Mahasiswa berada di jalur yang tepat. Pertahankan dukungan dan fasilitas yang ada untuk memastikan kelancaran studinya.")

    with st.expander("Lihat Detail Data yang Anda Masukkan"):
        st.dataframe(pd.DataFrame([input_dict]))