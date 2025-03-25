

-- Users Table (renamed from Member to match procedure references)
CREATE TABLE Users (
    MNO VARCHAR2(20) PRIMARY KEY,
    MNAME VARCHAR2(100),
    DOM DATE,  -- Changed from DATE_OF_MEMBERSHIP to match procedure parameter
    ADDR VARCHAR2(200),
    MOB VARCHAR2(15)
);

-- BookRecord Table
CREATE TABLE BookRecord (
    BNO VARCHAR2(20) PRIMARY KEY,
    BNAME VARCHAR2(100),
    AUTHOR VARCHAR2(100),  -- Changed from AUTH to match procedure parameter
    PRICE NUMBER(10, 2),
    PUBL VARCHAR2(100)
);

-- FeeStructure Table
CREATE TABLE FeeStructure (
    FEE_TYPE VARCHAR2(50) PRIMARY KEY,  -- Changed from FeeType to match procedure
    AMOUNT NUMBER(10, 2)
);

-- Payment Table (renamed from Payments to singular to match procedure)
CREATE TABLE Payment (
    PaymentID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    MNO VARCHAR2(20),
    AMOUNT NUMBER(10, 2),
    PAYMENT_DATE DATE,  -- Changed from PaymentDate to match procedure
    PAYMENT_METHOD VARCHAR2(50)  -- Added for RecordPaymentHistory procedure
);

-- Issue Table
CREATE TABLE Issue (
    IssueID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    MNO VARCHAR2(20),
    BNO VARCHAR2(20),
    ISSUE_DATE DATE,  -- Changed from d_o_issue to match procedure logic
    RETURN_DATE DATE,  -- Changed from d_o_ret to match procedure logic
    FOREIGN KEY (MNO) REFERENCES Users(MNO),
    FOREIGN KEY (BNO) REFERENCES BookRecord(BNO)
);

-- Acquisition Table (renamed from Acquisitions to singular)
CREATE TABLE Acquisition (
    ACQUISITION_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    BNO VARCHAR2(20),
    ACQ_DATE DATE,  -- Added for ReceiveGoods procedure
    STATUS VARCHAR2(20) CHECK(Status IN ('Pending', 'Received')),
    FOREIGN KEY (BNO) REFERENCES BookRecord(BNO)
);

-- Invoice Table (renamed from Invoices to singular)
CREATE TABLE Invoice (
    INVOICE_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    BNO VARCHAR2(20),
    INVOICE_NUMBER VARCHAR2(50),  -- Changed from InvoiceNumber to match procedure
    INVOICE_DATE DATE,  -- Changed from InvoiceDate to match procedure
    FOREIGN KEY (BNO) REFERENCES BookRecord(BNO)
);

-- FeeWaiver Table (renamed from FeeWaivers to singular)
CREATE TABLE FeeWaiver (
    WAIVER_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    MNO VARCHAR2(20),
    FEE_TYPE VARCHAR2(50),
    WAIVER_AMOUNT NUMBER(10, 2),
    REASON VARCHAR2(200),
    APPROVED_BY VARCHAR2(20),
    TIMESTAMP DATE,
    FOREIGN KEY (MNO) REFERENCES Users(MNO)
);

-- Refund Table (renamed from Refunds to singular)
CREATE TABLE Refund (
    REFUND_ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    PAYMENT_ID NUMBER,
    REFUND_AMOUNT NUMBER(10, 2),
    REASON VARCHAR2(200),
    APPROVED_BY VARCHAR2(20),
    TIMESTAMP DATE,
    FOREIGN KEY (PAYMENT_ID) REFERENCES Payment(PaymentID)
);

-- AuditTrails Table (unchanged but added for completeness)
CREATE TABLE AuditTrails (
    AuditID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    UserID VARCHAR2(20),
    ActivityType VARCHAR2(50),
    Timestamp DATE
);

-- Feedback Table (unchanged but added for completeness)
CREATE TABLE Feedback (
    FeedbackID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    UserID VARCHAR2(20),
    Message VARCHAR2(500),
    Timestamp DATE
);

-- SupportTickets Table (unchanged but added for completeness)
CREATE TABLE SupportTickets (
    TicketID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    UserID VARCHAR2(20),
    Issue VARCHAR2(500),
    Status VARCHAR2(20) CHECK(Status IN ('Open', 'In Progress', 'Resolved')),
    Timestamp DATE
);

