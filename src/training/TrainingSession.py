import csv
import json
import math
import random
from os import listdir


# A training session consists of several training cases. These cases are randomly drawn from the case directory or can
# specified as a list of case files.
class TrainingSession:
    def __init__(self, participant=None):
        self.participant = participant
        self.tolerance = 0.25            # Default error tolerance
        self.n_cases = 5                 # Default number of test cases
        self.case_dir = "/home/senne/Projects/follow_the_leader/data/cases/"    # Directory for training cases
        self.results = []                # Results of the training session
        self.cases = []                  # Initialize with no cases loaded

    # Load TrainingCases
    def load_cases(self, *args):
        if args:
            # If a list of cases is given, load them into the session
            for arg in args:
                self.cases.append(TrainingCase(self.case_dir + arg + ".csv", self.tolerance))
        else:
            # Load random cases
            files = listdir(self.case_dir)
            random.shuffle(files)
            for file in files:
                # Load only csv files
                if file.endswith(".csv"):
                    self.cases.append(TrainingCase(self.case_dir + file, self.tolerance))
                # Stop after n_cases
                if len(self.cases) == self.n_cases:
                    break
        # Activate cases
        for case in self.cases:
            case.load_case()


    # Start a TrainingCase, including a TrainingTrial.
    def start_case(self, index):
        


# A TrainingCase consists of several trials the user can do
class TrainingCase:
    def __init__(self, file_path, tolerance):
        self.file_path = file_path      # Which case
        self.n_trails = 0               # How many times submitted
        self.n_errors = 0               # How many times wrong, according to tolerance
        self.error = None               # What was the error in the last submission
        self.tolerance = tolerance      # Fault tolerance of the path
        self.path = []

    # Load the case file and return a list of coordinates for the path.
    def load_case(self):
        file = open(self.file_path, 'rU')
        # Map the CSV file onto JSON
        reader = csv.DictReader(file)
        for row in reader:
            self.path.append(json.dumps(row))


# Each submitted input is validated in a TrainingTrial.
class TrainingTrial:
    def __init__(self, case_data, tolerance):
        self.caseData = case_data
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
















