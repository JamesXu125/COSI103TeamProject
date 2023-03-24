from transaction import Transaction
import sys

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
    transaction = Transaction('transactions.db')
    print("Here are some options about transaction tracker:")
    show_menu()
    choice = input("Enter an option: ")
    while True:
        if choice == "0":
            break     
        elif choice == "1":
            print()
        elif choice == "2":
            print()
        elif choice == "3":
            print()
        elif choice == "4":
            print(transaction.get_all_transactions())
        elif choice == "5":
            print()
        elif choice == "6":
            transaction_id = input("Enter transaction id: ")
            transaction.delete_transaction_by_item_num(transaction_id)
        elif choice == "7":
            summary = transaction.summarize_by_date()
            print("Summary by date:")
            for s in summary:
                print(f"{s['date']}: {s['total']}")
        elif choice == "8":
            month_summary = transaction.summarize_transaction_by_month()
            print("Summary transaction by month")
            for r in month_summary:
                print(f"{r['month']}: {r['total']}")
        elif choice == "9":
            year_summary = transaction.summarize_transaction_by_year()
            print("Summary transaction by year")
            for r in year_summary:
                print(f"{r['year']}: {r['total']}")
        elif choice == "10":
            summary = transaction.summarize_by_category()
            print("Summarize by category: ")

            
        elif choice == "11":
            show_menu()
        else:
            print("Invalid input")
        choice = input("Enter another option: ")

main()
