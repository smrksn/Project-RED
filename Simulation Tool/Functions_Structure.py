import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import os

# Function 1: Shape Function 
def shape_vibration():
    Karamba_folder = r'Eigenmode Vectors'
    Karamba_file_paths = sorted([os.path.join(Karamba_folder, file) for file in os.listdir(Karamba_folder) if file.endswith('.csv')]) # List all files in the folder and sort them by name
    
    psi_normalized_values = []  # Initialize an empty list (In NumPy array all the inner arrays must have the same shape)
    height_values = []  # Initialize an empty list (In NumPy array all the inner arrays must have the same shape)
    for i, Karamba in enumerate(Karamba_file_paths):
        shape_data = np.genfromtxt(Karamba, delimiter=',') # Convert to NumPy directly, instead of Pandas DataFrame
        height = shape_data[:, 1] # NumPy array
        psi = shape_data[:, 0] # NumPy array
        psi_normalized = (psi - np.min(psi)) / (np.max(psi) - np.min(psi)) # Normalize the displacement data (max displacement = 1)
        psi_normalized_values.append(psi_normalized)
        height_values.append(height)
    return psi_normalized_values, height_values

## Function 2: Data Plotting
def plot_shape_vibration(height_values, psi_normalized_values):
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))
    for i, ax in enumerate(axes.flat):
        ax.plot(psi_normalized_values[i], height_values[i], color="green")
        ax.set_xlabel('Normalized displacement [-]')
        ax.set_ylabel('Story height [m]')
        k = i // 3 + 1
        j = ['a', 'b', 'c'][i % 3]
        ax.set_title(f"Archetype {k}{j}")
    plt.suptitle('Governing Vibration Modes $ψ(x)$ (from the Structural Analysis)', fontsize=15)
    plt.tight_layout()
    plt.savefig(os.path.join('./Outputs/','Modal Shapes.jpg'), dpi=1000)

# Function 3: Generalized displacement
def generalized_SDOF(natural_frequencies, participation_factors, x_common, y_calculated_interp_dis):
    z_0_values= np.array([])
    for i, (freq, gamma_prime) in enumerate(zip(natural_frequencies, participation_factors)):
        T=1/freq # Determine the natural period  
        # Create interpolation function to find the corresponding peak displacement, D from the response spectra
        f = interp1d(x_common, y_calculated_interp_dis, kind='linear', fill_value="extrapolate")
        D = f(T)
        z_0=gamma_prime*D # The peak value of z(t)
        z_0_values = np.append(z_0_values, z_0) 
    return z_0_values

# Function 4: Peak displacement of the generalized SDF (u_j0 = z_0 * psi_j)
def peak_displacements(psi_normalized_values, z_0_values):
    u_j0_values = [] # Initialize an empty list (In NumPy array all the inner arrays must have the same shape)
    # Loop through each psi_normalized and its corresponding z_0 value
    for psi_df, z_0_value in zip(psi_normalized_values, z_0_values):
        u_j0_base = [psi_df[0] * z_0_value]  # Include the first psi value [0] in u_j0_values
        for j in range(1, len(psi_df)):
            u_j0 = psi_df[j] * z_0_value
            u_j0_base = np.append(u_j0_base, u_j0)
        u_j0_values.append(u_j0_base)
    return u_j0_values


# Function 5: Data Plotting
def peak_displacements_plot(u_j0_values, height_values):
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))
    for i, ax in enumerate(axes.flat):
        ax.plot(u_j0_values[i], height_values[i], marker='o', linestyle='-', label='Floor Level')
        ax.set_xlabel('Peak Displacement [cm]')
        ax.set_ylabel('Building height [m]')
        k = i // 3 + 1
        j = ['a', 'b', 'c'][i % 3]
        ax.set_title(f"Archetype {k}{j}")
    plt.suptitle('Peak Displacements at Varying Heights Along the Structure', fontsize=15)
    plt.tight_layout()
    plt.savefig(os.path.join('./Outputs/','Peak Displacements'), dpi=1000)