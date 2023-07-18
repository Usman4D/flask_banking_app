from flask_login import UserMixin
from . import db

from enum import Enum


class Account_type(Enum):
    CHECKINGS = 'Checkings'
    SAVINGS = 'Savings'


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    accounts = db.relationship('Account', backref='user')


class Customer(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Account(db.Model):
    # primary keys are required by SQLAlchemy
    number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    type = db.Column(db.Enum(Account_type))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    balance = db.Column(db.Float)
    transactions = db.relationship('Transaction', backref='account')


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    to_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    amount = db.Column(db.Float)
    account_id = db.Column(db.Integer, db.ForeignKey('account.number'))
    description = db.Column(db.String(1000))


class Bank(db.Model):
    # primary keys are required by SQLAlchemy
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))


class Branch(db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    bank_code = db.Column(db.Integer, db.ForeignKey('bank.code'))
