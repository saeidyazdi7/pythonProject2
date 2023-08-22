def ave(li):
    return sum(li) / len(li)


setattr(ave, "schoolName", "sadat")
if hasattr(ave, "schoolName"):
    print(getattr(ave, "schoolName"))
