import sys

#########################################################################################################################

from Functions_Earthquake import load_data, plot_data, response_spectrum, check_response_spectrum, plot_response_spectrum
from Functions_Structure import shape_vibration, plot_shape_vibration, generalized_SDOF, peak_displacements, peak_displacements_plot
from Functions_Map import SLS_ULS, neighbourhood_map, risk_map
from Functions_Input import input_gui
from Functions_Output import output_gui

#########################################################################################################################

# Initialize global variables.
random_earthquake = None 
natural_frequencies = None
participation_factors = None
place_name = None
dist = 1000  # Distance from place_name in meters (map size) - the most optimal for the vizualization

# Callback function to set the global variables.
def callback(var_earthquake, var_frequencies, var_factors, var_address):
    global random_earthquake, natural_frequencies, participation_factors, place_name
    random_earthquake = var_earthquake
    natural_frequencies = var_frequencies
    participation_factors = var_factors
    place_name = var_address

#########################################################################################################################

def main():
    total_tasks = 13 # Insert the total number of tasks (functions imported)
    update_progress_bar(0, total_tasks) # Initialize the progress bar and update the progress bar as each task is completed

    time, ag, timeStep, ag_file_path = load_data(random_earthquake) # Call for the function

    completed_tasks = 1 
    update_progress_bar(completed_tasks, total_tasks)

    plot_data(time, ag) # Call for the function

    completed_tasks = 2  
    update_progress_bar(completed_tasks, total_tasks)

    Tarray, peakDisp = response_spectrum(ag, time, timeStep) # Call for the function
    
    completed_tasks = 3  
    update_progress_bar(completed_tasks, total_tasks)

    x_common, y_calculated_interp_dis, y_seismosignal_interp_dis = check_response_spectrum(ag_file_path, Tarray, peakDisp) # Call for the function

    completed_tasks = 4  
    update_progress_bar(completed_tasks, total_tasks)

    plot_response_spectrum(x_common, y_calculated_interp_dis, y_seismosignal_interp_dis) # Call for the function
    
    completed_tasks = 5 
    update_progress_bar(completed_tasks, total_tasks)

    psi_normalized_values, height_values = shape_vibration() # Call for the function
    
    completed_tasks = 6 
    update_progress_bar(completed_tasks, total_tasks)

    plot_shape_vibration(height_values, psi_normalized_values) # Call for the function

    completed_tasks = 7  
    update_progress_bar(completed_tasks, total_tasks)

    z_0_values = generalized_SDOF(natural_frequencies, participation_factors, x_common, y_calculated_interp_dis) # Call for the function

    completed_tasks = 8  
    update_progress_bar(completed_tasks, total_tasks)

    u_j0_values = peak_displacements(psi_normalized_values, z_0_values) # Call for the function

    completed_tasks = 9  
    update_progress_bar(completed_tasks, total_tasks)

    peak_displacements_plot(u_j0_values, height_values) # Call for the function

    completed_tasks = 10 
    update_progress_bar(completed_tasks, total_tasks)

    SLS_indexes, ULS_indexes = SLS_ULS(u_j0_values, height_values) # Call for the function

    completed_tasks = 11  
    update_progress_bar(completed_tasks, total_tasks)

    roads, groups = neighbourhood_map(place_name, dist) # Call for the function

    completed_tasks = 12 
    update_progress_bar(completed_tasks, total_tasks)

    risk_map(SLS_indexes, ULS_indexes, roads, groups) # Call for the function

    completed_tasks = 13
    update_progress_bar(completed_tasks, total_tasks)


def update_progress_bar(completed, total):
    progress = completed / total
    bar_length = 50
    progress_bar = "#" * int(bar_length * progress)
    spaces = " " * (bar_length - len(progress_bar))

    sys.stdout.write(f"\r[{progress_bar}{spaces}] {int(progress * 100)}%")
    sys.stdout.flush()

#########################################################################################################################

if __name__ == "__main__":
    input_gui(callback)
    print("Processing... Please wait.")
    main()
    print(" ... Wait for the results to appear.")
    output_gui()
    print("Simulation execution is done.")