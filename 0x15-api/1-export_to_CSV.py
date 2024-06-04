import csv
import requests
import sys

if __name__ == "__main__":
    # Ensure correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command-line arguments
    employee_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information from the API and convert the response to a JSON object
    user_response = requests.get(f"{url}users/{employee_id}")
    user_data = user_response.json()

    # Extract the username from the user data
    username = user_data.get("username")

    # Fetch the to-do list items associated with the given user ID
    # and convert the response to a JSON object
    todo_response = requests.get(f"{url}todos", params={"userId": employee_id})
    todos = todo_response.json()

    # Write the to-do list items to a CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write header row
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        # Write each task as a row in the CSV file
        for todo in todos:
            writer.writerow([employee_id, username, todo["completed"], todo["title"]])

    print(f"Data exported to {csv_filename}")
