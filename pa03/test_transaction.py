
import pytest
import sqlite3
from transaction import Transaction, to_dict, tuples_to_dicts

@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [(1, 12345, "test", "03/23/2023", "run test 1"), 
            (2, 3.14, "test", "03/23/2023", "run test 2"),
            (3, 37, "not test", "07/21/2021", "description"),
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

# test for the get all transactions method (method4) --Ziming
def test_getAll(transactions, returned_dicts):
    tc = transactions
    results = tc.get_all_transactions()
    expected = returned_dicts
    assert results == expected

# test for the add transaction method (method5) --Ziming 
def test_add(transactions, tuples):
    tc = transactions
    test_tuple = tuples
    add_t = (5, 125, "add_test", "03/23", "run test 5")
    test_tuple.append(add_t)
    tc.add_transaction(to_dict(add_t))
    expected = tuples_to_dicts(test_tuple)
    results = tc.get_all_transactions()
    assert results == expected

def test_summarize_by_category(transactions, returned_dicts):
    categories=[]
    expected=[]
    for i in (returned_dicts):
        if(i.get("category") not in categories):
            categories.append(i.get("category"))
            expected.append(i)
    expected = sorted(expected, key=lambda x: x['category'])
    results = transactions.summarize_by_category()
    assert results == expected
    
#pytest for delete the transaction by item number, method 6,  --hang liao
def test_delete_transaction(transactions):
    tc = transactions
    item_num = 1
    tc.delete_transaction(item_num)
    results = tc.get_all_transactions()
    expected = [to_dict(t) for t in [(2, 3.14, "test", "03/23/2023", "run test 2"), 
                                     (3, 37, "not test", "07/21/2021", "description")]]
    assert results == expected

#pytest for summarize the transaction by date, method 7,  --hang liao
def test_summarize_by_date(transactions, returned_dicts):
    dates = []
    expected = []
    for t in returned_dicts:
        date = t.get("date")
        if date not in dates:
            dates.append(date)
            total_amount = sum(d.get("amount") for d in returned_dicts if d.get("date") == date)
            expected.append({"date": date, "total_amount": total_amount})
    expected = sorted(expected, key=lambda x: x['date'])
    results = transactions.summarize_transaction_by_date()
    assert results == expected

    
#pytest for summarize_transaction_by_year, method 8 -- zijun wang
def test_summarize_transaction_by_year(transactions):
    tc = transactions
    expected = [
        {"date": "2021", "total_amount": 37},
        {"date": "2023", "total_amount": 12348.14},
    ]
    results = tc.summarize_transaction_by_year()
    assert results == expected

#pytest for summarize_transaction_by_month, method 9 -- zijun wang
def test_summarize_transaction_by_month(transactions):
    tc = transactions
    expected = [
        {"date": "03/2023", "total_amount": 12348.14},
        {"date": "07/2021", "total_amount": 37},
    ]
    results = tc.summarize_transaction_by_month()
    assert results == expected

