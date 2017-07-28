from app import db

def init_test_db_connection(self):
    db.begin_transaction()

def close_test_db_connection(self):
    db.rollback()
