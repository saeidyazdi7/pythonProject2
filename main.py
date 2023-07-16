dic = {}
key = input("Keyword:")
means = input("Mean:").split(",")
dic[key] = means
word = input("Enter:")
print("Mean:", dic.get(word))
