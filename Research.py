import requests

def get_heavy_metal_data(sampling_point_id):
    """
    Fetches real water quality data from the Environment Agency API.
    """
    # Determinand 6451 is commonly used for Lead (example)
    url = f"https://environment.data.gov.uk/water-quality/data/measurement.json?samplingPoint={sampling_point_id}&determinand=6451"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            items = data.get("items", [])
            if items:
                # Get the most recent measurement
                latest = items[0]
                return f"Lead Level: {latest['result']} {latest['unit']['label']}"
        return "No recent data for this location."
    except Exception as e:
        return f"Error: {e}"
