
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent/100))
        return final_price
    else:
        return price

final_price = calculate_discount(200, 10)

print(f"The final price is {final_price}")