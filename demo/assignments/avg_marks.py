st = "90,45,68,74,aa,34"
marks = st.split(",")
#print(marks)
total = 0
for m in marks:
    total += int(m)

print(total // len(marks))


