"""
Evaluation class. Evaluations have comments, goals, metrics, closing date, etc. 
"""
from datetime import datetime

class Evaluation:
    """closing_date must be in format dd-mm-yyyy"""
    def __init__(self, active: bool, goals: list, comments: list, closing_date: str):
        # closing_date require a specific format dd-mm-YYYY
        try:
            self.closing_date = datetime.strptime(closing_date, "%d-%m-%Y") 
        except ValueError:
            print("error: closing_date's format is not valid. Registered as None.")
            self.closing_date = None
        
        self.active = active 
        self.goals = goals
        self.comments = comments

