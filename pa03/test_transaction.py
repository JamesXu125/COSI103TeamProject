import pytest
from transaction import Transaction

@pytest.fixture
def transaction():
    # Create a temporary database file for testing
    db_file = 'test.db'
    # Create a Transaction instance using the temporary database file
    t = Transaction(db_file)
    # Yield the Transaction instance so it can be used in the tests
    yield t
    # Close the Transaction instance and delete the temporary database file after the tests
    t.close()
    os.remove(db_file)
    
def test_delete_transaction(transaction):
    # Call delete_transaction to delete the test transaction
    transaction.add_transaction(1, 10.50, 'Groceries', '2022-03-22', 'Bought some apples and oranges')
    transaction.delete_transaction(1)
    # Use a SELECT statement to check if the transaction was deleted
    transaction.cursor.execute("SELECT * FROM transactions WHERE id=?", (1,))
    # Fetch the result of the SELECT statement
    result = transaction.cursor.fetchone()
    # Check that the result is None (i.e., the transaction was deleted)
    assert result is None

def test_summarize_by_date(transaction):
    # Add some test transactions to the database
    transaction.add_transaction(1, 10.50, 'Groceries', '2022-03-22', 'Bought some apples and oranges')
    transaction.add_transaction(2, 15.25, 'Gas', '2022-03-22', 'Filled up the tank')
    transaction.add_transaction(3, 20.00, 'Dinner', '2022-03-23', 'Ate at a fancy restaurant')
    # Call summarize_by_date to get a summary of transactions by date
    summary = transaction.summarize_by_date()
    # Check that the summary is correct
    assert summary == [('2022-03-22', 25.75), ('2022-03-23', 20.0)]
    
