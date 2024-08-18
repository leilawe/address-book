file=open("my_text.txt", "r")

content=file.read()
print(content)


# file=open("my_text.txt", "w")
# file.write("avaz shod")

file=open("my_text.txt", "a")
file.write("\nin khat taze ezafe shode")