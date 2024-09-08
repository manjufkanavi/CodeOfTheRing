import random

# Function to generate a random number with the desired number of digits
def generate_random_number(digits):
    if digits < 1:
        raise ValueError("Number of digits must be at least 1")
    
    lower_bound = 10**(digits - 1)
    upper_bound = 10**digits - 1
    return random.randint(lower_bound, upper_bound)

# Take the number of digits as input from the user
num_digits = int(input("Enter the number of digits: "))

# Generate and print the random number with the desired number of digits
random_number = generate_random_number(num_digits)
print(f"Random {num_digits}-digit number: {random_number}")
