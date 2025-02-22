#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from ai_blog.crew import AiBlog

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'source_location': 'pune',
        'destination_location': 'jaipur',
        'travel_date': '2025-03-15',
        'travel_duration': '5 days',
        'number_of_travelers': '2',
        'travel_companions_type': 'Couple',
        'budget_per_person': '15000',
        'preferred_travel_mode': 'Flight',
        'accommodation_type': 'Hotel',
        'meal_preferences': 'Non-Veg',
        'interests': 'Nature',
        'accessibility_needs': 'Wheelchair accessible',
        'dietary_restrictions': 'Gluten-free',
        'special_requests': 'Early check-in and city view room',
        'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    }
    
    try:
        AiBlog().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


