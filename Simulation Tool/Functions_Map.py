import osmnx as ox
import matplotlib.pyplot as plt
import geopandas as gpd
import os
import warnings
from matplotlib.legend import Legend

# Function 1: SLS and ULS Displacement Checks
def SLS_ULS(u_j0_values, height_values):
    damage_status = []
    collapse_status = []
    for archetype, height in zip(u_j0_values, height_values):
        status_SLS = [] # Boolean values cannot be inserted into NumPy
        status_ULS = [] # Boolean values cannot be inserted into NumPy
        for i in range(1, len(archetype)): # archetype and height arrays are the same
            prev_index = max(i - 1, 0)
            # First derive the heights and displacements (drifts) per floor
            story_height =(height[i] - height[prev_index])*100 # Convert meters to cm
            story_displacement = archetype[i] - archetype[prev_index]
            # SLS criteria (Turkey)
            SLS_criteria =  story_displacement > (0.016*story_height)
            # ULS criteria (International)
            ULS_criteria =  story_displacement > (0.025*story_height)
            status_SLS.append(SLS_criteria)
            status_ULS.append(ULS_criteria)
        damage_status.append(status_SLS)
        collapse_status.append(status_ULS)

    # Find the indexes of the archetypes with True (SLS) values
    SLS_indexes = [index for index, archetype in enumerate(damage_status) if any(archetype)]
    # Find the indexes of the archetypes with True (ULS) values
    ULS_indexes = [index for index, archetype in enumerate(collapse_status) if any(archetype)]
    
    return SLS_indexes, ULS_indexes

## Function 2: Neighbourhood Map
def neighbourhood_map(place_name, dist):
    # Download the roa11d network
    roads = ox.graph_from_address(place_name, dist, 'bbox', network_type='all_private', simplify=True)

    # Download building footprints for a specific place (GeoDataFrame)
    tags = {"building": True}
    gdf = ox.features_from_address(place_name, tags, dist)

    # Filter out the specific warning message (this does no affect the results)
    warnings.filterwarnings("ignore", message="Geometry is in a geographic CRS. Results from 'centroid' are likely incorrect.*")
    # Calculate the centroids of the building footprints
    gdf['centroid'] = gdf.centroid # Creating a new column in a GeoDataFrame called 'centroid' 
    # Re-enable warnings for other types
    warnings.filterwarnings("default")

    # Shuffle the rows in the GeoDataFrame randomly
    shuffled_gdf = gdf.sample(frac=1, random_state=1)

    # Split the shuffled GeoDataFrame into nine groups (archetypes)
    group_size = len(shuffled_gdf) // 9
    groups = [shuffled_gdf.iloc[i * group_size:(i + 1) * group_size] for i in range(9)]

    # Define a list of colors for the nine groups (archetypes)
    colors = ['deepskyblue', 'skyblue', 'lightskyblue', 'darkorchid', 'darkviolet', 'mediumorchid', 'khaki', 'palegoldenrod', 'darkkhaki']

    fig, ax = ox.plot_graph(roads, show=False, close=False, node_color="none")
    # Plot each group with a different color
    for i, group in enumerate(groups):
        group_gdf = gpd.GeoDataFrame(group, geometry=group['centroid'])
        k = i // 3 + 1
        j = ['a', 'b', 'c'][i % 3]
        group_gdf.plot(ax=ax, color=colors[i], label=f"Archetype {k}{j}", markersize=5)
    ax.set_title("Neigbourhood Map")
    plt.legend()
    image_path_1 = os.path.join('./Outputs/','Neighbourhood Map')
    plt.savefig(image_path_1, dpi=1000)

    return roads, groups

# Function 3: Risk Map
def risk_map(SLS_indexes, ULS_indexes, roads, groups):  
    colors = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'grey'] # Initialize all colors
    marker_sizes = [5] * len(colors)  # Initialize all marker sizes to 5
    
    for index in SLS_indexes:
        if 0 <= index < len(colors):
            colors[index] = 'lightsalmon'
            marker_sizes[index] = 15  # Set marker size to 15 for orange points

    for index in ULS_indexes:
        if 0 <= index < len(colors):
            colors[index] = 'red'
            marker_sizes[index] = 15  # Set marker size to 15 for red points

    fig, ax = ox.plot_graph(roads, show=False, close=False, node_color="none")
    for i, group in enumerate(groups):
        group_gdf = gpd.GeoDataFrame(group, geometry=group['centroid'])
        k = i // 3 + 1
        j = ['a', 'b', 'c'][i % 3]
        group_gdf.plot(ax=ax, color=colors[i], label=f"Archetype {k}{j}", markersize=marker_sizes[i])    
    ax.set_title("Risk Response Map")
    plt.legend() 
    # Create handles for the used colors
    legend_handles = [plt.Line2D([0], [0], marker='o', color=color, markerfacecolor=color, markersize=10, linestyle='None') for color in ['grey', 'lightsalmon', 'red']]
    # Create labels for the limit states
    legend_labels = ['Safe', 'SLS', 'ULS']
    # Add the custom color notations legend to the plot
    custom_legend = Legend(ax, legend_handles, legend_labels, title="Exceeded Limit States", loc='lower left')
    ax.add_artist(custom_legend)
    image_path_2 = os.path.join('./Outputs/','Risk Response Map')
    plt.savefig(image_path_2, dpi=1000)