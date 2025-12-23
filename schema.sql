-- Food Donation Management System Database Schema

CREATE DATABASE IF NOT EXISTS food_donation;
USE food_donation;

-- Donors Table
CREATE TABLE IF NOT EXISTS Donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Food Table
CREATE TABLE IF NOT EXISTS Food (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT NOT NULL,
    food_type VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    expiry_date DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'Available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (donor_id) REFERENCES Donors(donor_id) ON DELETE CASCADE
);

-- NGOs Table
CREATE TABLE IF NOT EXISTS NGOs (
    ngo_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Distribution Table
CREATE TABLE IF NOT EXISTS Distribution (
    distribution_id INT AUTO_INCREMENT PRIMARY KEY,
    ngo_id INT NOT NULL,
    food_id INT NOT NULL,
    distribution_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ngo_id) REFERENCES NGOs(ngo_id) ON DELETE CASCADE,
    FOREIGN KEY (food_id) REFERENCES Food(food_id) ON DELETE CASCADE
);

-- Create Indexes for better query performance
CREATE INDEX idx_donor_id ON Food(donor_id);
CREATE INDEX idx_ngo_id ON Distribution(ngo_id);
CREATE INDEX idx_food_id ON Distribution(food_id);
CREATE INDEX idx_status ON Food(status);
CREATE INDEX idx_expiry_date ON Food(expiry_date);
