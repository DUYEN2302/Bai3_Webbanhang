CREATE USER 'kieuduyen'@'localhost' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON *.* TO 'kieuduyen'@'localhost';
FLUSH PRIVILEGES;
show databases;
CREATE DATABASE IF NOT EXISTS store_db;

USE store_db;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    description TEXT
);

-- Thêm vài sản phẩm mẫu
INSERT INTO products (name, price, image, description)
VALUES('Sản phẩm 1', '300.000 VND', 'product1.jpg', 'vải thoáng mát'),('Sản phẩm 2', '400.000 VND', 'product2.jpg', 'vải ấm'),('Sản phẩm 3', '500.000 VND', 'product3.jpg', 'năng động, trẻ trung');

