jobtypeRNC = 0

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

# Get user input for the job type
print("1. Service Work")
print("2. New Construction")
print("3. Septic Tanks")
job_type = int(input("What type of job is it? "))

# If the job type is New Construction Job, get user input for the job type
if job_type == 2:
    print("1. Residential")
    print("2. Commercial")
    print("3. Industrial")
    job_type = int(input("What type of new construction job is it? "))

if job_type == 1:
    print("1. Water Service Line")
    print ("2. Sewer Line")
    print("3. Plumbing Rough-In")
    print("4. Plumbing Tap-Out")
    print("5. Plumbing Trim-In")
    print("6. Gas Distribution System")
    jobtypeRNC = int(input("Pick a service: "))

if jobtypeRNC == 1:
    pipesize = int(input("Pipe size: "))
    pipelength = int(input("How many feet of pipe: "))
    glue = int(input("Glue: "))
    fitting = int(input("Fitting:"))




# Get user input for the quantities of each item
pipes_quantity = int(input("How many pipes will be used? "))
fittings_quantity = int(input("How many fittings will be used? "))
valves_quantity = int(input("How many valves will be used? "))
toilets_quantity = int(input("How many toilets will be used? "))
sinks_quantity = int(input("How many sinks will be used? "))

# Create a dictionary of the items and their quantities
items = {
    "Pipes": pipes_quantity,
    "Fittings": fittings_quantity,
    "Valves": valves_quantity,
    "Toilets": toilets_quantity,
    "Sinks": sinks_quantity
}

# Calculate the total cost and print the result
total_cost = calculate_cost(job_type, items)
print("The total cost of the job is:", total_cost)
