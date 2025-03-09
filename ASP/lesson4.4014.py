x = 99.9
x_int = int(x)
print(x_int)

y = "2006"
y_int = int(y)
print(y_int)

#  تبدیل set به list :
my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
print(my_list)

# تبدیل list به set :
my_list = [1, 2, 3, 4, 5, 5, 3, 2]
my_set = set(my_list)
print(my_set)

# تبدیل dict به list از کلیدها :
my_dict = {"a": 1, "b": 2, "c": 3}
keeys_list = list(my_dict.keys())
print(keeys_list)

# تبدیل str به list :
my_string = "hello"
string_list = list(my_string)
print(string_list)
