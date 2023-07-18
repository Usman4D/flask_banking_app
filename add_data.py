import random
from flask import request, Blueprint
from .models import Account

from . import db
auth = Blueprint('auth', __name__)


@auth.route('/add_account', methods=['POST'])
def add_account():
    name = request.form.get('account_name')
    # type = request.form.get('account_type')
    selected_option = request.form['account_type']
    acc_no = generate_14_digit_integer()
    # account = Account(number=acc_no, name=name, type)


def generate_14_digit_integer():
    """Generates a 14-digit integer."""
    number = ''
    for i in range(14):
        number += str(random.randint(0, 9))
    return int(number)
