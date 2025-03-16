-- MySQL script to set up the database and table

CREATE DATABASE IF NOT EXISTS amazon_scraper;

USE amazon_scraper;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price VARCHAR(255) NOT NULL,
    reviews VARCHAR(255) NOT NULL,
    availability VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);