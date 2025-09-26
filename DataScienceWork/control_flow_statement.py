# conditional statement
# >, >=, <, <=, ==, !=
'''
x = 10
if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")

else:
    print("x is Zero") 

   # for loops 

menu = ["Dahi Bhallay","Baryani","Daal", "Samoasy"," shami","Paneer"]
for food in menu:
    print(food) 

    

 # while Loop

i = 1
while i <= 6:
    print(i)
    i+=1
    if i == 3:
        break
        

for latters in "Python":
    if latters == "h":
        break #control statement break
    print(latters,end="")
    

for latters in "Python":
    if latters == "h":
        continue #control statement continue
    print(latters,end="")


for latters in "Python":
    if latters == "h":
        pass #control statement pass
    print(latters,end="")
'''

# Nested loops (loop ky ander loop)

'''   # Nested for loops

colors = ["red","blue","green"]
items = ["book","pen","copy"]

for color in colors:
    for item in items:
        print(color , item )


     # Nested while loops

i =  0
while i < 3:
    j = 0
    while j < 3:
        print(i,j)
        j +=1
    i +=1
 

    # for loop inside while loop
i = 1
while i < 4:
    for j in range(3):
        print(i,j)
    i +=1
'''
    # while loop inside for loop (assingment)

for j in range(1,3,1):
    i = 1
    while i < 4:
        print(i,j)
        i +=1

