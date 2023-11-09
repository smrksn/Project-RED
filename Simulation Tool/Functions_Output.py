import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import subprocess

# Function 1: Create a Graphical User Interface (GUI) for the outputs
def output_gui():

    # Define a function to display images and associated text.
    def display_images_and_text():
        image_labels = []  # Keep references to image labels
        text_labels = []   # Keep references to text labels
        
        for i, path in enumerate(image_paths):
            if not os.path.exists(path):
                print(f"Image file does not exist: {path}")
                continue
            img = Image.open(path)           
            # Resize the image
            new_width = 500
            original_width, original_height = img.size
            new_height = int((new_width / original_width) * original_height)
            img = img.resize((new_width, new_height))           
            # Convert the image to a format compatible with tkinter
            img_tk = ImageTk.PhotoImage(img)      
            # Create a label to display the image in the current column
            figure_label = tk.Label(frame, image=img_tk)
            figure_label.image = img_tk  # Keep a reference to the image to prevent it from being garbage collected
            figure_label.grid(row=0, column=i, padx=10, pady=10)  # Add padding for spacing
            image_labels.append(figure_label)
            
            # Create a frame to enclose the text label
            text_frame = ttk.Frame(frame, height = 500, borderwidth=2, relief="sunken")
            text_frame.grid(row=1, column=i, padx=10, pady=10)
            # Add explanatory text below the image and wrap it
            text_label = ttk.Label(text_frame, text=texts[i], wraplength=400)
            text_label.pack(padx=5, pady=5)
            text_labels.append(text_label)



    # Define a function to open a folder in the file explorer.
    def open_folder():
        folder_path = os.path.join('.', 'Outputs')
        if os.path.exists(folder_path):
            try:
                with subprocess.Popen(['explorer', folder_path], shell=True):
                    pass  # Do nothing, just wait for the subprocess to finish
            except Exception as e:
                print(f"Failed to open the folder: {e}")
        else:
            print("Folder does not exist.")



    # Define a function to handle GUI window closing.
    def on_closing():
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.quit()  # Stop the main loop
            root.destroy()  # Destroy the window



    # Create a new top-level GUI window for displaying simulation output.
    root = tk.Toplevel()
    root.title("Response Map Simulation: OUTPUT")
    frame = ttk.Frame(root)
    frame.grid(padx=10, pady=10)  # Use grid manager



    # Define image paths for Risk and Neighborhood Maps.
    image_path_1 = os.path.join('./Outputs/', 'Neighbourhood Map.png')
    image_path_2 = os.path.join('./Outputs/', 'Risk Response Map.png')
    image_paths = [image_path_1, image_path_2]



    # Add explanatory texts for each map.
    texts = [
        "The Neighbourhood Map provides a visual representation of an imaginary neighborhood populated by various building archetypes. Please note that in the current simulation, we can simulate only 9 different building archetypes. The map randomly assigns these archetypes to existing building footprints, offering a graphical depiction of the imaginary neighborhood's diversity.",
        "The Risk Response Map visually portrays earthquake-affected archetypes within the specified neighborhood. Fatality risk assessment adheres to Turkish and international design codes, specifying Inter-Story Drift standards: 0.016 times the story height for Serviceability Limit State (SLS) and 0.025 times the story height for Ultimate Limit State (ULS). Non-compliance indicates a significant risk of structural damage or collapse, respectively."
    ]



    # Display the maps side by side with text annotations using the previously defined function.
    display_images_and_text()



    # Add a label for opening the 'Figures' folder and a button for this purpose, using the previously defined function.
    open_folder_label = ttk.Label(frame, text="Check out intermediate results and other simulation-generated outputs by clicking the button below:", font=("Arial", 10, "bold"))
    open_folder_label.grid(row=2, column=0, columnspan=2, padx=10, pady=20) 
    open_folder_button = ttk.Button(frame, text="Open Outputs Folder", command=open_folder)
    open_folder_button.grid(row=3, column=0, columnspan=2, padx=10)



    # Set a function to handle window closing when the close button is clicked, using the previously defined function.
    root.protocol("WM_DELETE_WINDOW", on_closing)



    # Scheduling ensures that the GUI remains responsive while the images are processed and displayed.
    root.after(0, display_images_and_text)
    


    root.mainloop()