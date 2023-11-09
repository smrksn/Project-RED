# Project-RED
Rapid Estimation of Disaster Consequences | AR3B012 - CORE Studio | TU Delft

## Overview

## Structural Analysis
... Ramya's part

## Simulation Tool
The 'Simulation Tool,' primarily implemented within the MASTERCODE.py file, serves as the core tool for assessing the response of nine standard structural archetypes to seismic events. Upon running the MASTERCODE.py script, this tool provides a user-friendly interface to streamline the analysis process.

### Repository Contents
- **py files**: In addition to the MASTERCODE.py, this repository contains essential Python files that provide the necessary functions for the analysis.
- **txt files**: The text files are utilized to store data entered into the interface, enhancing user convenience.
- **“Outputs”**: This folder stores output and intermediate results generated during the simulation.
- **“Ground Accelerations”**: This folder holds 15 earthquake acceleration series.
- **“Eigenmode Vectors”**: This folder stores the shape of vibration vectors obtained from the structural analysis.
- **“Seismosignal Response Displacement”**: This folder contains the displacement data corresponding to each file stored in the **'Ground Acceleration'** folder. This data has been extracted using SeismoSignal.
- **“Codeflows”**: This folder contains visual summaries (HTML files) of each Python file's execution sequence for a quick overview of content and flow within.

### Using the Simulation Tool
To begin, open the MASTERCODE.py file and execute it. When the popup window appears, follow these steps to assign the necessary variables:
1.	**Select Earthquake Acceleration Series**: Select an earthquake acceleration series based on the specified magnitudes.
3.	**Insert Structural Analysis Variables**: Input the three required variables from the structural analysis for each of the nine archetypes.
3.	**Specify Map Address**: Define the address for which the maps will be displayed within a 1000-meter radius.
4.	**Save Input Values**: You are allowed to save all the inserted values to avoid reinserting them each time. These values will be stored in respective text files.
5.	**Run the Simulation**: Once you have configured the input parameters, click the "Submit Variables" button to initiate the simulation.
   
![Input Window](https://github.com/smrksn/Project-RED/assets/144154829/394dce26-0ee8-402a-a09d-ac9bc084434a)

The simulation will run until a popup window displays the output results. In this window, you can view the Neighbourhood Map and Risk Response Map. Additionally, you can access the **"Open Outputs Folder"** button to open the outputs folder in the same working directory, where intermediate results are stored.

![Output Window](https://github.com/smrksn/Project-RED/assets/144154829/ebd7bd35-ff84-4d1c-ad0b-479ea66e3dac)

### Outputs
- **Acceleration Time Series** displays ground acceleration data for the selected ground motion event.
- **Deformation Response Spectra** illustrates the buildings' response to specified seismic activity, showcasing data alignment with SeismoSignal.
- **Modal Shapes** graphs show the fundamental mode of vibration or the governing pattern of displacement that the archetypes undergo during the seismic event.
- **Peak Displacements** graphs illustrate the maximum displacement encountered by each floor within a given archetype during a selected ground motion event.
- **Neighbourhood Map** is a visual representation of various types of archetype buildings in a specified neighbourhood. In the current simulation program, they are randomly assigned to the existing building footprints.
- **Risk Response Map** is a visual representation of danger spots within a neighbourhood that has been subjected to severe damage or collapse due to the earthquake.

ADD IMAGE HERE

### Proper Variable Insertion Format and Guidelines
In the input interface, certain considerations need to be kept in mind to ensure smooth operation:

- **Earthquake Acceleration Records**: Users are restricted to utilizing the 15 pre-stored earthquake acceleration records. Each of these records is linked with the SeismoSignal analysis output for response spectra.
- **Natural Frequencies and Participation Factors**: The natural frequencies and participation factors must be manually inserted one by one. Whenever you press the "Save" button, it will overwrite the previously inserted value for the respective archetype in the corresponding text file.
- **Modal Shape Files**: The simulation program is sensitive to the format of the vibration data.
   - Ensure that the data in the CSV files conform to the following layout:
      - The first column represents the modal displacement along the x or y-axis.
      - The second column represents the respective z-coordinate, indicating the story height from the ground in meters.
      - The CSV files should be generated with comma separation.
      - If the initial x or y displacements are not normalized within the 0-1 range, the code will handle it during execution.
   - Adhering to the archetype numbering convention for file names is vital for seamless organization:
      - Ensure files are named to allow sorting from top to bottom. The initial file corresponds to the first archetype, and the sequence continues.
      - This naming convention aids in accurately overwriting the appropriate file in the folder during CSV file modifications post-structural analysis revisions, maintaining the correct file count in the folder.
   - Utilize the "Insert Files" button in the user interface to upload CSV files or drag them directly to the **“Eigenmode Vectors”** folder.

ADD IMAGES HERE

- **Address Format**: Typically, Open Street Map accepts addresses in the format of "Street, Home Number, Town, Country." In case of any errors, verify the entered address using the Online version of Open Street Map.

