import pytest
from transaction import Transaction

@pytest.fixture
def transaction():
    return Transaction()
  
def test_delete_transaction(transaction):
    transaction.add_transaction(100, "food", "2023-03-20", "groceries")
    transaction.delete_transaction(1)
    result = transaction.get_transactions()
    assert len(result) == 0

def test_get_transactions_by_date(transaction):
    transaction.add_transaction(100, "food", "2023-03-20", "groceries")
    transaction.add_transaction(200, "clothing", "2023-03-21", "new shirt")
    result = transaction.get_transactions_by_date("2023-03-20")
    assert len(result) == 1
    assert result[0]["amount"] == 100
    assert result[0]["description"] == "food"
    assert result[0]["date"] == "2023-03-20"
    assert result[0]["category"] == "groceries"
