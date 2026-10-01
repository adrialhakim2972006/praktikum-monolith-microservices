# Praktikum Monolith vs Microservices dengan Flask Python

Praktikum ini merupakan implementasi sederhana arsitektur Monolith dan Microservices menggunakan Flask Python.

## Struktur Project

- `monolith_app.py` → Aplikasi dengan arsitektur Monolith
- `book_service.py` → Book Service pada arsitektur Microservices
- `order_service.py` → Order Service pada arsitektur Microservices

## Persiapan

Pastikan Python sudah terpasang pada komputer.

Install library yang diperlukan:

```bash
pip install Flask requests
```

Masuk ke folder project:

```cmd
cd /d "D:\Semester 5\Paradigma Sistem untuk TI\praktikum-monolith-microservices"
```

# 1. Arsitektur Monolith

Pada arsitektur Monolith, fitur buku dan pesanan berada dalam satu aplikasi Flask.

## 1.1 Menjalankan Aplikasi Monolith

Jalankan perintah:

```cmd
python monolith_app.py
```

Aplikasi berjalan pada:

```text
http://localhost:5000
```

## 1.2 Pengujian Daftar Buku

Buka terminal baru pada folder project, kemudian jalankan:

```cmd
curl.exe http://localhost:5000/books
```

Hasil yang diharapkan:

```json
[
    {
        "id": 1,
        "stock": 5,
        "title": "Belajar Flask"
    }
]
```

## 1.3 Pengujian Membuat Pesanan

Gunakan perintah:

```cmd
curl.exe -X POST http://localhost:5000/orders -H "Content-Type: application/json" -d "{\"book_id\":1}"
```

Hasil yang diharapkan:

```json
{
    "book_id": 1,
    "id": 1,
    "status": "berhasil"
}
```

## 1.4 Memeriksa Stok Setelah Pesanan

Jalankan kembali:

```cmd
curl.exe http://localhost:5000/books
```

Stok buku berubah dari `5` menjadi `4` karena pada arsitektur Monolith proses pembuatan pesanan sekaligus mengurangi stok buku.

# 2. Arsitektur Microservices

Pada arsitektur Microservices, aplikasi dibagi menjadi dua service:

- **Book Service**
- **Order Service**

Book Service bertanggung jawab terhadap data buku, sedangkan Order Service bertanggung jawab terhadap proses pemesanan.

## 2.1 Menjalankan Book Service

Buka terminal pertama pada folder project:

```cmd
python book_service.py
```

Book Service berjalan pada:

```text
http://localhost:5001
```

Biarkan terminal ini tetap berjalan.

## 2.2 Pengujian Daftar Buku

Buka terminal kedua pada folder project, kemudian jalankan:

```cmd
curl.exe http://localhost:5001/books
```

Hasil yang diharapkan:

```json
[
    {
        "id": 1,
        "stock": 5,
        "title": "Belajar Flask"
    }
]
```

## 2.3 Pengujian Detail Buku

Jalankan:

```cmd
curl.exe http://localhost:5001/books/1
```

Hasil yang diharapkan:

```json
{
    "id": 1,
    "stock": 5,
    "title": "Belajar Flask"
}
```

## 2.4 Menjalankan Order Service

Buka terminal ketiga pada folder project:

```cmd
python order_service.py
```

Order Service berjalan pada:

```text
http://localhost:5002
```

Biarkan Book Service dan Order Service tetap berjalan.

## 2.5 Pengujian Membuat Pesanan

Buka terminal baru dan jalankan:

```cmd
curl.exe -X POST http://localhost:5002/orders -H "Content-Type: application/json" -d "{\"book_id\":1}"
```

Hasil yang diharapkan:

```json
{
    "book_id": 1,
    "status": "berhasil"
}
```

Pada proses ini, Order Service meminta informasi buku kepada Book Service melalui HTTP/API sebelum membuat pesanan.

## 2.6 Memeriksa Stok Buku

Jalankan:

```cmd
curl.exe http://localhost:5001/books
```

Hasilnya tetap menunjukkan:

```json
[
    {
        "id": 1,
        "stock": 5,
        "title": "Belajar Flask"
    }
]
```

Stok tetap `5` karena implementasi Microservices pada praktikum ini belum memiliki proses untuk memperbarui stok pada Book Service.

# 3. Pengujian Fault Isolation

Pengujian ini dilakukan untuk melihat kondisi ketika Book Service mengalami gangguan.

## 3.1 Menghentikan Book Service

Pada terminal yang menjalankan Book Service, tekan:

```text
CTRL + C
```

Book Service akan berhenti.

Order Service tetap berjalan pada port `5002`.

## 3.2 Menguji Order Service Saat Book Service Down

Jalankan:

```cmd
curl.exe -X POST http://localhost:5002/orders -H "Content-Type: application/json" -d "{\"book_id\":1}"
```

Hasil yang diharapkan:

```json
{
    "error": "Book Service sedang down!"
}
```

Hasil tersebut menunjukkan bahwa Order Service tetap berjalan, tetapi proses pemesanan tidak dapat dilakukan karena Order Service tidak dapat berkomunikasi dengan Book Service.

# 4. Ringkasan

## Monolith

- Berjalan pada port `5000`.
- Fitur buku dan pesanan berada dalam satu aplikasi.
- Pesanan berhasil dibuat melalui endpoint `/orders`.
- Stok berkurang setelah pesanan berhasil dibuat.

## Microservices

- Book Service berjalan pada port `5001`.
- Order Service berjalan pada port `5002`.
- Book Service dan Order Service merupakan service yang terpisah.
- Komunikasi antarservice menggunakan HTTP/API.
- Order Service tetap berjalan ketika Book Service dihentikan.
- Pemesanan gagal ketika Book Service sedang down.

# Teknologi yang Digunakan

- Python
- Flask
- Requests
- Visual Studio Code
- Terminal
- Git
- GitHub
