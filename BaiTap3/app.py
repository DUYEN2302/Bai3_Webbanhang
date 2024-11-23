import mysql.connector
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Mã hóa session

# Kết nối MySQL
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='kieuduyen',  # Thay đổi với tên người dùng của bạn
        password='admin123',  # Thay đổi với mật khẩu của bạn
        database='store_db'  # Thay đổi với tên database của bạn
    )

# Lấy danh sách sản phẩm từ MySQL
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')  # Thực thi câu lệnh SQL để lấy dữ liệu sản phẩm
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products_page():
    products = get_products()  # Lấy sản phẩm từ MySQL
    return render_template('products.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products WHERE id = %s', (product_id,))  # Lấy sản phẩm theo ID
    product = cursor.fetchone()
    cursor.close()
    conn.close()

    if product:
        # Kiểm tra xem giỏ hàng đã có sản phẩm này chưa
        if 'cart' not in session:
            session['cart'] = {}

        if product_id in session['cart']:
            session['cart'][product_id]['quantity'] += 1
        else:
            session['cart'][product_id] = {
                'name': product['name'],
                'price': product['price'],
                'image': product['image'],
                'quantity': 1
            }

        # Lưu giỏ hàng vào session
        session.modified = True
    
    return redirect(url_for('products_page'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    return render_template('cart.html', cart_items=cart_items)

if __name__ == '__main__':
    app.run(debug=True)
