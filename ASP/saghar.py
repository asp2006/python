# بارگذاری شیت خاص از فایل اکسل
import pandas as pd
df_sheet = pd.read_excel(file_path, sheet_name='Sheet1')

# نمایش داده‌های شیت خاص
print("داده‌های شیت 'Sheet1':")
print(df_sheet)
