Library Management System (LMS) Documentation
Overview
The Library Management System is a Python-based application with Oracle database integration that efficiently manages library operations. It provides a comprehensive solution for user management, catalog management, fee processing, and reporting through both console and GUI interfaces.

Key Features
Core Functionalities
User Management: Full CRUD operations for library members

Catalog Management: Complete book inventory control

Fee Processing: Automated fee calculations and payment tracking

Acquisition Workflow: End-to-end management of new book acquisitions

Advanced Features
Dynamic Reporting: Real-time analytics on library usage

Automated Notifications: Overdue book alerts

Dual Interface: Both console and graphical user interfaces

Technology Stack
Backend
Python 3.x

cx_Oracle for Oracle database connectivity

Tkinter for GUI components

Database
Oracle Database (Version 19c or compatible)

PL/SQL Procedures for business logic

Installation Guide
Prerequisites
Python 3.8+

Oracle Database (Tested with 19c)

Oracle Client Libraries

cx_Oracle package (pip install cx_Oracle)

Database Configuration
Execute the provided SQL scripts to create:

Tables (Users, BookRecord, FeeStructure, etc.)

Stored procedures (InsertUser, UpdateBook, etc.)

Sequences and constraints

Configure the connection in get_connection() function:

python
Copy
dsn = cx_Oracle.makedsn("your_host", "your_port", service_name="your_service")
connection = cx_Oracle.connect(user='your_username', password='your_password', dsn=dsn)
System Architecture
Database Schema
Users: Member information (MNO, MNAME, DOM, ADDR, MOB)

BookRecord: Book inventory (BNO, BNAME, AUTHOR, PRICE, PUBL)

FeeStructure: Fee configurations (FEE_TYPE, AMOUNT)

Payments: Transaction records (PAYMENT_ID, MNO, AMOUNT, PAYMENT_DATE)

Application Layers
Presentation Layer: Console menus and Tkinter GUI

Business Logic Layer: Python functions and Oracle stored procedures

Data Access Layer: cx_Oracle connection handlers

Usage Guide
Console Interface
Navigate through hierarchical menus:

Main Menu → User Management → [Sub-options]

All operations feature input validation and error recovery

GUI Interface
Accessible through main menu option 8:

Login with credentials (admin/password)

Search functionality with real-time results

Theme customization (light/dark mode)

Error Handling System
The application implements comprehensive error handling:

Database constraint violations

Input validation failures

Connection issues

Business logic exceptions

All errors provide:

Clear user-friendly messages

Context-specific recovery options

Detailed logging

Reporting Module
Generate valuable insights:

Popularity Analytics: Most issued books

Member Activity: Frequent borrowers

Temporal Analysis: Recent checkouts

Financial Reports: Fee collections

