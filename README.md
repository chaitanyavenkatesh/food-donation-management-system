# 🍲 Food Donation Management System

A Python-based desktop application built with **Tkinter** and **MySQL** to streamline food donation management. The system provides an intuitive GUI for admins to efficiently manage donors, food items, NGOs, and food distribution operations.

---

## ✨ Features

- 👥 **Donor Management** - Register and manage food donors
- 🥘 **Food Item Tracking** - Monitor available food items and quantities
- 🏢 **NGO Management** - Maintain NGO details and contact information
- 📦 **Distribution System** - Track food distribution to NGOs
- 🔐 **Secure Authentication** - Admin login system
- 💾 **Database Integration** - Persistent data storage with MySQL

---

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Tkinter** - GUI framework
- **MySQL** - Database management
- **mysql-connector-python** - MySQL database connector

---

## 📂 Project Structure
```
food-donation-management/
│
├── food_donation_app.py                    # Main application file
├── schema.sql                              # MySQL database schema
└── README.md                               # Project documentation
```

---

## 🔧 Prerequisites

Before running the project, ensure you have:

- Python 3.x installed ([Download Python](https://www.python.org/downloads/))
- MySQL Server installed ([Download MySQL](https://dev.mysql.com/downloads/))
- Basic knowledge of Python and MySQL

---

## 📥 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/food-donation-management.git
cd food-donation-management
```

### 2. Install Dependencies
```bash
pip install mysql-connector-python
```

Or using requirements.txt:
```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

### 1. Create Database

Open MySQL command line or MySQL Workbench and run:
```sql
CREATE DATABASE food_donation;
USE food_donation;
```

### 2. Import Schema

Import the database schema using one of these methods:

**Method 1: MySQL Command Line**
```bash
mysql -u root -p food_donation < database_schema.sql
```

**Method 2: MySQL Workbench**
- Open MySQL Workbench
- Select your connection
- Go to File → Run SQL Script
- Select `database_schema.sql`
- Execute

---

## ⚙️ Configuration

Update database credentials in `main.py`:
```python
# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "****",  # Change to your MySQL password
    "database": "food_donation"
}
```

---

## ▶️ Running the Application

Execute the main application file:
```bash
python main.py
```


## 🔮 Future Enhancements

- [ ] Multi-user role support (Admin, Volunteer, NGO)
- [ ] Email notifications for food distribution
- [ ] Reports and analytics dashboard
- [ ] Mobile application support
- [ ] Real-time inventory tracking
- [ ] Donation history and statistics

---

## 👤 Author

**Chaitanya Venkatesh**

- GitHub: [chaitanyavenkatesh](https://github.com/chaitanyavenkatesh)
- LinkedIn: [Chaitanya V](https://www.linkedin.com/in/chaitanya-v-531470363/)
- Email: chaitanyav2323@gmail.com
---

<div align="center">
  
### ⭐ If you find this project helpful, please consider giving it a star!

Made with ❤️ by Chaitanya Venkatesh

</div>

---
