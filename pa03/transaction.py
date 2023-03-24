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

    def get_all_transactions(self):
        return self.runQuery('''SELECT * FROM transactions''',())
    
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

