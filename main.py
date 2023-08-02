# تعریف تابع split_bill که دو پارامتر می گیرد: names و amounts
def split_bill(names, amounts):
    # محاسبه قیمت کل بدون احتساب تیپ
    total = sum(amounts)
    # محاسبه قیمت هر شخص با تقسیم قیمت کل بر تعداد افراد
    each_pay = total / len(names)
    # ایجاد یک دیکشنری خالی برای ذخیره اختلاف های هر شخص
    diffs = {}
    # حلقه روی لیست نام ها و مقادیر
    for name, amount in zip(names, amounts):
        # محاسبه اختلاف بین قیمت هر شخص و قیمت مساوی
        diff = amount - each_pay
        # افزودن اختلاف به دیکشنری با نام شخص به عنوان کلید
        diffs[name] = diff
    # حلقه روی دیکشنری اختلاف ها
    for name, diff in diffs.items():
        # اگر اختلاف منفی باشد، یعنی شخص باید پول بدهد
        if diff < 0:
            # حلقه روی دوباره روی دیکشنری اختلاف ها
            for other_name, other_diff in diffs.items():
                # اگر نام شخص با نام دیگر متفاوت باشد و اختلاف دیگر مثبت باشد، یعنی شخص دیگر باید پول بگیرد
                if name != other_name and other_diff > 0:
                    # محاسبه حداقل مبلغ قابل پرداخت بین دو شخص با استفاده از تابع min
                    min_pay = min(-diff, other_diff)
                    # چاپ جمله با فرمت مورد نظر
                    print(f"{name} pays {min_pay:.2f} dollars to {other_name}.")
                    # کاهش اختلاف های دو شخص با مقدار پرداخت شده
                    diffs[name] += min_pay
                    diffs[other_name] -= min_pay


# درخواست ورودی از کاربر
# تبدیل ورودی به لیست با جداسازی با کاما
names = input("Enter the names of the people: ").split(",")
# تبدیل ورودی به لیست عدد صحیح با جداسازی با کاما و استفاده از comprehension list
amounts = [int(x) for x in input("Enter the amounts paid by each person: ").split(",")]
# فرض کنید تعداد نام ها و مقادیر برابر است

# فراخوانی تابع با ورودی های درخواست شده
split_bill(names, amounts)
