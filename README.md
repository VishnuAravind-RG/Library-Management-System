# Library Management System (LMS)

![Library Management System](https://via.placeholder.com/800x400?text=Library+Management+System) <!-- Add actual image if available -->

## Overview

The Library Management System is a Python-based application with Oracle database integration that efficiently manages library operations. It provides a comprehensive solution for user management, catalog management, fee processing, and reporting through both console and GUI interfaces.

## Key Features

### Core Functionalities
- **User Management**: Full CRUD operations for library members
- **Catalog Management**: Complete book inventory control
- **Fee Processing**: Automated fee calculations and payment tracking
- **Acquisition Workflow**: End-to-end management of new book acquisitions

### Advanced Features
- **Dynamic Reporting**: Real-time analytics on library usage
- **Automated Notifications**: Overdue book alerts
- **Dual Interface**: Both console and graphical user interfaces

## Technology Stack

### Backend
- Python 3.x
- cx_Oracle for Oracle database connectivity
- Tkinter for GUI components

### Database
- Oracle Database (Version 19c or compatible)
- PL/SQL Procedures for business logic

## Installation Guide

### Prerequisites
1. Python 3.8+
2. Oracle Database (Tested with 19c)
3. Oracle Client Libraries
4. cx_Oracle package (`pip install cx_Oracle`)

### Database Configuration
1. Execute the provided SQL scripts to create:
   - Tables (Users, BookRecord, FeeStructure, etc.)
   - Stored procedures (InsertUser, UpdateBook, etc.)
   - Sequences and constraints

2. Configure the connection in `get_connection()` function:
```python
dsn = cx_Oracle.makedsn("your_host", "your_port", service_name="your_service")
connection = cx_Oracle.connect(user='your_username', password='your_password', dsn=dsn)
