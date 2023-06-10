# Q2

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

if name1 < name2:
    print(name1, name2)
else:
    print(name2, name1)

# Q3

stock_price = float(input("Enter the stock price: "))
shares_num = int(input("Enter the number of stocks: "))

total_deal = stock_price * shares_num

if total_deal < 10000:
    print("Sorry, the amount is too low.")
else:
    max_price = float(input("Enter the maximum price you are willing to pay per stock: "))
    if max_price > (stock_price * 1.05):
        print("Ask was sent successfully.")
    else:
        print("Sorry, price range is too low.")

# Q4
# For loops The 'end' parameter of the print() function is set to a space character so that each number is printed
# on the same line with a space between them. There is another new line print '\n' to differentiate different problem
# prints.

for i in range(1, 8):
    print(i, end=" ")

for i in range(7):
    print(i+1, end=" ")
print("\n")
for i in range(2, 9, 2):
    print(i, end=" ")

for i in [2, 4, 6, 8]:
    print(i, end=" ")
print("\n")
for i in range(9, 0, -2):
    print(i, end=" ")

for i in [9, 7, 5, 3, 1]:
    print(i, end=" ")
print("\n")

# While loops
i = 1
while i <= 7:
    print(i, end=" ")
    i += 1
print("\n")

i = 0
while i <= 6:
    print(i+1, end=" ")
    i += 1
print("\n")

i = 2
while i <= 8:
    print(i, end=" ")
    i += 2
print("\n")

i = 9
while i >= 1:
    print(i, end=" ")
    i -= 2
print("\n")
