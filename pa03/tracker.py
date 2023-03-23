from transaction import Transaction
def show_menu():
    print("0. quit")
    print("1. show categories")
    print("2. add category")
    print("3. modify category")
    print("4. show transactions")
    print("5. add transaction")
    print("6. delete transaction")
    print("7. summarize transactions by date")
    print("8. summarize transactions by month")
    print("9. summarize transactions by year")
    print("10. summarize transactions by category")
    print("11. print this menu")

def main():
    transaction = Transaction()
    while True:
        if choice == "0":
            break
        elif choice == "6":
            transaction_id = input("Enter transaction id: ")
            delete_transaction_by_item_num(transaction_id)
        elif choice == "7":
            summary = transaction.summarize_by_date()
            print("Summary by date:")
            for s in summary:
            print(f"{s['date']}: {s['total']}")
