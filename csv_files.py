import csv
# with open("data.csv", "r") as fdr:
#     students= csv.reader(fdr)
#     for student in students:
#         print(student)
single_student=["Urooj", "AI", "3:30-6:30"]
students=[
    ["Urooj", "AI", "3:30-6:30"],
    ["Urooj", "AI", "3:30-6:30"],
    ["Urooj", "AI", "3:30-6:30"]
]
print(single_student)
with open("data.csv", "w",newline='') as f:
    writer=csv.writer(f,delimiter=',')
    for student in students:
        writer.writerow(student)