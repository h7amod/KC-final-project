def supplier_module():
    print("Welcome to the supplier module")

    num_ingredients = int(input("How many ingredients do you want to input: "))

    ingredient_names = []
    ingredient_quantities = []
    ingredients_cost = []

    for i in range(num_ingredients):
        ingredient_name = input(f"Enter the name of ingredient {i + 1}: ")
        ingredient_names.append(ingredient_name)

        while True:
            try:
                ingredient_unit = input(f"Is {ingredient_name} measured in kilograms (kg) or bottles/cans? ").lower()
                if ingredient_unit in ["kg", "kilograms", "bottle", "bottles", "can", "cans"]:
                    break
                else:
                    print("Invalid input. Please enter 'kg' for kilograms or 'bottle'/'can' for bottles/cans.")
            except ValueError:
                print("Invalid input. Please enter 'kg' for kilograms or 'bottle'/'can' for bottles/cans.")

        while True:
            try:
                if ingredient_unit in ["bottle", "bottles", "can", "cans"]:
                    ingredient_cost = float(input(f"Enter the cost of a {ingredient_name} {ingredient_unit}: "))
                else:
                    ingredient_cost = float(input(f"Enter the cost of 1 kg of {ingredient_name}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid cost.")

        while True:
            try:
                ingredient_quantity = float(input(f"Enter the quantity of {ingredient_name} used per meal: "))
                ingredient_quantities.append(ingredient_quantity)
                break
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")

        ingredients_cost.append(ingredient_cost)

    #حساب التكلفة الكامله (كجم أو بطول/علب)
    total_expenses = sum(cost * quantity for cost, quantity in zip(ingredients_cost, ingredient_quantities))

    while True:
        try:
            meal_price = float(input("Enter the price of the meal: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid price.")

    profit_or_loss = meal_price - total_expenses

    print(f"Total Expenses: {total_expenses:.2f} KWD")
    print(f"Selling Price: {meal_price:.2f} KWD")
    if profit_or_loss > 0:
        print(f"Profit: {profit_or_loss:.2f} KWD")
    elif profit_or_loss < 0:
        print(f'Loss: {abs(profit_or_loss):.2f} KWD')
    else:
        print("No profit or loss")


def consumer_module():
    print("Welcome to the consumer module")

    restaurant_menu = [
        {
            'name': 'falafel sandwich',
            'price': 0.1
        },
        {
            'name': 'hotdog',
            'price': 0.25
        },
        {
            'name': 'chicken sandwich (meal)',
            'price': 1.1
        },
        {
            'name': 'chicken sandwich',
            'price': 0.5
        },
        {
            'name': 'shawarma chicken',
            'price': 0.5
        },
        {
            'name': 'shawarma beef',
            'price': 0.5
        },
        {
            'name': 'chabati rashid',
            'price': 0.75
        },
        {
            'name': 'fries',
            'price': 0.3
        },
        {
            'name': 'pepsi',
            'price': 0.15
        },
        {
            'name': 'mountain dew',
            'price': 0.15
        },
        {
            'name': '7up',
            'price': 0.15
        }
    ]

    try:
        consumer_budget = float(input("How much money do you have (KWD)? "))
    except ValueError:
        print("Invalid input. Please enter a valid amount in KWD.")
        return

    affordable_items = []
    for item in restaurant_menu:
        if item['price'] <= consumer_budget:
            affordable_items.append(item)

    if affordable_items:
        print("You can afford the following items:")
        for item in affordable_items:
            print(f"{item['name']}: KWD {item['price']:.2f}")
    else:
        print("Sorry, you don't have enough money to buy anything from the menu.")




while True:
    print("\nOptions:")
    print("1. Supplier Module")
    print("2. Consumer Module")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        supplier_module()
    elif choice == '2':
        consumer_module()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

