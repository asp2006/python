# تبدیل ورودی به عدد صحیح :
num = int(input("please enter a number: "))
print(f"the number:{num}")

# تبدیل ورودی به عدد اعشاری (float) :
decimal = float(input("decimal num: "))
print(f"Your choices:{decimal}")

#  گرفتن نام و سن در یک خط :
name,age = input("name and age :").split()
age = int(age)
print(f"the result :{name},{age}")

try:
    num = int(input("Entered number :"))
    print(f"num :")
except ValueError:
    print("please enter a number...!")
    print(input(f"Entered number :"))
