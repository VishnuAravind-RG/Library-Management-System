# Library Management System

## Overview
The Library Management System (LMS) is a comprehensive software application designed to manage the operations of a library effectively. It provides functionalities for managing users, books, acquisitions, fees, and dynamic reporting. The system aims to streamline library processes and enhance user interaction.

## Features

### User Management
- Add, update, delete, and search for library members.
- Notify users about overdue books.

### Catalog Management
- Add, update, delete, and search for books in the library catalog.

### Acquisition Management
- Manage the acquisition of new books and resources.
- Record the receipt of goods and process invoices.

### Fee Management
- Manage membership fees and track payments.
- Automatically calculate fines for overdue books.

### Dynamic Reporting
- Generate reports on:
  - Most popular books.
  - Most active members.
  - Books issued in the last month.
  - Overdue books and fines.

### Enhanced User Interactivity
- Real-time notifications for overdue books.
- Interactive help menu for user guidance.
- User profiles to view borrowing history.

## Technologies Used
- Python
- MySQL (Database)
- MySQL Connector/Python

## Installation

### Prerequisites
1. Python 3.x installed on your machine.
2. MySQL Server installed and running.
3. MySQL Connector/Python library installed. You can install it using pip:


### Database Setup
1. Create a database named `Library` in MySQL.
2. Execute the SQL scripts provided in the code to create the required tables:
- `Member`
- `BookRecord`
- `Acquisitions`
- `Invoices`
- `FeeStructure`
- `Payments`
- `issue`

### Running the Application
1. Clone this repository:


## Usage
Follow the on-screen prompts to navigate through different functionalities of the system. The main menu allows you to choose between user management, catalog management, acquisition management, fee management, dynamic reporting, and exiting the application.

## Contribution
Contributions are welcome! If you have suggestions or improvements, please feel free to create a pull request or open an issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to all contributors and libraries that made this project possible!

