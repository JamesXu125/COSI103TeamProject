import sqlite3

class Transaction:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                            (item_num INTEGER,
                            amount REAL,
                            category TEXT,
                            date TEXT,
                            description TEXT)''')
        self.conn.commit()

    def get_all_transactions(self):
        self.cursor.execute('''SELECT * FROM transactions''')
        return self.cursor.fetchall()
    
    def get_transaction_by_item_num(self, item):
        self.cursor.execute('''SELECT * FROM transactions WHERE item_num=?''', (item,))
        return self.cursor.fetchone()
    
    def get_transactions_by_category(self, category):
        self.cursor.execute('''SELECT * FROM transactions WHERE category=?''', (category,))
        return self.cursor.fetchall()
    
    def add_transaction(self, item_num, amount, category, date, description):
        self.cursor.execute('''INSERT INTO transactions
                            (item_num, amount, category, date, description)
                            VALUES (?, ?, ?, ?, ?)''',
                            (item_num, amount, category, date, description))
        self.conn.commit()

    def delete_transaction_by_item_num(self, item):
        self.cursor.execute('''DELETE FROM transactions WHERE item_num=?''', (item,))
        self.conn.commit()