
import pytest
import sqlite3
from transaction import Transaction, to_dict, tuples_to_dicts

@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [(1, 12345, "test", "03/23/2023", "run test 1"), 
            (2, 3.14, "test", "03/23/2023", "run test 2")
           ]

@pytest.fixture
def returned_tuples(tuples):
    return [tuples[i] for i in range(len(tuples))]

@pytest.fixture
def returned_dicts(tuples):
    return tuples_to_dicts([tuples[i] for i in range(len(tuples))])

@pytest.fixture
def transaction_path(tmp_path):
    yield tmp_path / 'transaction.db'

@pytest.fixture(autouse=True)
def transactions(transaction_path, tuples):
    "create and initialize the transaction in the database"
    con = sqlite3.connect(transaction_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                (item_num INTEGER,
                amount REAL,
                category TEXT,
                date TEXT,
                description TEXT)''')
    for i in range(len(tuples)):
        cur.execute('''INSERT INTO transactions VALUES(?,?,?,?,?)''',tuples[i])
    con.commit()
    tc = Transaction(transaction_path)
    yield tc
    cur.execute('''drop table transactions''')
    con.commit()

def test_getAll(transactions, returned_dicts):
    tc = transactions
    results = tc.get_all_transactions()
    expected = returned_dicts
    assert results == expected