
user_info1={
"name": "leila",
"last_name": "weisi",
"age": "23"
}

user_info2={
"name": "hesam",
"last_name": "shakiba",
"age": "27"
}
user_info1["age"]="22"
print(user_info1, user_info2)

user_infos=[]
user_infos.append(user_info1)
user_infos.append(user_info2)
print(user_infos)


for key, value in user_infos.item():
    print(f"your{key} is: {value}")