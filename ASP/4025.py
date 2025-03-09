count = 1
while count <= 5:
    print(count)
    count += 1

# استفاده از حلقه while برای ورودی کاربر :
user_input = ''
while user_input != 'exit':
    user_input = input("enter a command:")
    print("You entered:", user_input)

# استفاده از break و continue در حلقه while :
count = 0
while count < 10:
    count += 1
    if count == 5:
        continue
    print(count)

#  خطر حلقه‌های بی‌نهایت :
count = 0
while count < 5:
    print("This will run forever")
    break

# حلقه while برای درخواست تایید از کاربر :
user_input = ""
while user_input != "yes" and user_input != "no":
    user_input = input("Do you want to continue? (yes/no):").lower()
    if user_input == "yes":
        print("You chose to continue!")
        break
    elif user_input == "no":
        print("You chose to stop!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
