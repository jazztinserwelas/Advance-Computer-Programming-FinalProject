import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("StepUp Job-Matching Platform")
root.geometry("800x600")
root.resizable(True, True)

# Set the background color of the root window
root.config(bg="blue")

# Dictionary of jobs per municipalities (4 jobs per municipalities)
job_dict = {
    "Agoncillo": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Alitagtag": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Balayan": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Balete": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Batangas": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Bauan": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Calaca": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Calatagan": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Cuenca": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Ibaan": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Laurel": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Lemery": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Lian": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Lobo": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Mabini": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Malvar": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Mataasnakahoy": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Nasugbu": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Padre Garcia": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Rosario": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "San Jose": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "San Juan": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "San Luis": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "San Nicolas": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "San Pascual": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Santa Teresita": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Santo Tomas": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Taal": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Talisay": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Tanauan": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Taysan": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ],
    "Tingloy": [
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Warehouse Assistant", "Salary": "₱600/day", "Skills": "Organization, physical strength"},
        {"Title": "Driver", "Salary": "₱600/day", "Skills": "Driving, navigation"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"}
    ],
    "Tuy": [
        {"Title": "House Cleaner", "Salary": "₱500/day", "Skills": "Basic cleaning, time management"},
        {"Title": "Store Assistant", "Salary": "₱550/day", "Skills": "Customer service, organization"},
        {"Title": "Delivery Rider", "Salary": "₱700/day", "Skills": "Driving, route planning"},
        {"Title": "Factory Worker", "Salary": "₱500/day", "Skills": "Assembly, physical labor"}
    ]
}

# List of Municipalities in the Batangas 
municipalities = list(job_dict.keys())

# Function to filter jobs by location
def get_jobs_for_location(location):
    return job_dict.get(location, [])

# Home Page
home_frame = tk.Frame(root, bg="blue")
home_frame.pack(expand=True)

# Title
title_label = tk.Label(home_frame, text="StepUp: Job-Matching Platform", font=("Impact", 30, "bold"), fg="yellow", bg="blue")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Input Fields for Name, Address, Phone Number, and Age
name_label = tk.Label(home_frame, text="Name:", font=("Courier", 12), fg="white", bg="red")
name_label.grid(row=1, column=0, sticky="e", padx=10, pady=5)
name_entry = tk.Entry(home_frame, font=("Courier", 12))
name_entry.grid(row=1, column=1, padx=10, pady=5)

address_label = tk.Label(home_frame, text="Address:", font=("Courier", 12), fg="white", bg="red")
address_label.grid(row=2, column=0, sticky="e", padx=10, pady=5)
address_entry = tk.Entry(home_frame, font=("Arial", 12))
address_entry.grid(row=2, column=1, padx=10, pady=5)

phone_label = tk.Label(home_frame, text="Phone Number:", font=("Courier", 12), fg="white", bg="red")
phone_label.grid(row=3, column=0, sticky="e", padx=10, pady=5)
phone_entry = tk.Entry(home_frame, font=("Arial", 12))
phone_entry.grid(row=3, column=1, padx=10, pady=5)

age_label = tk.Label(home_frame, text="Age:", font=("Courier", 12), fg="white", bg="red")
age_label.grid(row=4, column=0, sticky="e", padx=10, pady=5)
age_entry = tk.Entry(home_frame, font=("Arial", 12))
age_entry.grid(row=4, column=1, padx=10, pady=5)

# Dropdown for Location Selection with Default Value
location_label = tk.Label(home_frame, text="Select Location:", font=("Courier", 12), fg="white", bg="red")
location_label.grid(row=5, column=0, sticky="e", padx=10, pady=5)

location_var = tk.StringVar(value=municipalities[0])  # Default selection is the first municipality
location_dropdown = tk.OptionMenu(home_frame, location_var, *municipalities)
location_dropdown.grid(row=5, column=1, padx=10, pady=5)

# Button to View Available Jobs
go_to_jobs_button = tk.Button(home_frame, text="PROCEED", font=("Tahoma", 14), width=20, command=lambda: go_to_jobs_page())
go_to_jobs_button.grid(row=6, column=0, columnspan=2, pady=20)

# Function to validate inputs
def validate_inputs():
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    age = age_entry.get()

    if not name or not address or not phone or not age:
        messagebox.showerror("Input Error", "All fields are required. Please fill in all the fields.")
        return False

    if not phone.isdigit() or len(phone) != 11:
        messagebox.showerror("Input Error", "Phone number must be 11 digits and numeric.")
        return False

    if not age.isdigit() or int(age) < 18:
        messagebox.showerror("Input Error", "Age must be at least 18 and numeric.")
        return False
    
    return True

# Function to move to jobs page after validation
def go_to_jobs_page():
    if validate_inputs():  # Only proceed if validation is successful
        home_frame.pack_forget()  # Hide home page
        jobs_page_frame.pack(expand=True)  # Show jobs page and ensure it takes full space

# Jobs Page (Second Page)
jobs_page_frame = tk.Frame(root, bg="blue")

# Title for Jobs Page
title_jobs_label = tk.Label(jobs_page_frame, text="AVAILABLE LOCAL JOBS IN YOUR CHOSEN LOCATION", font=("Impact", 30, "bold"), fg="yellow", bg="blue")
title_jobs_label.grid(row=0, column=0, columnspan=2, pady=20)

# Job Buttons Frame (Dynamic Content for Jobs)
job_buttons_frame = tk.Frame(jobs_page_frame, bg="blue")
job_buttons_frame.grid(row=1, column=0, columnspan=2, pady=20)

# Job Details Frame (To show job details dynamically)
job_details_frame = tk.Frame(jobs_page_frame, bg="blue")
job_details_frame.grid(row=2, column=0, columnspan=2, pady=20)

# Function to show jobs in the selected location
def show_jobs_in_location(location):
    jobs_in_location = get_jobs_for_location(location)

    # Clear existing job details
    for widget in job_buttons_frame.winfo_children():
        widget.destroy()

    # Clear the previous job details section
    for widget in job_details_frame.winfo_children():
        widget.destroy()

    # Display available jobs in the selected location
    for i, job in enumerate(jobs_in_location):
        # Job Title
        job_button = tk.Button(job_buttons_frame, text=job["Title"], font=("Courier", 12), fg="white", bg="red", 
                               command=lambda job=job: display_job_details(job))
        job_button.grid(row=i, column=0, padx=10, pady=5, sticky="w")

# Function to display job details
def display_job_details(job):
    # Clear the previous job details
    for widget in job_details_frame.winfo_children():
        widget.destroy()

    # Display the selected job details
    job_title_label = tk.Label(job_details_frame, text=f"Job Title: {job['Title']}", font=("Courier", 14), fg="white", bg="blue")
    job_title_label.grid(row=0, column=0, padx=10, pady=5)

    job_salary_label = tk.Label(job_details_frame, text=f"Salary: {job['Salary']}", font=("Courier", 12), fg="white", bg="blue")
    job_salary_label.grid(row=1, column=0, padx=10, pady=5)

    job_skills_label = tk.Label(job_details_frame, text=f"Skills: {job['Skills']}", font=("Courier", 12), fg="white", bg="blue")
    job_skills_label.grid(row=2, column=0, padx=10, pady=5)

    # Apply Button for each job
    apply_button = tk.Button(job_details_frame, text="Apply", font=("Verdana", 14), width=20, 
                              command=lambda job=job: go_to_apply_page(job))
    apply_button.grid(row=3, column=0, padx=10, pady=5)

# Function to go to the Apply Page with job details
selected_job = None  # Global variable to store the selected job

def go_to_apply_page(job):
    global selected_job
    selected_job = job  # Store the selected job
    jobs_page_frame.pack_forget()  # Hide jobs page
    apply_page_frame.pack(expand=True)  # Show apply page

# Apply Page (Third Page)
apply_page_frame = tk.Frame(root, bg="blue")

# Apply Page Title
apply_title_label = tk.Label(apply_page_frame, text="Thank you for applying!", font=("Courier", 18, "bold"), fg="yellow", bg="blue")
apply_title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Apply Page Message
apply_message_label = tk.Label(apply_page_frame, text="We appreciate your interest in this job.\nOur team will get in touch with you soon.\nThank you for using StepUp!", font=("Arial", 14), fg="white", bg="blue", justify="center")
apply_message_label.grid(row=1, column=0, columnspan=2, pady=20)

# Display selected job details
def display_apply_page():
    if selected_job:
        apply_message_label.config(
            text=f"Job Title: {selected_job['Title']}\n"
                 f"Salary: {selected_job['Salary']}\n"
                 f"Skills: {selected_job['Skills']}")

# Thank You Button (Exit)
thank_you_button = tk.Button(apply_page_frame, text="Done!", font=("Arial", 14), width=20, command=root.quit)
thank_you_button.grid(row=2, column=0, columnspan=2, pady=20)

# Back Button to Home
back_button = tk.Button(apply_page_frame, text="Back to Home", font=("Arial", 14), width=20, command=lambda: go_back_home())
back_button.grid(row=3, column=0, columnspan=2, pady=20)

# Function to go back to the home page
def go_back_home():
    apply_page_frame.pack_forget()  # Hide apply page
    home_frame.pack(expand=True)   # Show home page

# Initially show jobs for the default selected location
location_var.trace("w", lambda *args: show_jobs_in_location(location_var.get()))
show_jobs_in_location(municipalities[0])  # Show jobs for the first municipality

# Run the Tkinter event loop
root.mainloop()