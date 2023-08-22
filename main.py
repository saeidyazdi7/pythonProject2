# تعریف یک تابع بازگشتی به نام is_palindrome
def is_palindrome(s):
    # اگر رشته خالی باشد یا فقط یک حرف داشته باشد، True را برگردان
    if len(s) <= 1:
        return True
    # در غیر این صورت، بررسی کن که اولین و آخرین حرف رشته با هم برابر هستند یا خیر
    else:
        # اگر برابر نباشند، False را برگردان
        if s[0] != s[-1]:
            return False
        # اگر برابر باشند، باقی رشته را بدون اولین و آخرین حرف برای بررسی بفرست
        else:
            return is_palindrome(s[1:-1])


print(is_palindrome("123321"))
