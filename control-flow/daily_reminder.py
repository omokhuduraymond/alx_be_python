task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() 
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} task and requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a {priority} task, consider completing it when you have free time.")
        else:
            print("Invalid input for time-bound field.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} task and requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a {priority} task, consider completing it when you have free time.")
        else:
            print("Invalid input for time-bound field.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} task and requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a {priority} task, consider completing it when you have free time.")
        else:
            print("Invalid input for time-bound field.")
    case _:  
        print("Priority not registered.")

