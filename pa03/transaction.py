import sqlite3

class Transaction:
    def __init__(self, db_path):
        self.db_path = db_path
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                            (item_num INTEGER,
                            amount REAL,
                            category TEXT,
                            date TEXT,
                            description TEXT)''',())
        # self.runQuery('''INSERT INTO transactions VALUES (1, 12345, 'test', '03/23/2023', 'run test 1')''',())
        # self.runQuery('''INSERT INTO transactions VALUES (2, 3.14, 'test', '03/23/2023', 'run test 2')''',())
        #self.runQuery('''INSERT INTO transactions VALUES (3, 37, 'not test', '07/21/2021', 'description')''',())

    # get all transaction, method 4 
    def get_all_transactions(self):
        return self.runQuery('''SELECT * FROM transactions''',())
    def summarize_by_category(self):
        return self.runQuery('''SELECT * FROM transactions GROUP BY category''',())
    
    # add one transaction, method 5 --Ziming
    def add_transaction(self, item):
        return self.runQuery('''INSERT INTO transactions VALUES(?,?,?,?,?)''',(item['item_num'],item['amount'],
        item['category'],item['date'],item['description']))
    
    #delete the transaction by item number, method 6,  --hang liao
    def delete_transaction(self, item_num):
        return self.runQuery('''DELETE FROM transactions WHERE item_num=?''', (item_num,))
    
    #summarize the transaction by date, method 7,  --hangliao
    def summarize_transaction_by_date(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT date, SUM(amount) FROM transactions GROUP BY date')
        results = cursor.fetchall()
        return [{"date": date, "total_amount": amount} for date, amount in results]
    
    #summarize the transaction by month, method 8,  --zijun wang
    def summarize_transaction_by_month(self):
        self.cursor.execute("SELECT strftime('%m', date) AS month, SUM(amount) FROM transactions GROUP BY month")
        return self.cursor.fetchall()
    
    #summarize the transaction by year, method 9,  --zijun wang
    def summarize_by_transaction_year(self):
        self.cursor.execute("SELECT strftime('%Y', date) AS year, SUM(amount) FROM transactions GROUP BY year")
        return self.cursor.fetchall()
    
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect(self.db_path)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return tuples_to_dicts(tuples)

def to_dict(t):
    transaction = {'item_num': t[0], 'amount': t[1], 'category': t[2], 'date': t[3], 'description': t[4]}
    return transaction

def tuples_to_dicts(ts):
    return [to_dict(t) for t in ts]

