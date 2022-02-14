grade = {"python":[10], "Java":[5]}
# z = sum(grade.values())
# print(z)
print(list(grade.values()))
z =0
x =0
for i in list(grade.values()):
    z += sum(i)
    x += len(i)
print(z/x)


#grade_val = sum(grade.values())/len(grade.values())
# print(grade_val)