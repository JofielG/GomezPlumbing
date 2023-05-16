import tkinter as tk

# Define a dictionary to hold the items and their costs for each job type
service_work_costs = {
    "Pipes": 10,
    "Fittings": 5,
    "Valves": 15,
    "Toilets": 100,
    "Sinks": 50
}

residential_new_construction_costs = {
    "Pipes": 15,
    "Fittings": 8,
    "Valves": 20,
    "Toilets": 120,
    "Sinks": 60
}

commercial_new_construction_costs = {
    "Pipes": 20,
    "Fittings": 10,
    "Valves": 25,
    "Toilets": 150,
    "Sinks": 75
}

industrial_new_construction_costs = {
    "Pipes": 25,
    "Fittings": 12,
    "Valves": 30,
    "Toilets": 200,
    "Sinks": 100
}

septic_tank_installation_costs = {
    "Septic Tank": 500,
    "Drain Field": 1000,
    "Pipes": 50
}

# Define a function to calculate the total cost of the job based on job type and items
def calculate_cost(job_type, items):
    if job_type == "Service Work":
        item_costs = service_work_costs
    elif job_type == "Residential New Construction":
        item_costs = residential_new_construction_costs
    elif job_type == "Commercial New Construction":
        item_costs = commercial_new_construction_costs
    elif job_type == "Industrial New Construction":
        item_costs = industrial_new_construction_costs
    elif job_type == "Septic Tank Installation":
        item_costs = septic_tank_installation_costs
    else:
        print("Invalid job type")
        return 0
    total_cost = 0
    for item, quantity in items.items():
        item_cost = item_costs[item]
        total_cost += item_cost * quantity
    return total_cost

# Define a function to handle the button click event
def calculate_button_click():
    # Get the job type and item quantities from the input fields
    job_type = job_type_entry.get()
    pipes_quantity = int(pipes_entry.get())
    fittings_quantity = int(fittings_entry.get())
    valves_quantity = int(valves_entry.get())
    toilets_quantity = int(toilets_entry.get())
    sinks_quantity = int(sinks_entry.get())
    
    # Create a dictionary of the items and their quantities
    items = {
        "Pipes": pipes_quantity,
        "Fittings": fittings_quantity,
        "Valves": valves_quantity,
        "Toilets": toilets_quantity,
        "Sinks": sinks_quantity
    }

    # Calculate the total cost and display the result
    total_cost = calculate_cost(job_type, items)
    total_cost_label.config(text="Total Cost: ${:.2f}".format(total_cost))

# Create the main window
root = tk.Tk()
root.title("Plumber Job Cost Calculator")

# Create the job type input field and label
job_type_label = tk.Label(root, text="Job Type:")
job_type_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
job_type_entry = tk.Entry(root)
job_type_entry.grid(row=0, column=1, padx=5, pady=5)
