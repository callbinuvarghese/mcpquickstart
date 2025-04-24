# Bring in MCP Server SDK
from mcp.server.fastmcp import FastMCP

# Create server 
mcp = FastMCP("HealthTools")

@mcp.tool()
def calculate_bmi(weight: float, height: float) -> str:
    """Calculate BMI given weight in kg and height in meters.
    
    Args:
        weight (float): Weight in kilograms.
        height (float): Height in meters.
    
    Returns:
        str: BMI value.
    """
    if height <= 0:
        return "Height must be greater than zero."
    bmi = weight / (height ** 2)
    return f"Your BMI is {bmi:.2f}."

@mcp.tool()
def heart_rate_zones(heart_rate: int) -> str:
    """Determine heart rate zones based on the given heart rate.
    
    Args:
        heart_rate (int): Heart rate in beats per minute (BPM).
    
    Returns:
        str: Heart rate zone.
    """
    if heart_rate < 60:
        return "Below normal resting heart rate."
    elif 60 <= heart_rate <= 100:
        return "Normal resting heart rate."
    elif 101 <= heart_rate <= 140:
        return "Moderate exercise zone."
    elif 141 <= heart_rate <= 180:
        return "Hard exercise zone."
    else:
        return "Maximum effort zone."
    
@mcp.tool()
def loinc_codes(loinc_desc:str) -> str:
    """Get LOINC code based on the description of the health terminology.
    Args:
        loinc_code (str): Loinc code description.
        Example payload: "Cholesterol, Total"
        Example payload: "Glucose"
    
    Returns:
        str: LOINC code and description.
        Example Response: "LOINC Code: 2093-3, Description: Cholesterol, Total"
    """
    
    loinc_codes = {
        "2093-3": "Cholesterol, Total",
        "2085-9": "Glucose",
        "4548-4": "Hemoglobin A1c",
        "20564-1": "Body Mass Index (BMI)",
        "39156-5": "Systolic Blood Pressure",
        "39157-3": "Diastolic Blood Pressure"
    }
    for code, desc in loinc_codes.items():
        if loinc_desc.lower() in desc.lower():
            return f"LOINC Code: {code}, Description: {desc}"
    return "No matching LOINC code found."