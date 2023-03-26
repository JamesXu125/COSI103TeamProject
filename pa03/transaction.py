import sqlite3

class Transaction:
    """
    A class to represent a transaction database.
    """
    def __init__(self, db_path):
        """
        Constructs a Transaction object with a path to a SQLite database file.

        Args:
            db_path (str): The path to the SQLite database file.
        """
        self.db_path = db_path
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                            (item_num INTEGER,
                            amount REAL,
                            category TEXT,
                            date TEXT,
                            description TEXT)''',())

    def get_all_transactions(self):
        """
        Retrieves all transactions from the database.

        Returns:
            list: A list of dictionaries representing the transactions.
        """
        return self.runQuery('''SELECT * FROM transactions''',())

    def add_transaction(self, item):
        """
        Adds a transaction to the database.

        Args:
            item (dict): A dictionary representing the transaction.

        Returns:
            list: A list of dictionaries representing the transactions.
        """
        return self.runQuery('''INSERT INTO transactions VALUES(?,?,?,?,?)''',(item['item_num'],item['amount'],
        item['category'],item['date'],item['description']))

    def delete_transaction(self, item_num):
        """
        Deletes a transaction from the database by its item number.

        Args:
            item_num (int): The item number of the transaction to delete.
        """
        return self.runQuery('''DELETE FROM transactions WHERE item_num=?''', (item_num,))

    def summarize_transaction_by_date(self):
        """
        Summarizes the transactions in the database by date.

        Returns:
            list: A list of dictionaries representing the summarized transactions.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT date, SUM(amount) FROM transactions GROUP BY date')
        results = cursor.fetchall()
        return [{"date": date, "total_amount": amount} for date, amount in results]

    def summarize_transaction_by_month(self):
        """
        Summarizes the transactions in the database by month.

        Returns:
            list: A list of dictionaries representing the summarized transactions.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT substr(date,1,2) || '/' ||substr(date,7,10) AS month,SUM(amount) FROM transactions GROUP BY month")
        results = cursor.fetchall()
        return [{"date": date, "total_amount": amount} for date, amount in results]

    def summarize_transaction_by_year(self):
        """
        Summarizes the transactions in the database by year.

        Returns:
            list: A list of dictionaries representing the summarized transactions.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT substr(date,7,10) AS year, SUM(amount) FROM transactions GROUP BY year")
        results = cursor.fetchall()
        return [{"date": date, "total_amount": amount} for date, amount in results]

    def summarize_by_category(self):
        """
        Summarizes the transactions in the database by category.

        Returns:
            list: A list of dictionaries representing the summarized transactions.
        """
        return self.runQuery('''SELECT * FROM transactions GROUP BY category''',())

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return tuples_to_dicts(tuples)

def to_dict(tran):
    transaction = {'item_num': tran[0], 'amount': tran[1], 'category': tran[2], 'date': tran[3], 'description': tran[4]}
    return transaction

def tuples_to_dicts(trans):
    return [to_dict(tran) for tran in trans]
