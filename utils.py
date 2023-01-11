import requests, json

url = "http://localhost:9190/proxies"

## Define function to call api
def request(api):
    request_url = f"{url}/{api}"
    response = requests.get(request_url)
    data = response.json()
    return data


def request_suggested():
    data = request("自动选择")
    suggeested = data["now"]
    return suggeested


def select_global_proxy(proxy_name):
    print("select proxy ", proxy_name)
    request_url = f"{url}/GLOBAL"
    data = '{"name": "' + proxy_name + '"}'
    response = requests.put(request_url, data=data.encode("utf-8"))
    return response.status_code
