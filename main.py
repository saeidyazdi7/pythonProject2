def ave(li):
    return sum(li), len(li)


setattr(ave, "schoolName", "shafagh")
print(ave.schoolName)
print(ave.__dict__)
print(getattr(ave, "schoolName"))
# ave.schoolName = "Sadat"
# print(dir(ave))
# print(ave.schoolName)
