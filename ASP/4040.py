import pandas as pd
from openpyxl import load_workbook

file_path = r"C:\Users\kara\OneDrive\Desktop\python\ASP\sample1.xlsx"
df = pd.read_excel(file_path)
print("Data from the original file:")
print(df)
# نوشتن داده‌ها به یک فایل اکسل جدید
data = {
    'Name': ['ali', 'sahar', 'sara'],
    'Age': [19, 11, 10],
    'City': ['abadan', 'abadan', 'abadan']
}

# تبدیل داده‌ها به DataFrame
df_new = pd.DataFrame(data)

# مسیر فایل اکسل برای ذخیره
output_file = r"C:\Users\kara\OneDrive\Documents\output_file.xlsx"  # اضافه کردن پسوند .xlsx

# نوشتن داده‌ها به فایل اکسل جدید
df_new.to_excel(output_file, index=False)

print(f"Data has been successfully saved in the file {output_file}.")

# انتخاب یک شیت خاص از فایل اکسل (اگر به این شیت نیاز دارید)
# فقط داده‌های شیت 'Sheet1' را در صورتی که نیاز دارید نمایش دهید:
df_Sheet = pd.read_excel(output_file, sheet_name='Sheet1')
print("'Sheet1' data:")
print(df_Sheet)

# افزودن داده به شیت موجود :
# بارگذاری فایل اکسل
wb = load_workbook(output_file)

# انتخاب شیت موجود
ws = wb.active

# افزودن داده به اولین ردیف خالی
# دقت کنید که تعداد ستون‌ها باید با تعداد ستون‌های DataFrame شما برابر باشد
ws.append(['Fatemeh', 44, 'abadan'])  # داده جدید به شیت اضافه شد

# ذخیره تغییرات
wb.save(output_file)

# فیلتر کردن داده‌ها: افراد با سن بیشتر از 18 سال
# توجه: فیلتر کردن باید بر روی df_new انجام شود که داده‌های جدید را شامل می‌شود
filtered_df = df_new[df_new['Age'] > 18]

# نمایش داده‌های فیلتر شده
print("Filtered data (Age > 18):")
print(filtered_df)

# محاسبه میانگین سن
mean_age = df_new['Age'].mean()
print(f"Mean Age: {mean_age}")

# محاسبه مجموع سن
sum_age = df_new['Age'].sum()
print(f"Sum of Ages: {sum_age}")
