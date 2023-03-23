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
            
        elif choice == "4":
            trs = transaction.show_transactions()
            print("Here are all the transactions:\n", trs)
        
        elif choice == "5":
            item_num = input("Enter the item number of the transaction to be added: ")
            amount = input("Enter the amount of transaction to be added: ")
            category = input("Enter the category of transaction to be added: ")
            date = input("Enter the date of transaction to be added: ")
            description = input("Enter the description of transaction to be added: ")
            trs = (item_num, amount, category, date, description)
            transaction.add_transaction(trs)
            print("Transaction ",trs, " has been added!")
            
        elif choice == "6":
            transaction_id = input("Enter transaction id: ")
            delete_transaction_by_item_num(transaction_id)

        elif choice == "7":
            summary = transaction.summarize_by_date()
            print("Summary by date:")
            for s in summary:
            print(f"{s['date']}: {s['total']}")
            
            
        elif choice == "11":
            show_menu()
        else:
            print("Invalid choice")
