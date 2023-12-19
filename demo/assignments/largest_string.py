def largest_name(*names):
    ls = ""
    for n in names:
        if len(n) > len(ls):
            ls = n
            
    return ls


print(largest_name('Steve', "Mark", "Jackson", "Joe", "Andy"))