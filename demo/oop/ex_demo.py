s = input("Enter number:")
try:
    v = int(s)
    print(100 // v)
except ValueError as ex:
    print("Error: ", ex)
# except ZeroDivisionError:
#     print("Sorry! Zero is not valid!")
else:
    print("Done")
finally:
    print("Finally!")

print('The End')
