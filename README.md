# Project-RED

<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/144154829/281760123-cd4f7a60-0e19-4087-83f5-68304ccbeb00.jpeg" width=70% height=70%>

## Go Directly to:
[YouTube Introduction Video](https://youtu.be/DX2MPyc3SCs)

[Project's Overview](https://github.com/smrksn/Project-RED/blob/main/README.md#project-overview)

[Structural Analysis](https://github.com/smrksn/Project-RED/blob/main/README.md#structural-analysis)

[Simulation Tool](https://github.com/smrksn/Project-RED/blob/main/README.md#simulation-tool)


## Project's Overview:
This project's core objective is to develop a Response Map for aiding Response Management teams post-earthquakes. Currently, the delayed acquisition of reliable satellite data, taking 24 to 36 hours, poses a critical challenge. The Response Map seeks to substantially reduce this timeframe, offering an immediate estimation of affected buildings based on their structural properties. This swift response enhances post-earthquake assessment efficiency, facilitating timely decision-making for response teams. Simultaneously, the project lays the groundwork for a prospective GIS database. Paired with ground acceleration records, this database is poised to efficiently produce Risk Response Maps for seismic event-impacted regions.
### Context and Copyright
This project, focusing on the Turkey–Syria seismic events of February 6, 2023, is an integral part of CORE Studio's dedication to Earthquake Resilience and Recovery. Aligned with the Master's in Building Technology coursework at TU Delft, it challenges Building Technologists to grapple with global challenges and craft practical solutions for future scenarios.

All rights, including intellectual property, are credited to Delft University of Technology (TU Delft). Proper attribution to the original creators is mandatory for any use of the material.

### Current Limitations
The project envisions the development of a country-specific extensive database, integrating three critical structural variables for evaluating structural integrity after induced earthquakes. However, these types of databases are currently in a conceptual stage and not widely implemented. To address this limitation, users can generate their own database through the **Structural Analysis** approach. This database accommodates nine different buildings or three main archetypes parametrically altered. Users can then leverage the structural analysis outputs in the **Simulation Tool**, which aligns with seismic engineering principles and national/international design codes.

## Structural Analysis
Structural analysis is vital for creating an archetypes database, extracting essential variables needed for a 'Simulation Tool'.
The 3D  structures are modelled in the following version:
- Rhino Version 7 SR34.
- Grasshopper Version Build 1.0.0007.
- Karamba3D 2.2.0.180-230616.

### Contents
- **Rhino Grasshopper File**: This file encompasses all nine archetype models.
- **Vibration Shape**: Housing CSV files, it presents values in {ψ(x), Column height} format.

### Using the File
Utilize the provided file as follows:
1. Model the structural elements and link them to the element's component.
2. Establish connections for the corresponding supports and cross-section details.
3. Specify the material properties.
4. Given the scenario of an unoccupied building, apply only gravity load.
5. Integrate all components into the Assemble model for finite element analysis at mode 0.
6. Extract the natural frequency and participation factor.
7. Retrieve the deformation axis at the origin and divide the curve by the number of floors to extract inter-story drift.

### Design Assumptions
1)	The natural frequency and participation factor values fall within the range of 0.5-1.5 units. Consequently, adjustments to the cross-sectional dimensions of the structural elements are made in accordance with rule-of-thumb guidelines.
2)	The Karamba results gave 3 participation factors - in the x, y and z-axis. The following steps were considered while selecting the participation factor for the next analysis step. If there are 3 modes of participation factor:
   - The z-axis is ruled out because the z is constant (0,3,6,9). 
   - For the x and y-axis look at displacements - consider the higher displacement values. 
   - And then, consider the participation factor in that direction.

### Creating CSV files
- Right-click on the 'Displacement Values' panel and choose "Stream Destination."
- Select the destination and specify the file name; choose the .csv format from the "Save as type" menu.
- After creating the file, right-click on the panel header once more and opt for "Stream Contents."

## Simulation Tool
The 'Simulation Tool' assesses the response of nine structural archetypes to seismic events. Running the **MASTERCODE.py** script activates this user-friendly interface, streamlining the analysis process.
Please refer to 'requirements_Simulation Tool.txt' for the software requirements needed to run the Simulation Tool.

### Contents
- **py files**: In addition to the MASTERCODE.py, this repository contains essential Python files that provide the necessary functions for the analysis.
- **txt files**: The text files are utilized to store data entered into the interface, enhancing user convenience.
- **“Outputs”**: This folder stores output and intermediate results generated during the simulation.
- **“Ground Accelerations”**: This folder holds 15 earthquake acceleration series.
- **“Eigenmode Vectors”**: This folder stores the shape of vibration vectors obtained from the structural analysis.
- **“Seismosignal Response Displacements”**: This folder contains the displacement data corresponding to each file stored in the 'Ground Acceleration' folder. This data has been extracted using SeismoSignal.
- **“Codeflows”**: This folder contains visual summaries (HTML files) of each Python file's execution sequence for a quick overview of content and flow within.

### Using the Simulation Tool
To begin, open the MASTERCODE.py file and execute it. When the popup window appears, follow these steps to assign the necessary variables:
1.	**Select Earthquake Acceleration Series**: Select an earthquake acceleration series based on the specified magnitudes.
3.	**Insert Structural Analysis Variables**: Input the three required variables from the structural analysis for each of the nine archetypes.
3.	**Specify Map Address**: Define the address for which the maps will be displayed within a 1000-meter radius.
4.	**Save Input Values**: You are allowed to save all the inserted values to avoid reinserting them each time. These values will be stored in respective text files.
5.	**Run the Simulation**: Once you have configured the input parameters, click the "Submit Variables" button to initiate the simulation.
   
<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/144154829/281756761-0a70f8d9-6bcd-4746-837c-103540360608.png" width=70% height=70%>


The simulation will run until a popup window displays the output results. In this window, you can view the Neighbourhood Map and Risk Response Map. Additionally, you can access the **"Open Outputs Folder"** button to open the outputs folder in the same working directory, where intermediate results are stored.

<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/144154829/281757940-a32ad45b-8d1e-4ff2-aa22-f4dba05ea23f.png" width=70% height=70%>

### Outputs
- **Acceleration Time Series** displays ground acceleration data for the selected ground motion event.
- **Deformation Response Spectra** illustrates the buildings' response to specified seismic activity, showcasing data alignment with SeismoSignal.
- **Modal Shapes** graphs show the fundamental mode of vibration or the governing pattern of displacement that the archetypes undergo during the seismic event.
- **Peak Displacements** graphs illustrate the maximum displacement encountered by each floor within a given archetype during a selected ground motion event.
- **Neighbourhood Map** is a visual representation of various types of archetype buildings in a specified neighbourhood. In the current simulation program, they are randomly assigned to the existing building footprints.
- **Risk Response Map** is a visual representation of danger spots within a neighbourhood that has been subjected to severe damage or collapse due to the earthquake.

<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/144154829/281755499-2aff03bc-5c54-40f7-b527-6348a5e7b927.png">


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

<img src="https://user-images.githubusercontent.com/144154829/281750282-49bd6476-f09d-4f63-b5ad-d58e3c8451dd.png" width=30% height=30%>

- **Address Format**: Typically, Open Street Map accepts addresses in the format of "Street, Home Number, Town, Country." In case of any errors, verify the entered address using the Online version of Open Street Map.

Project RED © November, 2023 by Ramya Kumaraswamy, Sofia Markson

