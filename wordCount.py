sentence = input("Type a sentence ...") 
count = 0
for x in sentence :
    if(x != " "): 
        count = count+1 

print("Number of letters in the snetence you enetered - " , count)