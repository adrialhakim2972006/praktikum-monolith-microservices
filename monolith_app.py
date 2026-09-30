from flask import Flask, jsonify, request 
 
app = Flask(__name__) 
 
# Database bohongan (In-memory)
# Digunakan untuk menyimpan data buku selama program berjalan
books = [ 
    { 
        "id": 1, 
        "title": "Belajar Flask", 
        "stock": 5 
    } 
] 
 
# Menyimpan data pesanan yang dibuat oleh pengguna
orders = [] 
 
 
# ========================= 
# FITUR BUKU 
# ========================= 

# Route GET /books digunakan untuk menampilkan daftar buku
@app.route('/books', methods=['GET']) 
def get_books():
    # Mengembalikan data books dalam format JSON
    return jsonify(books) 
 
 
# ========================= 
# FITUR PESANAN 
# ========================= 

# Route POST /orders digunakan untuk membuat pesanan baru
@app.route('/orders', methods=['POST']) 
def create_order(): 
 
    # Mengambil data JSON yang dikirim oleh pengguna
    data = request.get_json()

    # Mengambil nilai book_id dari data pesanan
    book_id = data.get('book_id') 
 
    # Melakukan pengecekan terhadap data buku
    for b in books:

        # Mengecek ID buku dan memastikan stok masih tersedia
        if b['id'] == book_id and b['stock'] > 0: 
 
            # Mengurangi stok buku sebanyak 1 setelah dipesan
            b['stock'] -= 1 
 
            # Membuat data pesanan baru
            order = { 
                "id": len(orders) + 1, 
                "book_id": book_id, 
                "status": "berhasil" 
            } 
 
            # Menyimpan pesanan ke dalam daftar orders
            orders.append(order) 
 
            # Mengembalikan data pesanan dengan status berhasil
            return jsonify(order), 201 
 
    # Jika buku tidak ditemukan atau stok habis,
    # program mengembalikan pesan kesalahan
    return jsonify({ 
        "error": "Buku tidak ditemukan atau stok habis"
    }), 400 
 
 
if __name__ == '__main__':

    # Menjalankan aplikasi Flask pada port 5000
    app.run(port=5000, debug=True)