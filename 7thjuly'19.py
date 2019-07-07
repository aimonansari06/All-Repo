alien={"hey":"ola", "how are you":"baa bdu bi", "bye":"guxs", "planet?":"okhel"}
Humans={"ola": "hey", "baa bdu bi": "how are you", "guxs":"bye","okhel":"planet?"}
inp=input("are you human//jaaduu: ")
if inp=="yes":
    data=input("ask question: ")
    for i in alien:
            if data==i:
                print("***Transalated***")
                print(alien[i])
elif inp=="no":
    data1=input("arh hddik: ")
    for x in Humans:
        if data1==x:
            print("***YRCJSJHSB***")
            print(Humans[x])             
    