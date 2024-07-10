from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_migrate import Migrate
from models import db, bcrypt, User, Transaction

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect("https://mfukoyangubanking.pages.dev/#")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))
        
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', transactions=transactions, balance=current_user.balance)

@app.route('/deposit', methods=['POST'])
@login_required
def deposit():
    amount = float(request.form['amount'])
    current_user.balance += amount
    transaction = Transaction(user_id=current_user.id, amount=amount, type='deposit')
    db.session.add(transaction)
    db.session.commit()
    flash('Deposit successful!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/withdraw', methods=['POST'])
@login_required
def withdraw():
    amount = float(request.form['amount'])
    if current_user.balance >= amount:
        current_user.balance -= amount
        transaction = Transaction(user_id=current_user.id, amount=amount, type='withdrawal')
        db.session.add(transaction)
        db.session.commit()
        flash('Withdrawal successful!', 'success')
    else:
        flash('Insufficient balance for withdrawal.', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/transfer', methods=['POST'])
@login_required
def transfer():
    recipient_username = request.form['recipient']
    amount = float(request.form['amount'])
    recipient = User.query.filter_by(username=recipient_username).first()
    if recipient and current_user.balance >= amount:
        current_user.balance -= amount
        recipient.balance += amount
        transaction = Transaction(user_id=current_user.id, amount=amount, type='transfer', recipient_id=recipient.id)
        db.session.add(transaction)
        db.session.commit()
        flash('Transfer successful!', 'success')
    else:
        flash('Transfer failed. Check recipient username and your balance.', 'danger')
    return redirect(url_for('dashboard'))

@app.route('/request_money', methods=['POST'])
@login_required
def request_money():
    amount = float(request.form['amount'])
    message = request.form['message']
    transaction = Transaction(user_id=current_user.id, amount=amount, type='request', recipient_id=None, message=message)
    db.session.add(transaction)
    db.session.commit()
    flash('Money request sent!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)

