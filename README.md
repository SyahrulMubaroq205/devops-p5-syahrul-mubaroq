# Simple Asset Inventory API

Simple Asset Inventory API adalah aplikasi sederhana berbasis Python yang digunakan untuk melakukan registrasi aset, menampilkan daftar aset, dan memperbarui kondisi aset. Aplikasi ini dibuat sebagai proyek pembelajaran untuk penerapan pipeline DevSecOps.

## Teknologi yang Digunakan

- **Python 3.12** sebagai bahasa pemrograman utama.
- **pytest** untuk menjalankan pengujian unit.
- **Bandit** sebagai alat Static Application Security Testing (SAST) untuk mendeteksi potensi masalah keamanan pada kode Python.
- **GitHub Actions** untuk menjalankan proses build, pengujian, dan pemindaian keamanan secara otomatis.

## Fitur Aplikasi

- Mendaftarkan aset dengan informasi nama, lokasi, dan kondisi.
- Menampilkan daftar aset yang telah didaftarkan.
- Memperbarui kondisi aset yang sudah terdaftar.
- Memvalidasi data masukan, termasuk nama aset, lokasi, dan kondisi yang diperbolehkan.

## Cara Menjalankan Aplikasi

Pastikan Python 3.12 telah terpasang. Buka terminal pada direktori proyek, kemudian jalankan perintah berikut:

```bash
python -m venv .venv
```

Aktifkan virtual environment sesuai sistem operasi yang digunakan.

**Linux / WSL:**

```bash
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

Setelah virtual environment aktif, pasang dependensi dan jalankan aplikasi:

```bash
pip install -r requirements.txt
python -m app.main
```

## Menjalankan Pengujian dan Pemindaian Keamanan

Untuk menjalankan unit test, gunakan perintah:

```bash
python -m pytest -v
```

Untuk melakukan pemindaian keamanan menggunakan Bandit, jalankan:

```bash
bandit -r app -ll
```

## Gambaran Pipeline CI/CD

Pipeline DevSecOps dikonfigurasi melalui file `.github/workflows/devsecops.yml` dan dijalankan secara otomatis ketika terdapat push ke branch `main` atau pull request yang ditujukan ke branch `main`.

Pipeline terdiri dari dua job utama. Job `build` bertugas memasang dependensi dan menjalankan unit test untuk memastikan fungsi aplikasi berjalan sesuai harapan. Setelah job tersebut berhasil, job `sast-scan` dijalankan untuk memeriksa potensi masalah keamanan menggunakan Bandit.

Pipeline menggunakan runner `ubuntu-latest` yang disediakan oleh GitHub Actions. Dengan demikian, proses build, pengujian, dan pemindaian keamanan dapat dijalankan di lingkungan cloud tanpa harus memasang Ubuntu dengan versi yang sama pada komputer lokal.

## Quality Gate

Quality Gate digunakan sebagai kriteria untuk menentukan apakah pipeline dapat dinyatakan berhasil. Pada proyek ini, pipeline dinyatakan lulus apabila seluruh unit test berhasil dijalankan dan Bandit tidak menemukan masalah keamanan dengan tingkat keparahan Medium atau High pada direktori `app/`.

Apabila unit test gagal atau pemindaian Bandit menemukan masalah yang memenuhi ambang batas tersebut, pipeline akan berstatus gagal. Aturan ini diterapkan untuk membantu menjaga kualitas kode dan mendeteksi potensi risiko keamanan sejak tahap pengembangan.