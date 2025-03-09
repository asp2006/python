# افزودن عناصر به مجموعه :
my_set = {1,2,3,}
my_set.add(4)
my_set.add(5)
my_set.add(6)
my_set.add(1)
print(my_set)

# حذف عناصر از مجموعه :
my_set = {1,2,3,3,4}
my_set.remove(3)
print(my_set)

# غیرقابل ترتیب بودن مجموعه‌ها :
my_set = {1,2,3,4,5}
try:
  print(my_set[0])
except TypeError as e :
  print("error:", str (e))  

# توانایی پذیرش انواع مختلف داده‌ها :
my_set = {1,2,1.84,"hola",(1,2,3,)}
print(my_set)

# عملیات روی مجموعه‌ها :
# اتحاد (Union) :
set_a = {1,2,3}
set_b = {4,5,6}
union_set = set_a | set_b
print("Union:", union_set)

# اشتراک (Intersection) :
set_1 = {1,2,2,3,4,}
set_2 = {2,4,5,6}
intersection_set = set_1 & set_2
print("intersection:", intersection_set)

# تفاضل (Difference) :
set_a = {10,20,30,40}
set_b = {30,40,50,60,}
difference_set = set_a - set_b
print(difference_set)

# تفاضل متقارن (Symmetric Difference) :
symmetric_diference_set = set_a ^ set_b
print("Symmetric Diference:", symmetric_diference_set)

# زیرمجموعه و فوق‌مجموعه (Subset and Superset) :
sepid_python1 = {"sharifi","salimi","salemi","yavari"}
sepid_python2 = {"salemi","sharifi"}
is_subset = sepid_python2.issubset(sepid_python1)
is_superset = sepid_python1.issuperset(sepid_python2)
print("is sepid_python2 a subset of sepid_python1?", is_subset)
print("is sepid_python1 a superset of sepid_python2?",is_superset)