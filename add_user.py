from app import app, db, bcrypt, User

with app.app_context():
    # Define the recipient username and password
    username = 'recipient_username'  # Replace with desired recipient username
    password = 'recipient_password'  # Replace with desired recipient password

    # Check if the username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        print(f'User {username} already exists.')
    else:
        # Create a new user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, balance=100.0)  # Set an initial balance
        db.session.add(new_user)
        db.session.commit()
        print(f'User {username} added with initial balance of 100.0')

