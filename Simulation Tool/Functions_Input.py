import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from ttkthemes import ThemedTk

#################################################################################################################

# Define interim functions for loading and saving input values from GUI.

# Load previously submitted values from a natural_frequencies.txt
def load_values_freq(entry_var_frequencies):
    config_file = "natural_frequencies.txt"
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            lines = file.readlines()
            if len(lines) == 9:
                for i in range(9):
                    entry_var_frequencies[i].delete(0, tk.END) # Clear the entry field
                    entry_var_frequencies[i].insert(0, lines[i].strip()) # Set the value from the file to the entry field

# Save currently entered values to natural_frequencies.txt
def save_values_freq(entry_var_frequencies):
    config_file = "natural_frequencies.txt"
    with open(config_file, "w") as file:
        for entry in entry_var_frequencies:
            value = entry.get()
            file.write(f"{value}\n")

# Load previously submitted values from a participation_factors.txt
def load_values_fac(entry_var_factors):
    config_file = "participation_factors.txt"
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            lines = file.readlines()
            if len(lines) == 9:
                for i in range(9):
                    entry_var_factors[i].delete(0, tk.END) # Clear the entry field
                    entry_var_factors[i].insert(0, lines[i].strip()) # Set the value from the file to the entry field

# Save currently entered values to participation_factors.txt
def save_values_fac(entry_var_factors):
    config_file = "participation_factors.txt"
    with open(config_file, "w") as file:
        for entry in entry_var_factors:
            value = entry.get()
            file.write(f"{value}\n")

# Load previously submitted values from a address.txt
def load_values_address(entry_var_address):
    config_file = "address.txt"
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as file:
            value = file.read()
            entry_var_address.delete(0, tk.END)  # Clear the entry field
            entry_var_address.insert(0, value)  # Set the value from the file to the entry field

# Save currently entered values to address.txt
def save_values_address(entry_var_address):
    config_file = "address.txt"
    value = entry_var_address.get()  # Get the string value from the entry field
    with open(config_file, "w", encoding="utf-8") as file:
        file.write(value)

#################################################################################################################

