import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime, timedelta
import os
import json
import csv



def check_availability():
    # Get the selected dates from the calendars
    start_date_str = start_calendar.get_date()
    end_date_str = end_calendar.get_date()

    # Convert string dates to datetime objects
    start_date = datetime.strptime(start_date_str, "%m/%d/%y")
    end_date = datetime.strptime(end_date_str, "%m/%d/%y")

    # Generate the list of dates in the range
    date_range = [(start_date + timedelta(days=i)).strftime("%m/%d/%y") for i in range((end_date - start_date).days + 1)]

    # Read and check JSON files
    scheduling_folder = r"D:\Python Files\scheduling\ipads"
    available_ipads = []

    for file_name in os.listdir(scheduling_folder):
        if file_name.endswith(".json"):
            ipad_path = os.path.join(scheduling_folder, file_name)

            with open(ipad_path, "r") as file:
                try:
                    data = json.load(file)
                    if not data:  # If the file is blank or empty
                        available_ipads.append(file_name.replace(".json", ""))
                        continue

                    # Check for any events that overlap with the selected date range
                    booked_dates = data.get("booked_dates", [])
                    conflict = any(date in booked_dates for date in date_range)

                    if not conflict:
                        available_ipads.append(file_name.replace(".json", ""))

                except json.JSONDecodeError:
                    # Treat as no bookings if the file is invalid
                    available_ipads.append(file_name.replace(".json", ""))

    # Create the quantity selection window if there are available iPads
    if available_ipads:
        available_count = len(available_ipads)
        message = f"Available iPads for the selected dates: {available_count}"

        def get_required_quantity():
            required_quantity = quantity_var.get()
            if required_quantity > available_count:
                messagebox.showerror("Error", f"Cannot select more than {available_count} iPads.")
            else:
                # Get Name, Event, Address from the entry fields
                name = name_entry.get()
                event = event_entry.get()
                address = address_entry.get()

                if not name or not event or not address:
                    messagebox.showerror("Error", "All fields (Name, Event, Address) must be filled in.")
                else:
                    # Store the data in the selected iPads JSON files
                    for ipad_name in available_ipads[:required_quantity]:
                        ipad_file_path = os.path.join(scheduling_folder, f"{ipad_name}.json")

                        # Load existing data from the iPad file
                        with open(ipad_file_path, "r") as file:
                            ipad_data = json.load(file)

                        # Ensure the 'booked_dates' field exists
                        if "booked_dates" not in ipad_data:
                            ipad_data["booked_dates"] = []

                        # Append the new event's dates to the 'booked_dates' list
                        ipad_data["booked_dates"].extend(date_range)

                        # Also store the event data (Name, Event, Address)
                        event_data = {
                            "name": name,
                            "event": event,
                            "address": address,
                            "dates": date_range
                        }

                        # Append the event data to the list of events
                        if "events" not in ipad_data:
                            ipad_data["events"] = []
                        ipad_data["events"].append(event_data)

                        # Save the updated data back to the iPad's JSON file
                        with open(ipad_file_path, "w") as file:
                            json.dump(ipad_data, file, indent=4)

                    messagebox.showinfo("Success", f"You have selected {required_quantity} iPads.\n"
                                                  f"Name: {name}\nEvent: {event}\nAddress: {address}\n"
                                                  f"Dates: {', '.join(date_range)}")
            generate_calendar_csv()

        # Display the available iPads message and quantity selection in the same window
        quantity_window = tk.Toplevel(root)
        quantity_window.title("Select Quantity")

        # Display the availability message
        availability_label = tk.Label(quantity_window, text=message)
        availability_label.pack(padx=10, pady=10)

        # Create a dropdown for selecting the quantity
        quantity_var = tk.IntVar(value=1)  # Default value
        dropdown = tk.OptionMenu(quantity_window, quantity_var, *range(1, available_count + 1))
        dropdown.pack(padx=10, pady=10)

        # Add text fields for Name, Event, Address
        name_label = tk.Label(quantity_window, text="Name:")
        name_label.pack(padx=10, pady=5)
        name_entry = tk.Entry(quantity_window)
        name_entry.pack(padx=10, pady=5)

        event_label = tk.Label(quantity_window, text="Event:")
        event_label.pack(padx=10, pady=5)
        event_entry = tk.Entry(quantity_window)
        event_entry.pack(padx=10, pady=5)

        address_label = tk.Label(quantity_window, text="Address:")
        address_label.pack(padx=10, pady=5)
        address_entry = tk.Entry(quantity_window)
        address_entry.pack(padx=10, pady=5)

        # Add a submit button
        submit_button = tk.Button(quantity_window, text="Submit", command=get_required_quantity)
        submit_button.pack(padx=10, pady=10)

    else:
        message = "No iPads are available for the selected dates."
        messagebox.showinfo("Availability", message)

