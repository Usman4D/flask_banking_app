import random
import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import db
from .models import Account, Transaction

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return redirect(url_for('auth.login'))


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, accounts=current_user.accounts)


@main.route('/add_account', methods=['POST'])
@login_required
def add_account():
    name = request.form.get('account_name')
    balance = request.form.get('account_balance')
    # type = request.form.get('account_type')
    selected_option = request.form['account_select']
    # print("================================================================")
    # print(selected_option)
    # print("================================================================")
    acc_no = generate_14_digit_integer()
    # Replace with mysql statements
    account = Account(number=acc_no, name=name,
                      type=selected_option.upper(), user_id=current_user.id, balance=balance)
    db.session.add(account)
    db.session.commit()

    return redirect(url_for('main.profile'))


@main.route('/add_transaction', methods=['POST'])
@login_required
def add_transaction():
    account_number = request.form.get('account_number')
    selected_account = request.form['account_select']
    transfer_balance = float(request.form.get('account_balance'))
    description = request.form.get('description')
    account_id = request.form.get('data')

    account_target = Account.query.get(account_number)
    if account_target == None:
        flash('No such account exists')
        return redirect((url_for('main.make_transaction')))
        # return render_template('transactions_modal.html', account_id=account_id)

    current_account = Account.query.filter_by(name=selected_account).first()
    current_account.balance -= transfer_balance

    if current_account.balance-transfer_balance < 0:
        flash('Insufficient balance')
        return redirect((url_for('main.make_transaction')))

    target_user = account_target.user
    account_target.balance += transfer_balance
    transaction = Transaction(date=datetime.datetime.today(
    ), to_user=target_user.id, amount=transfer_balance, account_id=account_number, account=account_target,  description=description)

    db.session.add(transaction)
    db.session.commit()

    return redirect(url_for('main.profile'))


@main.route('/make_transaction', methods=['POST'])
@login_required
def make_transaction():
    account_id = int(request.form['data'])
    accounts = current_user.accounts
    return render_template('transactions_modal.html', accounts=accounts, account_id=account_id)


@main.route('/accounts_details', methods=['POST'])
@login_required
def account_details():
    account_number = int(request.form['data'])
    # replace with mysql statements
    account = Account.query.get(account_number)
    # accounts = current_user.accounts
    transactions = account.transactions
    print("================================================================")
    print(transactions)
    print("================================================================")

    return render_template('accounts_modal.html', account=account, user_name=current_user.name, transactions=transactions)


def generate_14_digit_integer():
    """Generates a 14-digit integer."""
    number = ''
    for i in range(14):
        number += str(random.randint(0, 9))
    return int(number)
