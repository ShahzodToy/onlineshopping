# Online Shopping Platform

Welcome to the Online Shopping Platform! This project is a comprehensive e-commerce application built with Django. It allows users to browse products, add items to their cart, and manage their orders efficiently.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization
- Product catalog with categories and detailed views
- Shopping cart functionality
- Order management and checkout process
- Admin panel for managing products, orders, and users
- Responsive design for mobile and desktop views

## Installation

To get started with this project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShahzodToy/onlineshopping.git
   cd online-shopping-platform

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver