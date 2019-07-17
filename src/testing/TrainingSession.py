import csv
import json

class TrainingSession:
    def __init__(self, participant):
        self.participant = participant
        self.tolerance = 0.25            # Default error tolerance
        self.numberOfCases = 5           # Default number of test cases
        self.caseDir = "/draw_cases"     # Directory for training cases
        self.results = []                # Results of the training session

class TrainingCase
    def __init__(self, tolerance):
        self.casePath = None            # Which case
        self.numberOfTrials = 0         # How many times submitted
        self.numberOfErrors = 0         # How many times wrong, according to tolerance
        self.error = None               # What was the error in the last submission
        self.tolerance = tolerance      # Fault tolerance of the path

    # Load the case file and return a list of coordinates for the path.
    def load_case(self):
        file = open(self.casePath, 'rU')
        # Map the CSV file onto JSON
        reader = csv.DictReader(file, fieldnames=("x", "y"))
        return json.dumps([row for row in reader])








