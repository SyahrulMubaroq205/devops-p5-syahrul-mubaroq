# Simple Asset Inventory API

Simple Asset Inventory API adalah aplikasi sederhana berbasis Python untuk melakukan registrasi aset, menampilkan daftar aset, dan memperbarui kondisi aset. Proyek ini dibuat sebagai penerapan pembelajaran DevSecOps dengan mengintegrasikan pengujian otomatis dan pemindaian keamanan ke dalam pipeline CI/CD.

## Teknologi yang Digunakan

- **Python 3.12** sebagai bahasa pemrograman utama.
- **pytest** untuk menjalankan pengujian unit.
- **Bandit** untuk melakukan Static Application Security Testing (SAST) pada kode Python.
- **SonarQube Community Build** untuk menganalisis kualitas kode dan mengevaluasi Quality Gate.
- **GitHub Actions** untuk mengotomatisasi pengujian dan pemindaian keamanan.

## Fitur Aplikasi

- Mendaftarkan aset dengan informasi nama, lokasi, dan kondisi.
- Menampilkan daftar aset yang telah didaftarkan.
- Memperbarui kondisi aset yang sudah terdaftar.
- Memvalidasi data masukan, termasuk nama aset, lokasi, dan kondisi yang diperbolehkan.

## Cara Menjalankan Aplikasi

Pastikan Python 3.12 telah terpasang. Buka terminal pada direktori proyek, kemudian jalankan:

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

Pasang dependensi:

```bash
python -m pip install -r requirements.txt
```

Jalankan aplikasi:

```bash
python -m app.main
```

## Menjalankan Pengujian dan Pemindaian Keamanan

Untuk menjalankan unit test:

```bash
python -m pytest -v
```

Untuk melakukan pemindaian keamanan menggunakan Bandit:

```bash
bandit -r app -ll
```

Perintah Bandit tersebut memeriksa kode di direktori `app` dengan ambang pelaporan tingkat keparahan Low ke atas dan tingkat kepercayaan default Bandit. Pada pipeline, opsi `-ll` membuat temuan berkeparahan Medium dan High dapat menyebabkan job gagal.

## Gambaran Pipeline CI/CD

Pipeline DevSecOps menggunakan GitHub Actions dan dikonfigurasi melalui dua file workflow.

### 1. Build, Unit Test, dan SAST

File: `.github/workflows/devsecops.yml`

Workflow ini berjalan ketika terdapat push ke branch `main` atau pull request yang ditujukan ke branch `main`. Pipeline terdiri dari dua job:

- **`build`**: memasang dependensi dan menjalankan unit test menggunakan pytest.
- **`sast-scan`**: dijalankan setelah job `build` berhasil, kemudian memindai kode menggunakan Bandit.

Workflow ini menggunakan runner `ubuntu-latest` yang disediakan oleh GitHub Actions.

### 2. Analisis SonarQube

File: `.github/workflows/sonarqube-local.yml`

Workflow ini berjalan ketika terdapat push ke branch `main`. Job analisis menggunakan runner `self-hosted` pada komputer lokal yang terhubung ke GitHub. Runner tersebut menjalankan SonarScanner melalui Docker untuk mengirim hasil analisis ke SonarQube Community Build yang berjalan secara lokal.

Workflow menunggu hasil Quality Gate SonarQube. Jika analisis gagal atau Quality Gate tidak terpenuhi, job akan berstatus gagal.

Integrasi ini membutuhkan Docker, layanan SonarQube lokal yang aktif, runner yang sedang berjalan, dan GitHub Actions secret `SONAR_TOKEN` yang valid.

## Quality Gate

Proyek ini menerapkan dua pemeriksaan kualitas dan keamanan kode:

- **Bandit:** job SAST dinyatakan berhasil apabila tidak ditemukan temuan dengan tingkat keparahan Medium atau High pada direktori `app`.
- **SonarQube:** job analisis menunggu hasil Quality Gate dari server SonarQube. Status lulus atau gagal mengikuti hasil pemeriksaan yang dikonfigurasi pada server tersebut.

Pada analisis terbaru yang dilakukan pada 18 Oktober 2026, dashboard SonarQube menunjukkan status **Quality Gate Passed** dengan 0 new issues dan 0 security hotspots. Hasil tersebut merupakan hasil analisis pada saat pengujian dilakukan, bukan jaminan bahwa aplikasi bebas dari seluruh kerentanan keamanan.

## Kesimpulan

Penerapan pipeline DevSecOps pada Simple Asset Inventory API membantu mengotomatisasi pengujian unit, pemindaian keamanan statis menggunakan Bandit, dan analisis kualitas kode menggunakan SonarQube. Integrasi ini membantu mendeteksi masalah sejak tahap pengembangan dan memberikan pemeriksaan yang konsisten setiap kali perubahan kode dikirim ke repository.
