import requests
def make_api_call(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error making API call..", e)
        return None

# function call to get the employee
emp_id = input("Please enter Employee ID : ")

if emp_id == None:
    api_url = "https://reqres.in/api/users?page=2"
    # api_url = "https://gorest.co.in/public/v2/users"
else:
    api_url = f"https://reqres.in/api/users/{emp_id}"
    # api_url = f"https://gorest.co.in/public/v2/users/{emp_id}"
result = make_api_call(api_url)

if result:
    if emp_id != None:
        print(result)
    else:
        for emp in result:
            print(emp)
elif result == None:
    print("No such employee exist..")
else:
    print("API call failed..")