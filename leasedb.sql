-- leasedb.sql
CREATE DATABASE IF NOT EXISTS leasedb;
USE leasedb;

CREATE TABLE IF NOT EXISTS leases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    clauses TEXT NOT NULL
);


