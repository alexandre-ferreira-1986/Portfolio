
# Value of the Coke
total = 50

# Logic
while total > 0:
    # Print the amount due and ask the user the value
    print("Amout Due: ", total, end="")
    value = int(input("Insert Coin: "))
    
    if value in [25, 10, 5]:
        total -= value

# How much the machine has to give back
owed = abs(total)

# Print the result
print("Change Owed: ", owed)
    
    

# Alternative logic
# if coin in [25,10,5]

