def my_len(obj):  # تعریف یک تابع با نام my_len و یک پارامتر obj
    count = 0  # ایجاد یک متغیر با مقدار صفر به عنوان شمارنده
    for item in obj:  # حلقه for برای پیمایش در هر عضو obj
        count += 1  # افزودن یک واحد به شمارنده
    print(count)
    return count  # برگرداندن مقدار شمارنده به عنوان خروجی تابع


x = input("Enter:")
my_len(x)
