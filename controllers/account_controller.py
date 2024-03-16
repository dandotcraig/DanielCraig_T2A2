from flask import Blueprint

from init import db
from models.account import Account, Account_schema, Accounts_schema


account_bp = Blueprint('account', __name__, url_prefix='/account')

@account_bp.route('/<int:account_id>')
def get_account(account_id):
    stmt = db.select(Account).filter_by(id=account_id)
    account = db.session.scalar(stmt)
    return Account_schema.dump(account)



@account_bp.route('/')
def get_all_accounts():
    stmt = db.select(Account).order_by(Account.date_added.desc())
    accounts = db.session.scalars(stmt)
    return Accounts_schema.dump(accounts)

