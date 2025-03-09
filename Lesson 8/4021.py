# ساختار پایه if :
x = 10
if x > 5:
    print("x is greater than 5")
# تورفتگی (Indentation) :
x = 10
if x > 11:
    print("x is greater than 11")
else:
    print("x is samll")
# عملگرهای مقایسه‌ای و منطقی :
x = 7
y = 9
if x > 5 and y < 10:
    print("both condition are true")
# ارزیابی‌های شرطی :
if "hello":
    print("This will print")
if 0:
    print("this will not print")
# شرط‌های تو در تو (Nested Conditions) :
x = 10 
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")
#  استفاده از elif و else :
x = 15
if x > 20:
    print("x is greater than 20")
elif x > 10:
    print("x is greater than 10 but less than equal to 20")
else:
    print("x is 10 or less")