-- Backups Table (unchanged but added for completeness)
CREATE TABLE Backups (
    BackupID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    BackupDate DATE,
    BackupFile VARCHAR2(200)
);
-- Insert User Procedure
CREATE OR REPLACE PROCEDURE InsertUser(
    p_mno IN VARCHAR2,
    p_mname IN VARCHAR2,
    p_dom IN DATE,
    p_addr IN VARCHAR2,
    p_mob IN VARCHAR2
) AS
BEGIN
    INSERT INTO Users (MNO, MNAME, DOM, ADDR, MOB)
    VALUES (p_mno, p_mname, p_dom, p_addr, p_mob);
END;
/

-- Update User Procedure
CREATE OR REPLACE PROCEDURE UpdateUser(
    p_mno IN VARCHAR2,
    p_mname IN VARCHAR2,
    p_dom IN DATE,
    p_addr IN VARCHAR2,
    p_mob IN VARCHAR2
) AS
BEGIN
    UPDATE Users
    SET MNAME = p_mname, DOM = p_dom, ADDR = p_addr, MOB = p_mob
    WHERE MNO = p_mno;
END;
/

-- Delete User Procedure
CREATE OR REPLACE PROCEDURE DeleteUser(
    p_mno IN VARCHAR2
) AS
BEGIN
    DELETE FROM Users WHERE MNO = p_mno;
END;
/

