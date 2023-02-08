#!/usr/bin/python3
"""Using a public API 'https://jsonplaceholder.typicode.com'"""
import requests
import sys

" main function to get to do list and users "
def get_employee_todo_list_progress(employee_id):
    """ 
    Get employee name
    """
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_name = employee_response.json().get("name")

    # get employee todo list
    todo_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_list = todo_response.json()

    # count number of completed and total tasks
    completed_tasks = [task for task in todo_list if task["completed"]]
    total_tasks = len(todo_list)
    completed_tasks_count = len(completed_tasks)

    # print progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

"""
test with employee id 1
"""
get_employee_todo_list_progress(sys.argv[1])
