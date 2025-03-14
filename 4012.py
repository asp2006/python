# دیکشنری برای اطلاعات کشورها
countries = {
    1: {"name": "ایران", "capital": "تهران", "area": "1,648,195 km²", "population": "82 میلیون نفر"},
    2: {"name": "آلمان", "capital": "برلین", "area": "357,022 km²", "population": "83 میلیون نفر"},
    3: {"name": "فرانسه", "capital": "پاریس", "area": "643,801 km²", "population": "67 میلیون نفر"},
    4: {"name": "ژاپن", "capital": "توکیو", "area": "377,975 km²", "population": "126 میلیون نفر"},
    5: {"name": "کانادا", "capital": "اتاوا", "area": "9,984,670 km²", "population": "38 میلیون نفر"}
}

# نمایش اطلاعات یک کشور بر اساس شناسه
country_id = 2  # آلمان
if country_id in countries:
    country = countries[country_id]
    print(f"Country: {country['name']}")
    print(f"Capital: {country['capital']}")
    print(f"Area: {country['area']}")
    print(f"Population: {country['population']}")
else:
    print("Country not found.")

# بروز رسانی اطلاعات یک کشور
countries[3]["population"] = "68 میلیون نفر"  # بروز رسانی جمعیت فرانسه

# افزودن کشور جدید
countries[6] = {"name": "آمریکا", "capital": "واشنگتن", "area": "9,525,067 km²", "population": "331 میلیون نفر"}

# نمایش اطلاعات تمامی کشورها
for country_id, info in countries.items():
    print(f"ID: {country_id}, Country: {info['name']}, Capital: {info['capital']}, "
          f"Area: {info['area']}, Population: {info['population']}")

# حذف یک کشور
del countries[5]  # حذف کانادا

# نمایش اطلاعات پس از حذف
print("\nCountry data after deleting Canada:")
for country_id, info in countries.items():
    print(f"ID: {country_id}, Country: {info['name']}, Capital: {info['capital']}, "
          f"Area: {info['area']}, Population: {info['population']}")
