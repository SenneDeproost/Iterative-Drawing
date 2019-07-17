import csv
import json
import math

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


class TrainingTrial:
    def __init__(self, caseData, tolerance):
        self.caseData = caseData
        self.tolerance = tolerance
        self.error = None

    # Check user input with the path of the case. The input is an JSON array of X Y key fields describing the
    # coordinates.
    def check(self, user_input):
        distances = []
        # Load JSON into list
        user_input = json.loads(user_input)
        # Check distance error for every point in case path
        for casePoint in self.caseData:
            case_x = casePoint['x']
            case_y = casePoint['y']
            lowest_distance = None
            for inputPoint in user_input:
                input_x = inputPoint['x']
                input_y = inputPoint['y']
                distance = math.sqrt((case_x - input_x)**2 + (case_y - input_y)**2)
                if lowest_distance > distance:
                    lowest_distance = distance
            distances.append(lowest_distance)













