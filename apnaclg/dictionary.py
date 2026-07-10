# dict = {
#     # key       Value
#     "name" : "rachit thakur",
#     "subject" : ['py', 'c', 'bio'],
#     "age" : 35,
#     "cgpa" : 9.4,
# }
# print(dict)

info = {
    "name" : "rachitv thakur",
    "subject" :{
        "py" : 45,
        "chem" :55,
        "bio" : 60,
    },
    "age": 20,
}
print(info)
info["name"] = "Rachit Thakur"
info["Address"] = "Nanauta"
print(info)

print(info.keys())
print(info.items())
print(info.get("name"))
print(len(info))
print(list(info.values()))




