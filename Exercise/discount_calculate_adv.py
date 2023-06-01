purchase_amount = float(input('Purchase Amount: '))
age = int(input('Age: '))
gender = input('Gender: ')
payment_method = input('Payment Method: ')

free_item = ''
discount = 0

# input validation
if purchase_amount <= 0:
    print('Amount invalid.Please enter a valid purchase amount.')

if age < 0:
    print('Age invalid.Please enter a valid age.')

if gender.lower() not in ['male', 'female']:
    print('Not Eligible for Free item.Please specify Gender for Free Item.')

if payment_method.lower() not in ['cash', 'card']:
    print('Invalid payment method. Please enter a valid payment method.')


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
