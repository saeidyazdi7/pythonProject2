# تعریف یک تابع بازگشتی به نام is_palindrome
def version(s):
    if s < 10:
        return s
    else:
        return s % 10 + version(s // 10)


print(version(1234))
