# عملگرهای عضویت (Membership Operators) :
# in :
name = ['ali','sahar','sara']
if 'ali' in name:
    print("'ali' is in the list of name")
if "reza" in name:
    print("is in the list")
else:
    print("is not")
# set :    
set = {323,378,356}
if 391 in set:
    print("is in the set")
else:
    print("is not")
# dictionary :
student = {'name': 'zhara', 'age': 18}
if 'name' in student:
    print("True")
# not in :
language = ("english","french","spanish")
if "italy" not in language:
    print(" 'italy' is not")

# عملگرهای هویتی (Identity Operators) :
# is :
a = [1,2,3]
b = a
if a is b:
    print("a and b refer to the same object")
# مقایسه با None :
c = None
if c is None:
    print("c is none")
# مقایسه دو لیست متفاوت: :
list1 = [1,2,3]
list2 = [1,2,3,4]
if list1 is not list2:
    print("list1 and list2 do not refer to the same object")
x = [3,4,5]
y = x.copy()
if x is not y:
    print("x and y are different objects")