from app import db, User, Transaction

with app.app_context():
    user = User.query.first()
    transactions = Transaction.query.filter_by(user_id=user.id).all()
    for transaction in transactions:
        print(transaction.id, transaction.type, transaction.amount)

