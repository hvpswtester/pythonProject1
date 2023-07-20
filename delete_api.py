import requests

def delete_api_call_emp(url):
    try:
        response = requests.delete(url)

        if response.status_code == 204:  # 204 No Content indicates successful deletion
            print("Record successfully deleted.")
        else:
            print(f"Failed to delete the Record. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print("Error making API call..", e)

# function call to delete the employee
emp_id = input("Please enter Employee ID you want to delete :")
# api_url = f"https://gorest.co.in/public/v2/todos/{emp_id}"
api_url = f"https://reqres.in/api/users/{emp_id}"
delete_api_call_emp(api_url)
