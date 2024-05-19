import requests
a=requests.get("https://reqres.in/api/users/")
# print(a)
# print(a.status_code)
# print(a.json())
s=a.json()["data"]
with open("../api_data.txt", "w") as f:
    is_header=True
    for i in s:
        if is_header==True:
            f.write(" ".join(i.keys()) + "\n")
            is_header=False
        f.write(" ".join(map(lambda x:str(x),i.values())) + "\n")


