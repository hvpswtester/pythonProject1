import requests

def create_user(firstname, lastname, email, url):
    data = {
        'firstname': firstname,
        'lastname': lastname,
        'email': email
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for any errors in the response
        # print("response ", response)
        return response.json()  # Return the JSON response data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

def main():
    # Get user input
    firstname = input("Enter First Name: ")
    lastname = input("Enter Last Name: ")
    email = input("Enter email: ")
    url = 'https://reqres.in/api/users'

    # Create the user using the API
    result = create_user(firstname, lastname, email, url)
    print("result ", result)

    if result is not None:
        print("User created successfully!")
        print("User details:")
        print(f"ID: {result['id']}")
        print(f"Firstname: {result['firstname']}")
        print(f"Lastname: {result['lastname']}")
        print(f"Email: {result['email']}")
        # print(f"Created At: {result['created_at']}")
    else:
        print("Failed to create user.")

if __name__ == "__main__":
    main()