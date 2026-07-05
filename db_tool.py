import pandas as pd
import random

def check_beverage(drink_name: str) -> str:
    """Queries the Starbucks dataset using Pandas to recommend low-sugar alternatives."""
    try:
        df = pd.read_csv('starbucks.csv')
        df.columns = df.columns.str.strip()
        
        # Search for the user's drink
        match = df[df['Beverage'].str.lower().str.contains(drink_name.lower(), na=False)]
        
        if match.empty:
            return f"Drink '{drink_name}' not found in the Starbucks database."
        
        # Get the first match's specific details
        first_match = match.iloc[0]
        original_name = f"{first_match['Beverage']} ({first_match['Beverage_prep']})"
        sugar_content = pd.to_numeric(first_match['Sugars (g)'], errors='coerce')
        calories = first_match['Calories']
        
        # Filter the dataframe for healthy alternatives (Less than 5g of sugar)
        # We also filter out basic "Short" sizes to give realistic recommendations
        healthy_df = df[
            (pd.to_numeric(df['Sugars (g)'], errors='coerce') <= 5) & 
            (~df['Beverage_prep'].str.contains('Short', case=False, na=False))
        ]
        
        if healthy_df.empty:
            return f"{original_name} has {sugar_content}g of sugar and {calories} calories. No low-sugar alternatives found."
            
        # Select a random healthy alternative
        healthy_choice = healthy_df.sample(1).iloc[0]
        rec_name = f"{healthy_choice['Beverage']} ({healthy_choice['Beverage_prep']})"
        rec_sugar = healthy_choice['Sugars (g)']
        rec_cal = healthy_choice['Calories']
        
        return (f"The {original_name} contains a massive {sugar_content}g of sugar and {calories} calories. "
                f"As a strict nutritionist, I recommend switching to the {rec_name}, "
                f"which only has {rec_sugar}g of sugar and {rec_cal} calories.")
        
    except FileNotFoundError:
        return "System Error: starbucks.csv database not found."
    except Exception as e:
        return f"System Error processing data: {str(e)}"
