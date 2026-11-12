"""
Garden Advice Generator Module.

This script provides tailored gardening tips and care advice based on the
current season and the specific type of plant being cultivated.
"""


def get_season_advice(season):
    """
    Determine gardening advice based on the given season.

    Args:
        season (str): Season (e.g., 'summer', 'winter').

    Returns:
        str: Season-specific gardening care instructions ending with a newline.
    """
    # Check if the season is summer and return watering/shade tips
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    # Check if the season is winter and return frost protection tips
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    # Handle any other season not explicitly covered
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """
    Determine gardening advice based on the type of plant.

    Args:
        plant_type (str): The category of plant (e.g., 'flower', 'vegetable').

    Returns:
        str: Plant-specific care instructions.
    """
    # Provide fertilising advice for flowering plants
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    # Provide pest control reminders for vegetable crops
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    # Handle unrecognised plant categories
    else:
        return "No advice for this type of plant."


def generate_garden_advice(season, plant_type):
    """
    Combine seasonal and plant-specific advice into a single message.

    Args:
        season (str): The current season.
        plant_type (str): The category of plant.

    Returns:
        str: The complete, combined gardening advice string.
    """
    # Retrieve the seasonal advice first
    advice = get_season_advice(season)
    # Append the plant-specific advice to the seasonal message
    advice += get_plant_advice(plant_type)
    return advice


# Hardcoded values for the season and plant type
# TODO: Replace with input() in a future update to allow user interaction.
season = "summer"
plant_type = "flower"

# Generate the combined gardening advice using the helper functions
advice = generate_garden_advice(season, plant_type)

# Output the final generated advice to the console
print(advice)

# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
