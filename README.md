# Library Management System (LMS)

<!-- Add actual image if available -->

## Overview

The Library Management System is a Python-based application integrated with an Oracle database to streamline library operations. It offers a robust solution for managing users, books, fines, and reporting through a console-based interface, with audit logging for tracking system activities.

## Key Features

### Core Functionalities
- **User Management**: Create, update, delete, and search library members.
- **Catalog Management**: Add, modify, remove, and search books in the inventory.
- **Fine Processing**: Calculate overdue fines, process payments, and view fine history.
- **Issue Management**: Issue books to members with a cart-based system and track due dates.

### Advanced Features
- **Dynamic Reporting**: Generate reports on popular books, active members, and recent issues.
- **Audit Logging**: Track all significant actions (e.g., insertions, updates, deletions) with user IDs and timestamps.
- **Console Interface**: Interactive command-line interface for all operations.

## Technology Stack

### Backend
- Python 3.x
- `cx_Oracle` for Oracle database connectivity

### Database
- Oracle Database (Version 19c or compatible)
- PL/SQL Procedures for business logic

## Installation Guide

### Prerequisites
1. **Python 3.8+**: Ensure Python is installed on your system.
2. **Oracle Database**: Tested with Oracle 19c; other compatible versions may work.
3. **Oracle Client Libraries**: Install Oracle Instant Client and configure it in your environment.
4. **cx_Oracle Package**: Install via pip:
   ```bash
   pip install cx_Oracle
