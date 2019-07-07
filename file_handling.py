with open("names.txt","w") as f:
    f.write("AIMON\n")
    f.write("AREEBA")

with open("names.txt", "a") as f:
    f.write("\nUrooj")
with open("names.txt","r") as f:
    data=f.read()
    print(data)

