import tkinter as tk
from tkinter import ttk

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("DataGrid Example")

# داده‌های نمونه
data = [
    {"ID": 1, "Name": "Ali", "Age": 19},
    {"ID": 2, "Name": "Sahar", "Age": 11},
    {"ID": 3, "Name": "Sara", "Age": 10},
]

# ایجاد Table یا Treeview
columns = ("ID", "Name", "Age")
tree = ttk.Treeview(root, columns=columns, show="headings")

# تعریف هدرها
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")

# اضافه کردن داده‌ها به دیتاگرید
for item in data:
    tree.insert("", "end", values=(item["ID"], item["Name"], item["Age"]))

# قرار دادن در پنجره
tree.pack()

root.mainloop()
