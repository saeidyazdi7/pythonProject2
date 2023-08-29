x = [1, 2, 3, 4]
d = {"l": (l := len(x)),
     "s": (s := sum(x)),
     "a": (a := s / l)
     }
print(d)
