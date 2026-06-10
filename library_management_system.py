books = ["Python", "Java", "C++", "JavaScript"]

while True:
    print("\n1. View Books")
    print("2. Search Book")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Available Books:")
        for book in books:
            print(book)

    elif choice == "2":
        search = input("Enter book name: ")

        if search in books:
            print("Book Available")
        else:
            print("Book Not Found")

    elif choice == "3":
        break