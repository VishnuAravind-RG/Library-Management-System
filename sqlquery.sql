-- Create the database
CREATE DATABASE IF NOT EXISTS Library;

USE Library;

-- Create Member table
CREATE TABLE IF NOT EXISTS Member (
    MNO VARCHAR(20) PRIMARY KEY,
    Mname VARCHAR(100),
    Date_of_Membership DATE,
    Addr VARCHAR(255),
    Mob VARCHAR(15)
);

-- Create BookRecord table
CREATE TABLE IF NOT EXISTS BookRecord (
    BNO VARCHAR(20) PRIMARY KEY,
    BName VARCHAR(100),
    Auth VARCHAR(100),
    Price DECIMAL(10, 2),
    Publ VARCHAR(100)
);

-- Create Acquisitions table
CREATE TABLE IF NOT EXISTS Acquisitions (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    BNO VARCHAR(20),
    Status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (BNO) REFERENCES BookRecord(BNO)
);

-- Create Invoices table
CREATE TABLE IF NOT EXISTS Invoices (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    BNO VARCHAR(20),
    InvoiceNumber VARCHAR(50),
    InvoiceDate DATE,
    FOREIGN KEY (BNO) REFERENCES BookRecord(BNO)
);

-- Create FeeStructure table
CREATE TABLE IF NOT EXISTS FeeStructure (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FeeType VARCHAR(50),
    Amount DECIMAL(10, 2)
);

-- Create Payments table
CREATE TABLE IF NOT EXISTS Payments (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    MNO VARCHAR(20),
    Amount DECIMAL(10, 2),
    PaymentDate DATE,
    FOREIGN KEY (MNO) REFERENCES Member(MNO)
);

-- Create issue table to track book issuance
CREATE TABLE IF NOT EXISTS issue (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    BNO VARCHAR(20),
    MNO VARCHAR(20),
    d_o_issue DATE,
    d_o_ret DATE,
    FOREIGN KEY (BNO) REFERENCES BookRecord(BNO),
    FOREIGN KEY (MNO) REFERENCES Member(MNO)
);
