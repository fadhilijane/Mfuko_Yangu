# MFUKO YANGU - Personal Banking App

MFUKO YANGU is a personal banking application designed to help you manage your finances with ease. The app provides features such as user registration, login, deposits, withdrawals, transfers, and transaction history.

## Features

- **User Registration and Login:** Secure authentication system with password hashing using bcrypt.
- **Dashboard:** View account balance and perform transactions.
- **Deposit and Withdraw:** Simple forms for adding or withdrawing funds.
- **Transfers:** Send money to other registered users.
- **Transaction History:** Detailed record of all transactions.

## Technology Stack

- **Backend:** Flask (Python)
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** HTML, CSS
- **Security:** Password hashing with bcrypt
- **Deployment:** DigitalOcean

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Mfuko_Yangu.git
   cd Mfuko_Yangu
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the application:**
   Open your browser and go to `http://127.0.0.1:5000`.

## Usage

- **Register:** Create a new user account.
- **Login:** Log in with your username and password.
- **Dashboard:** View your balance and perform deposits, withdrawals, transfers, and money requests.
- **Transaction History:** View a detailed list of all your transactions.

## File Structure

```
Mfuko_Yangu/
├── app.py
├── models.py
├── venv/
├── templates/
│   ├── base.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── transactions.html
│   ├── about.html
├── static/
│   └── styles.css
└── migrations/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch-name`.
5. Submit a pull request.

## Contact

For any questions or feedback, please contact [https://github.com/fadhilijane] at [janefadhili@gmail.com].

---

Thank you for using MFUKO YANGU!
```

Feel free to customize the README further to suit your specific needs.
