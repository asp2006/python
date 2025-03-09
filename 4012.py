people = {1: {"name": "ali", "age": 18, "city": "tehran"}}
print(people[1]["name"])

# بروز رسانی اطلاعات و پیمایش بر روی کلید و مقادیر

people[2] = {"name": "sahar", "age": 12, "city": "tehran"}
people[2]["age"] = 13
people[2]["name"] = "sara"
for key, value in people.items():
    print(f"{key}: {value}")
# delete one people : del people[1]

# درباره ی خانه
house = {"meterage": 120,
         "bedroom": "3 rooms",
         "balcony": "yes",
         "yard": "no",
         "buiit": 1996
         }

# نمایش اطلاعات خانه
print(f"Meterage:{house['meterage']}")
print(f"Bedroom:{house['bedroom']}")
print(f"Balcony:{house['balcony']}")
print(f"Yard:{house['yard']}")
print(f"Built:{house['buiit']}")

# بروز رسانی اطلاعات
house["buiit"] = 2006
for key, value in house.items():
    print(f"{key}:{value}")

# تعریف دیکشنری برای نگهداری اطلاعات کارمندان
employees = {
    101: {"name": "Ali", "department": "HR", "position": "Manager", "salary": 5000},
    102: {"name": "Sara", "department": "IT", "position": "Developer", "salary": 4000},
    103: {"name": "Reza", "department": "Finance", "position": "Accountant", "salary": 3500}
}

# شناسه کارمند
employee_id = 101

# دسترسی سریع به اطلاعات کارمند با استفاده از شناسه
if employee_id in employees:
    employee_info = employees[employee_id]
    print(f"Name: {employee_info['name']}")
    print(f"Department: {employee_info['department']}")
    print(f"Position: {employee_info['position']}")
    print(f"Salary: {employee_info['salary']}")
else:
    print("Employee not found.")


# نمایش تمامی اطلاعات کارمندان
for employee_id, employee_info in employees.items():
    print(f"ID:{employee_id}, Name:{employee_info['name']}, "
          f"Department:{employee_info['department']}, "
          f"Position:{employee_info['position']}, "
          f"Salary:{employee_info['salary']}")

# حذف اطلاعات کارمند با شناسه 102
<<<<<<< HEAD
del employees[102]
=======
del employees[101]
>>>>>>> 29015632ee19911724222ea2be77098f157d40af

# نمایش تمامی اطلاعات کارمندان پس از حذف
for employee_id, employee_info in employees.items():
    print(f"ID:{employee_id}, Name:{employee_info['name']}, "
          f"Department:{employee_info['department']}, "
          f"Position:{employee_info['position']}, "
          f"Salary:{employee_info['salary']}")


# دیکشنری برای تبدیل کد کشور به نام کشور
country_conversion = {
    +1: "United States",
    +98: "Iran",
    +44: "United Kingdom",
    +49: "Germany",
    +33: "France",
    +91: "India",
    +81: "Japan",
    +61: "Australia",
    +55: "Brazil",
    +52: "Mexico"
}

# لیست کد کشورهای که نیاز است به نام کشور تبدیل شوند
country_codes = [+81, +44, +98]

# تبدیل کد کشورها به نام کشورها
country_names = [country_conversion[code] for code in country_codes]

print("Country codes:", country_codes)
print("Country names:", country_names)
