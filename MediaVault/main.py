from services.library import (
    load_items,
    save_items,
    add_item,
    list_items,
    search_items,
    remove_item
)


# Mini sistema de menu 2.0 turbo
# Tiny menu system 2.0 turbo
def show_menu():
    print("\n=== MediaVault ===")
    print("1. Add Media")
    print("2. List Media")
    print("3. Search Media")
    print("4. Remove Media")
    print("5. Exit")


# Sistema de cadastro
# Registration system
def main():
    items = load_items()

    while True:
        show_menu()

        option = input("\nChoose an option: ")

        if option == "1":
            title = input("Title: ")
            category = input("Category: ")
            status = input("Status: ")

            try:
                rating = int(input("Rate (1-5): "))

            except ValueError:
                print("Rating must be a number, try again please.")
                continue

            # adiciona o item à biblioteca
            # adds the item to the library
            add_item(
                items,
                title,
                category,
                status,
                rating
            )

            save_items(items)

            print("Item added")

        # mostra os itens
        # displays the registered items
        elif option == "2":
            list_items(items)

        # pesquisa os itens
        # searches for media items
        elif option == "3":
            search = input("Search: ")

            results = search_items(items, search)

            # Caso seja algo que não está no sistema:
            # If the item is not found in the system:
            if not results:
                print("No items found.")

            else:
                list_items(results)

        elif option == "4":
            list_items(items)

            try:
                index = int(input("\nEnter item number to remove: "))

                removed = remove_item(items, index - 1)

                if removed:
                    save_items(items)
                    print("Item removed successfully!")

                else:
                    print("Invalid item.")

            except ValueError:
                print("Please enter a valid number.")

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
