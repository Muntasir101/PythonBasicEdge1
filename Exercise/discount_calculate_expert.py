while True:
    try:
        purchase_amount = float(input('Purchase Amount: '))
        if purchase_amount < 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid Purchase Amount.Please enter a valid amount.")

while True:
    try:
        age = int(input('Age: '))
        if age < 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid Age.Please enter a valid age.")

while True:
    try:
        gender = input('Gender: ')
        if gender.lower() not in ['male', 'female']:
            raise ValueError
        break
    except ValueError:
        print("Invalid Gender.Please enter a valid Gender Male or Female.")

while True:
    try:
        payment_method = input('Payment Method: ')
        if payment_method.lower() not in ['cash', 'card']:
            raise ValueError
        break
    except ValueError:
        print("Invalid payment Method.Please enter a valid Method.")

free_item = ''
discount = 0

# Condition 1: Customer need to purchase more than 1000 tk for discount
if purchase_amount > 1000:
    # Condition 2: Customer age less than 50 years
    if age < 50:
        # Condition 3: Male customer will get "Cake" and Female will get "Chocolate"
        if gender.lower() == 'male':
            free_item = 'Cake'
        elif gender.lower() == 'female':
            free_item = 'Chocolate'

        # Condition 4: cash will get 10% discount, card 20%
        if payment_method.lower() == "cash":
            discount = 10 / 100
        elif payment_method.lower() == "card":
            discount = 20 / 100

discount_amount = purchase_amount * discount
amount_to_pay = purchase_amount - discount_amount

print("Amount to pay: ", amount_to_pay)
print("Free item: ", free_item)
