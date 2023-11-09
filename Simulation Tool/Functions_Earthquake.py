import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Function 1: Data Acquisition
def load_data(random_earthquake):
    ag_folder = r"Ground Accelerations" 
    ag_file_paths = sorted([os.path.join(ag_folder, file) for file in os.listdir(ag_folder) if file.endswith('.csv')]) # List all files in the folder and sort them by name
    ag_file_path = ag_file_paths[random_earthquake]
    earthquake_data = pd.read_csv(ag_file_path) # Pandas DataFrame
    time = earthquake_data['Time [sec]'].values # NumPy array
    ag = earthquake_data['Acceleration [cm/sec2]'].values # NumPy array
    timeStep = time[2] - time[1] # NumPy array
    return time, ag, timeStep, ag_file_path

# Function 2: Data Plotting
def plot_data(time, ag):
    plt.figure()
    plt.plot(time, ag)
    plt.xlabel('Time [sec]')
    plt.ylabel('Ground Acceleration [cm/sec2]')
    plt.title('Acceleration Time Series')
    plt.savefig(os.path.join('./Outputs/','Acceleration Time Series.jpg'), dpi=1000)

''' 
We are now in the process of generating the Response Spectra, a visual representation 
that highlights the peak response values associated with their respective natural periods. 
To achieve this, we start by constructing an array of natural periods, Tarray. 
Following that, we create deformation response spectra by plotting the peak values (maximum values from Newmark integration output) 
extracted from the Response Time-Histories against this array of natural periods.
''' 

# Function 3: Response Spectrum Derivation
def response_spectrum(ag, time, timeStep):
    # Provide damping coefficient of the structure (usually 5%)
    xi = 0.05

    # Array of the natural periods (set the values from 0.1 to 10)
    # Use np.arange, instead of np.linspace, to specify the step
    Tarray=np.arange(0.1,10+0.1,0.1) # NumPy array

    # Provide Newmark integration variables (same as in Seismosignal)
    gamma=0.5 
    beta=0.25

    # Initialize arrays to store acceleration, velocity, displacement
    udd=np.zeros(np.shape(time)) # NumPy array
    ud=np.zeros(np.shape(time)) # NumPy array
    u=np.zeros(np.shape(time)) # NumPy array
    peakDisp=np.zeros(np.shape(Tarray)[0]) # NumPy array

    for j in range(0,np.shape(Tarray)[0]): # Loop for different natural periods
        T=Tarray[j]
        omega=2*np.pi/T # Angular natural frequency
        c=2*xi*(omega) # Damping
        k=np.power(omega, 2) # Stiffness
        
        for i in range(np.shape(time)[0]-1): # Newmark solver
            C1=u[i]+timeStep*ud[i]+0.5*np.power(timeStep,2)*(1-2*beta)*udd[i]
            C2=ud[i]+timeStep*(1-gamma)*udd[i]
        
            udd[i+1]=(ag[i+1]-c*C2-k*C1)/(1+gamma*c*timeStep+beta*k*np.power(timeStep,2))
            ud[i+1]=ud[i]+timeStep*((1-gamma)*udd[i]+gamma*udd[i+1])
            u[i+1]=u[i]+timeStep*ud[i]+0.5*np.power(timeStep,2)*((1-2*beta)*udd[i]+2*beta*udd[i+1])
    

        peakDisp[j]=np.max(np.abs(u))

    return Tarray, peakDisp

# Function 4: SeismoSignal Reference
def check_response_spectrum(ag_file_path, Tarray, peakDisp):
    ag_file_name = os.path.basename(ag_file_path) # Extract just the file name
    linked_file_name = "Seismosignal_" + ag_file_name # Determine the linked Seismosignal file
    linked_file_path = os.path.join(r"SeismoSignal Response Displacements", linked_file_name) # Specify the path to the linked file in the linked folder
    
    check_dis = pd.read_csv(linked_file_path) # Pandas DataFrame
    displacement = check_dis['Damp.=5.0%'].values # NumPy array
    period = check_dis['Period [sec]'].values # NumPy array

    # The calculated and Seismosignal periods must be the same, so to ensure that:
    # Create a common x-axis grid for the interpolation procedure
    min_value = int(min(np.min(Tarray), np.min(period)))
    max_value = int(max(np.max(Tarray), np.max(period)))
    x_common = np.linspace(min_value, max_value, 100)
    # Interpolate both datasets onto the common x-axis grid
    y_calculated_interp_dis = np.interp(x_common, Tarray, peakDisp)
    y_seismosignal_interp_dis = np.interp(x_common, period, displacement)

    return x_common, y_calculated_interp_dis, y_seismosignal_interp_dis

# Function 5: Data plotting
def plot_response_spectrum(x_common, y_calculated_interp_dis, y_seismosignal_interp_dis):
    plt.figure()
    plt.plot(x_common, y_calculated_interp_dis)
    plt.plot(x_common, y_seismosignal_interp_dis, linestyle='--')
    plt.xlabel('Natural period (T) [sec]')
    plt.ylabel('Peak Displacement [cm]')
    plt.legend(['Peak Displacements', 'SeismoSignal'])
    plt.title('Deformation Response Spectra')
    # Adding annotation about SeismoSignal's license restriction as a text below the plot
    max_period = 4.0
    annotation_text = f"Note: SeismoSignal License Limitation: Max Period = {max_period} sec"
    plt.figtext(0.5, 0.01, annotation_text, fontsize=8, horizontalalignment='center')
    plt.savefig(os.path.join('./Outputs/','Deformation Response Spectra.jpg'), dpi=1000)