from Database import fetch_from_db, save_to_db
from researcher import research_water_hardness

def get_water_profile(postcode):
    """
    Orchestrates the search: 
    1. Clean the input.
    2. Try the local database.
    3. If missing, research and save.
    """
    # 1. Clean and sectorize: 'PO1 1AA' -> 'PO1'
    sector = postcode.replace(" ", "")[:-3].upper()
    
    # 2. Try Database lookup first
    data = fetch_from_db(sector)
    
    # 3. If data is missing, trigger the Research Agent
    if not data:
        print(f"Data for {sector} not in database. Deploying Research Agent...")
        data = research_water_hardness(sector)
        
        # 4. Save to Database for future speed
        if data:
            save_to_db(sector, data)
            print(f"Success: Added {sector} to database.")
        
    return data

# --- Simple test ---
if __name__ == "__main__":
    test_pc = "PO1 1AA"
    result = get_water_profile(test_pc)
    print(f"Water profile for {test_pc}: {result}")
