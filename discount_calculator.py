# Define the function to calculate discount
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Apply the discount
        final_price = price - (price * discount_percent / 100)
    else:
        # Return the original price if discount is less than 20%
        final_price = price
    return final_price

# Prompt the user to enter the original price and discount percentage
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Print the final price
    print(f"The final price is: ${final_price:.2f}")

except ValueError:
    print("Please enter a valid number for price and discount percentage.")
