# Project-RED
![Intro](https://github.com/smrksn/Project-RED/assets/144154829/5fe729b6-53fb-45ce-8a17-0acd60329a00)

## Go Directly to:
[Project's Overview](https://github.com/smrksn/Project-RED/blob/main/README.md#project-overview)

[Structural Analysis](https://github.com/smrksn/Project-RED/blob/main/README.md#structural-analysis)

[Simulation Tool](https://github.com/smrksn/Project-RED/blob/main/README.md#simulation-tool)


## Project's Overview:
This project's core objective is to develop a Response Map for aiding Response Management teams post-earthquakes. Currently, the delayed acquisition of reliable satellite data, taking 24 to 36 hours, poses a critical challenge. The Response Map seeks to substantially reduce this timeframe, offering an immediate estimation of affected buildings based on their structural properties. This swift response enhances post-earthquake assessment efficiency, facilitating timely decision-making for response teams. Simultaneously, the project lays the groundwork for a prospective GIS database. Paired with ground acceleration records, this database is poised to efficiently produce Risk Response Maps for seismic event-impacted regions.
### Context Note
With a specific focus on the Turkey–Syria seismic events of February 6, 2023, this initiative is part of CORE Studio's emphasis on Earthquake Resilience and Recovery. The course urges Building Technologists to comprehend this global challenge and develop practical solutions for future scenarios.
### Current Limitations
The project envisions the development of a country-specific extensive database, integrating three critical structural variables for evaluating structural integrity after induced earthquakes. However, these types of databases are currently in a conceptual stage and not widely implemented. To address this limitation, users can generate their own database through the **Structural Analysis** approach. This database accommodates nine different buildings or three main archetypes parametrically altered. Users can then leverage the structural analysis outputs in the **Simulation Tool**, which aligns with seismic engineering principles and national/international design codes.

## Structural Analysis
... Ramya's part

## Simulation Tool
The 'Simulation Tool' assesses the response of nine structural archetypes to seismic events. Running the **MASTERCODE.py** script activates this user-friendly interface, streamlining the analysis process.

### Repository Contents
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

