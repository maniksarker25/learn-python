# ,csv comma separated value
#.txt text file
# write
# with open("message.txt","w") as file:
#     file.write("I love you, python!")

# append
# with open("message.txt","a") as file:
#     file.write("I love you, python!")

# read
with open("message.txt","r") as file:
    text = file.read()
    print(text)