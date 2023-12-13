st = "90,a1,45,68,74,aa,34"
marks = st.split(",")
# print(marks)
total = count = 0
for m in marks:
    if m.isdigit():
        total += int(m)
        count += 1

print(total // count)
