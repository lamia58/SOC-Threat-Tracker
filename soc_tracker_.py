
import csv

incidents = {}
logs = []


def add_incident():
    number = input("Enter incident ID: ")
    ip = input("Enter IP address: ")
    attack = input("Enter attack type: ")
    level = input("Enter level (low/medium/high): ")

    if number == "" or ip == "" or attack == "":
        print("Please fill in all details.")

    elif number in incidents:
        print("This ID already exists.")

    elif level not in ["low", "medium", "high"]:
        print("Wrong level!")

    else:
        incidents[number] = [ip, attack, level]
        logs.append(number)
        print("Incident added!")


def view_incidents():
    if len(incidents) == 0:
        print("No incidents found.")
    else:
        for number in incidents:
            print(number, incidents[number])


def view_logs():
    if len(logs) == 0:
        print("No logs found.")
    else:
        for log in logs:
            print(log)


def save_data():
    with open("logs.csv", "w", newline="") as file:
        writer = csv.writer(file)
        for number in incidents:
            writer.writerow([number] + incidents[number])
    print("Data saved!")


def load_data():
    try:
        with open("logs.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                number = row[0]
                incidents[number] = row[1:]
                logs.append(number)
    except FileNotFoundError:
        print("No saved data yet.")


load_data()

while True:
    print("\n--- SOC Dashboard ---")
    print("1. Add Incident")
    print("2. View Incidents")
    print("3. View Logs")
    print("4. Save and Exit")
    print("5. Exit without saving")

    choice = input("Choose: ")

    if choice == "1":
        add_incident()
    elif choice == "2":
        view_incidents()
    elif choice == "3":
        view_logs()
    elif choice == "4":
        save_data()
        break
    elif choice == "5":
        print("Exiting without saving.")
        break
    else:
        print("Wrong choice!")