-- Search User Procedure
CREATE OR REPLACE PROCEDURE SearchUser(
    p_mno IN VARCHAR2,
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
    SELECT * FROM Users WHERE MNO = p_mno;
END;
/

-- Insert Book Procedure
CREATE OR REPLACE PROCEDURE InsertBook(
    p_bno IN VARCHAR2,
    p_bname IN VARCHAR2,
    p_auth IN VARCHAR2,
    p_price IN NUMBER,
    p_publ IN VARCHAR2
) AS
BEGIN
    INSERT INTO BookRecord (BNO, BNAME, AUTHOR, PRICE, PUBL)
    VALUES (p_bno, p_bname, p_auth, p_price, p_publ);
END;
/

-- Update Book Procedure
CREATE OR REPLACE PROCEDURE UpdateBook(
    p_bno IN VARCHAR2,
    p_bname IN VARCHAR2,
    p_auth IN VARCHAR2,
    p_price IN NUMBER,
    p_publ IN VARCHAR2
) AS
BEGIN
    UPDATE BookRecord
    SET BNAME = p_bname, AUTHOR = p_auth, PRICE = p_price, PUBL = p_publ
    WHERE BNO = p_bno;
END;
/

-- Delete Book Procedure
CREATE OR REPLACE PROCEDURE DeleteBook(
    p_bno IN VARCHAR2
) AS
BEGIN
    DELETE FROM BookRecord WHERE BNO = p_bno;
END;
/

-- Search Book Procedure
CREATE OR REPLACE PROCEDURE SearchBook(
    p_bno IN VARCHAR2,
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
    SELECT * FROM BookRecord WHERE BNO = p_bno;
END;
/

-- Add Fee Structure Procedure
CREATE OR REPLACE PROCEDURE AddFeeStructure(
    p_fee_type IN VARCHAR2,
    p_amount IN NUMBER
) AS
BEGIN
    INSERT INTO FeeStructure (FEE_TYPE, AMOUNT)
    VALUES (p_fee_type, p_amount);
END;
/

-- Record Payment Procedure
CREATE OR REPLACE PROCEDURE RecordPayment(
    p_mno IN VARCHAR2,
    p_amount IN NUMBER
) AS
BEGIN
    INSERT INTO Payment (MNO, AMOUNT)
    VALUES (p_mno, p_amount);
END;
/

-- Calculate Fine Function
CREATE OR REPLACE FUNCTION CalculateFine(
    p_mno IN VARCHAR2
) RETURN NUMBER AS
    v_fine NUMBER := 0;
BEGIN
    SELECT SUM(10) INTO v_fine -- Example: $10 fine per overdue book
    FROM Issue
    WHERE MNO = p_mno AND RETURN_DATE IS NULL AND SYSDATE > ISSUE_DATE + 30;
    RETURN v_fine;
END;
/

-- Most Popular Books Procedure
CREATE OR REPLACE PROCEDURE MostPopularBooks(
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
    SELECT BNO, BNAME, COUNT(*) AS ISSUE_COUNT
    FROM Issue
    GROUP BY BNO, BNAME
    ORDER BY ISSUE_COUNT DESC;
END;
/

-- Most Active Members Procedure
CREATE OR REPLACE PROCEDURE MostActiveMembers(
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
    SELECT MNO, MNAME, COUNT(*) AS ISSUE_COUNT
    FROM Issue
    JOIN Users ON Issue.MNO = Users.MNO
    GROUP BY MNO, MNAME
    ORDER BY ISSUE_COUNT DESC;
END;
/

-- Books Issued Last Month Procedure
CREATE OR REPLACE PROCEDURE BooksIssuedLastMonth(
    p_cursor OUT SYS_REFCURSOR
) AS
BEGIN
    OPEN p_cursor FOR
    SELECT BNO, BNAME
    FROM Issue
    JOIN BookRecord ON Issue.BNO = BookRecord.BNO
    WHERE ISSUE_DATE >= ADD_MONTHS(SYSDATE, -1);
END;
/

-- Notify Overdue Books Procedure
CREATE OR REPLACE PROCEDURE NotifyOverdueBooks AS
BEGIN
    FOR rec IN (SELECT MNO, BNO FROM Issue WHERE RETURN_DATE IS NULL AND SYSDATE > ISSUE_DATE + 30) LOOP
        DBMS_OUTPUT.PUT_LINE('Notifying Member ' || rec.MNO || ' about overdue book ' || rec.BNO);
    END LOOP;
END;
/

-- Add Acquisition Procedure
CREATE OR REPLACE PROCEDURE AddAcquisition(
    p_bno IN VARCHAR2
) AS
BEGIN
    INSERT INTO Acquisition (BNO)
    VALUES (p_bno);
END;
/

-- Receive Goods Procedure
CREATE OR REPLACE PROCEDURE ReceiveGoods(
    p_bno IN VARCHAR2
) AS
BEGIN
    UPDATE Acquisition
    SET ACQ_DATE = SYSDATE
    WHERE BNO = p_bno;
END;
/

-- Process Invoice Procedure
CREATE OR REPLACE PROCEDURE ProcessInvoice(
    p_bno IN VARCHAR2,
    p_invoice_number IN VARCHAR2,
    p_invoice_date IN DATE
) AS
BEGIN
    INSERT INTO Invoice (BNO, INVOICE_NUMBER, INVOICE_DATE)
    VALUES (p_bno, p_invoice_number, p_invoice_date);
END;
/

-- Add Fee Waiver Procedure
CREATE OR REPLACE PROCEDURE AddFeeWaiver(
    p_mno IN VARCHAR2,
    p_fee_type IN VARCHAR2,
    p_waiver_amount IN NUMBER,
    p_reason IN VARCHAR2,
    p_approved_by IN VARCHAR2
) AS
BEGIN
    INSERT INTO FeeWaiver (MNO, FEE_TYPE, WAIVER_AMOUNT, REASON, APPROVED_BY)
    VALUES (p_mno, p_fee_type, p_waiver_amount, p_reason, p_approved_by);
END;
/

-- Record Payment History Procedure
CREATE OR REPLACE PROCEDURE RecordPaymentHistory(
    p_mno IN VARCHAR2,
    p_amount IN NUMBER,
    p_payment_method IN VARCHAR2
) AS
BEGIN
    INSERT INTO Payment (MNO, AMOUNT, PAYMENT_METHOD)
    VALUES (p_mno, p_amount, p_payment_method);
END;
/

-- Process Refund Procedure
CREATE OR REPLACE PROCEDURE ProcessRefund(
    p_payment_id IN NUMBER,
    p_refund_amount IN NUMBER,
    p_reason IN VARCHAR2,
    p_approved_by IN VARCHAR2
) AS
BEGIN
    INSERT INTO Refund (PAYMENT_ID, REFUND_AMOUNT, REASON, APPROVED_BY)
    VALUES (p_payment_id, p_refund_amount, p_reason, p_approved_by);
END;
/
