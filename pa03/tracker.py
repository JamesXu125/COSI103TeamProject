"""
This module implements a command-line interface for a transaction tracker.
"""
from transaction import Transaction

def show_menu():
    """
    Displays the menu of options for the user.
    """
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
    """
    Runs the main program loop for the transaction tracker.
    """
    transaction = Transaction('transactions.db')
    print("Here are some options about transaction tracker:")
    show_menu()
    choice = input("Enter an option: ")
    while True:
        if choice == "0":
            break
        if choice == "1":
            print()
        elif choice == "2":
            print()
        elif choice == "3":
            print()
        elif choice == "4":
            print(transaction.get_all_transactions())
        elif choice == "5":
            item = {}
            item['item_num'] = input("Enter the item number of transaction to be added: ")
            item['amount'] = input("Enter the amount of transaction to be added: ")
            item['category'] = input("Enter the category of transaction to be added: ")
            item['date'] = input("Enter the date of transaction to be added: ")
            item['description'] = input("Enter the description of transaction to be added: ")
            transaction.add_transaction(item)
            print("A transaction is added!")
        elif choice == "6":
            transaction_id = input("Enter transaction id: ")
            transaction.delete_transaction(transaction_id)
        elif choice == "7":
            transactions = transaction.summarize_transaction_by_date()
            for trans in transactions:
                print(f"{trans['date']}: {trans['total_amount']}")
        elif choice == "8":
            month_summary = transaction.summarize_transaction_by_month()
            for trans in month_summary:
                print(f"{trans['date']}: {trans['total_amount']}")
        elif choice == "9":
            year_summary = transaction.summarize_transaction_by_year()
            for trans in year_summary:
                print(f"{trans['date']}: {trans['total_amount']}")
        elif choice == "10":
            summary = transaction.summarize_by_category()
            print("Summarize by category: ")
            print(summary)
        elif choice == "11":
            show_menu()
        else:
            print("Invalid input")
        choice = input("Enter another option: ")

main()