import os
import json
import csv
from tkinter import messagebox

def generate_calendar_csv():
    # Get all the dates and booked iPads
    scheduling_folder = r"D:\Python Files\scheduling\ipads"
    ipad_bookings = {}

    # Create a set to track all booked dates across all iPads
    all_booked_dates = set()

    # Read the JSON files for all iPads
    for file_name in os.listdir(scheduling_folder):
        if file_name.endswith(".json"):
            ipad_path = os.path.join(scheduling_folder, file_name)

            with open(ipad_path, "r") as file:
                try:
                    data = json.load(file)
                    booked_dates = data.get("booked_dates", [])

                    # Store the booked dates for the specific iPad
                    ipad_name = file_name.replace(".json", "")
                    ipad_bookings[ipad_name] = booked_dates

                    # Add the booked dates to the set of all booked dates
                    all_booked_dates.update(booked_dates)

                except json.JSONDecodeError:
                    continue

    # Sort the dates in ascending order
    all_booked_dates = sorted(all_booked_dates)

    # Define the primary and backup paths
    primary_path = r"G:\共有ドライブ\JP - Tech - Service Desk\07 - Projects\POS Schedule"
    backup_path = r"G:\My Drive\JP - Tech - Service Desk\07 - Projects\POS Schedule"

    # Check if the primary path exists, otherwise use the backup path
    if os.path.exists(primary_path):
        save_path = primary_path
    else:
        save_path = backup_path

    # Define the full file path for saving the CSV
    csv_file_path = os.path.join(save_path, "ipad_availability.csv")

    # Create a CSV file to display availability
    with open(csv_file_path, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header row: "Date", followed by iPad names
        header = ["Date"] + list(ipad_bookings.keys())
        writer.writerow(header)

        # Write rows for each date
        for booked_date in all_booked_dates:
            row = [booked_date]

            # For each iPad, check if it's booked for this date
            for ipad_name, booked_dates in ipad_bookings.items():
                if booked_date in booked_dates:
                    row.append("Booked")
                else:
                    row.append("Available")

            # Write the row to the CSV file
            writer.writerow(row)

    print("CSV Generated", f"CSV file generated successfully at {csv_file_path}")

generate_calendar_csv()

# Create the main application window
root = tk.Tk()
root.title("Date Range Selector")
root.geometry("550x400")

# Create a frame to organize calendars side by side
calendar_frame = tk.Frame(root)
calendar_frame.pack(pady=10)

# Label and start date calendar on the left
start_label = tk.Label(calendar_frame, text="Select Start Date:")
start_label.grid(row=0, column=0, padx=10, pady=5)
start_calendar = Calendar(calendar_frame, selectmode="day")
start_calendar.grid(row=1, column=0, padx=10, pady=5)

# Label and end date calendar on the right
end_label = tk.Label(calendar_frame, text="Select End Date:")
end_label.grid(row=0, column=1, padx=10, pady=5)
end_calendar = Calendar(calendar_frame, selectmode="day")
end_calendar.grid(row=1, column=1, padx=10, pady=5)

# Button to check availability
check_button = tk.Button(root, text="Check Availability", command=check_availability)
check_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