# Function 1: Create a Graphical User Interface (GUI) for the inputs
def input_gui(callback):
    
    def upload_files():
        files = filedialog.askopenfilenames(title="Select Files to Upload")
        # Ensure a directory for file uploads exists
        upload_dir = 'Eigenmode Vectors'
        os.makedirs(upload_dir, exist_ok=True)
        for file in files:
            file_name = os.path.basename(file)
            destination = os.path.join(upload_dir, file_name)
            # Check if the file already exists, and ask for confirmation to overwrite
            if os.path.exists(destination):
                response = messagebox.askyesno("File Overwrite", f"Do you want to overwrite {file_name}?")
                if response:
                    os.replace(file, destination)
            else:
                os.replace(file, destination)

    def set_global_vars():
        var_earthquake = str(entry_var_earthquake.get())
        var_frequencies = [entry.get() for entry in entry_var_frequencies]
        var_factors = [entry.get() for entry in entry_var_factors]
        var_address = entry_var_address.get()

        var_earthquake = int(values_map.get(var_earthquake))
        var_frequencies = [float(item) for item in var_frequencies]
        var_factors = [float(item) for item in var_factors]

        # Set the global variables
        callback(var_earthquake, var_frequencies, var_factors, var_address)

        root.destroy()



    # Create the main gui window
    root = ThemedTk(theme="ubuntu")
    root.title("Response Map Simulation: INPUT")  # Set title for the window
    # Create a style for modern appearance for the gui
    style = ttk.Style()
    style.configure('Custom.TButton', font=('Arial', 10), padding=10)
    # Create the main frame from the gui
    frame = ttk.Frame(root)
    frame.grid(padx=10, pady=10)
    # The title/introduction for the gui
    intro_label = ttk.Label(frame, text="Please choose and provide the necessary variables and values to initiate the simulation", font=("Arial", 12))
    intro_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")



    # To fit as wanted, create a seperate frame for earthquake input
    earth_frame = ttk.Frame(frame, borderwidth=5)
    earth_frame.grid(row=1, column=0, sticky="ew")
    # Add the label
    earthquake_label = ttk.Label(earth_frame, text="Please choose one of the possible (stored) earthquakes:", font=("Arial", 10))
    earthquake_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
    # Create the combobox for the earthquakes list
    values_map = {
    "MW 4.6": 0,
    "MW 4.7": 1,
    "MW 7.7 (2023)" : 2,
    "MW 4.1": 3,
    "MW 4.9": 4,
    "MW 4.2": 5,
    "(Bolu Merkez) MW 7.1": 6,
    "(Düzce Merkez) MW 7.1": 7,
    "MW 5.8": 8,
    "ML 4.5": 9,
    "MD 3.6": 10,
    "(Düzce Merkez) MW 7.6": 11,
    "(Gebze) MW 7.6": 12,
    "(Izmit) MW 7.6": 13,
    "MW 4.5": 14,
    }
    entry_var_earthquake = ttk.Combobox(earth_frame, values=list(values_map.keys()))
    entry_var_earthquake.grid(row=1, column=3, columnspan =3, sticky="ew", padx=10, pady=10)
    entry_var_earthquake.current(2) # Item with index 2 is the initially selected item



    # Create a seperate frame to enclose the Karamba inputs
    karamba_frame = ttk.Frame(frame, borderwidth=5, relief="sunken")
    karamba_frame.grid(row=2, column=0, columnspan=10, rowspan=7, padx=10, pady=10)
    # Add the frame label
    title_label = ttk.Label(karamba_frame, text="To complete the values, please consult the Karamba example file in Grasshopper.", font=("Arial", 10, "bold"))
    title_label.grid(row=2, column=0, columnspan=9, sticky="ew", padx=10, pady=10)



    # Add the natural frequencies input label
    frequency_label = ttk.Label(karamba_frame, text="Provide the natural frequency (Hz) of each archetype:", font=("Arial", 10))
    frequency_label.grid(row=3, column=0, columnspan=10, sticky="ew", padx=10, pady=10)  # Use padx and pady for spacing
    # Create and position small text labels above the entries
    labels = ['Architype 1a', 'Architype 1b', 'Architype 1c', 'Architype 2a', 'Architype 2b', 'Architype 2c', 'Architype 3a', 'Architype 3b', 'Architype 3c']
    for i, label_text in enumerate(labels):
        label = ttk.Label(karamba_frame, text=label_text, font=("Arial", 8))
        label.grid(row=4, column=i, pady=5)  # Use pady to add space between the label and entry
    # Create 9 entry fields for the natural frequencies
    entry_var_frequencies = []
    for i in range(9):
        entry = ttk.Entry(karamba_frame)
        entry.grid(row=5, column=i, padx=10)
        entry_var_frequencies.append(entry)
    # Load previously submitted values
    load_values_freq(entry_var_frequencies)
    # Save Button
    save_button = ttk.Button(karamba_frame, text="Save Values", command=lambda: save_values_freq(entry_var_frequencies))
    save_button.grid(row=5, column=10)

 
 
    # Add the natural frequencies input label
    factors_label = ttk.Label(karamba_frame, text="Provide the participation factor of each archetype:", font=("Arial", 10))
    factors_label.grid(row=6, column=0, columnspan=10, sticky="ew", padx=10, pady=10)  # Use padx and pady for spacing
    # Create and position small text labels above the entries
    labels = ['Architype 1a', 'Architype 1b', 'Architype 1c', 'Architype 2a', 'Architype 2b', 'Architype 2c', 'Architype 3a', 'Architype 3b', 'Architype 3c']
    for i, label_text in enumerate(labels):
        label = ttk.Label(karamba_frame, text=label_text, font=("Arial", 8))
        label.grid(row=7, column=i, pady=5)  # Use pady to add space between the label and entry
    # Create 9 entry fields for the participation factors
    entry_var_factors = []
    for i in range(9):
        entry = ttk.Entry(karamba_frame)
        entry.grid(row=8, column=i)
        entry_var_factors.append(entry)
    # Load previously submitted values
    load_values_fac(entry_var_factors)
    # Save Button
    save_button = ttk.Button(karamba_frame, text="Save Values", command=lambda: save_values_fac(entry_var_factors))
    save_button.grid(row=8, column=10)



    # Add the vibration shape input label
    upload_label = ttk.Label(karamba_frame, text="Please upload the CSV-formatted vibration shape files to the specified directory. Please ensure that the file names adhere to the archetype numbering convention:", font=("Arial", 10))
    upload_label.grid(row=10, column=0, columnspan=7, sticky="ew", padx=10, pady=25)  
    # Create the the upload Button with label "Insert Files"
    upload_button = ttk.Button(karamba_frame, text="Insert Files", command=upload_files)
    upload_button.grid(row=10, column=7)



    # Add the address input label
    address_label = ttk.Label(frame, text="Enter the precise address to view the neighborhood within a 1000-meter radius:", font=("Arial", 10))
    address_label.grid(row=11, column=0, columnspan=10, sticky="ew", padx=10, pady=10) 
    # Create entry field for an address
    entry_var_address = ttk.Entry(frame)
    entry_var_address.grid(row=12, column=0, columnspan=5, sticky="ew", padx=10,)
    # Load previously submitted address
    load_values_address(entry_var_address)
    # Save Button
    save_button = ttk.Button(frame, text="Save Address", command=lambda: save_values_address(entry_var_address))
    save_button.grid(row=12, column=5)



    # Add the warning/check label
    run_label = ttk.Label(frame, text="Before submitting, please verify that all values and variables are correctly set", font=("Arial", 10, "bold"))
    run_label.grid(row=15, column=0, columnspan=10, padx=10, pady=10)  # Use padx and pady for spacing
    # SIMULATION RUN BUTTON
    update_button = ttk.Button(frame, text="Submit Variables", style='TButton', command=set_global_vars)
    update_button.grid(row=16, column=0, columnspan=10)



    root.mainloop()