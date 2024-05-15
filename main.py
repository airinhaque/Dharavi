import osmnx as ox
import geopandas as gpd
import folium

# Define the location (example: Dharavi, Mumbai)
place_name = "Dharavi, Mumbai, India"

# Function to fetch building footprints using osmnx
def fetch_building_footprints(place_name):
    try:
        # Fetch building footprints
        gdf_buildings = ox.geometries_from_place(place_name, tags={'building': True})
        if gdf_buildings.empty:
            print("No building footprints found.")
            return None
        return gdf_buildings
    except Exception as e:
        print(f"An error occurred while fetching building footprints: {e}")
        return None

# Fetch building footprints
print("Fetching building footprints...")
gdf_buildings = fetch_building_footprints(place_name)

if gdf_buildings is None:
    exit(1)

# Use centroid of buildings to center the map
center = gdf_buildings.geometry.centroid
center_lat = center.y.mean()
center_lon = center.x.mean()

# Create a Folium map centered around the centroid of building footprints
m = folium.Map(location=[center_lat, center_lon], zoom_start=15)

# Add building footprints to the map
folium.GeoJson(gdf_buildings.geometry).add_to(m)

# Save the Folium map
save_path = 'building_footprints_map.html'
m.save(save_path)
print(f"Map saved as {save_path}")
