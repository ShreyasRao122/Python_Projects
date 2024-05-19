import requests
response=requests.get("https://reqres.in/api/users/")
data=response.json()["data"]
with open("api_data.txt", "w") as f:
    is_header=True
    for item in data:
        if is_header==True:
            f.write(" ".join(item.keys()) + "\n")
            is_header=False
        f.write(" ".join(map(lambda x:str(x),item.values())) + "\n")


