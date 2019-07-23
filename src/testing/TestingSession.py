import csv
import json
import math
import random


# A testing session consists of several testing cases. These cases are randomly drawn from the case directory or can
# specified as a list of case files.
class TestingSession:
    def __init__(self, participant=None):
        self.participant = participant
        self.tolerance = 500  # Default error tolerance
        self.n_cases = 2  # Default number of test cases
        self.case_dir = "/home/senne/Projects/follow_the_leader/data/cases/"  # Directory for testing cases
        self.results = []  # Results of the testing session
        self.cases = []  # Initialize with no cases loaded
        self.current_index = 0  # Index of the set of cases

    # Load TestingCases
    def load_cases(self, *args):
        # Load actions.json
        actions = json.load(open(self.case_dir + "actions.json"))
        if args:
            # If a list of cases is given, load them into the session
            for arg in args:
                self.cases.append(TestingCase(self, arg, self.case_dir + actions[arg][0], self.tolerance))
        else:
            # Chose actions from case_dir, according to actions dictionary
            action_names = actions.keys()
            files = []
            # For every name of action in the dictionary
            for name in action_names:
                files.append(TestingCase(self, name, self.case_dir + actions[name][0], self.tolerance))
                # Stop after n_cases
                if len(self.cases) == self.n_cases:
                    break
            # Random shuffle files
            random.shuffle(files)
            self.cases = files
        # Activate cases
        for case in self.cases:
            case.load_case()

    # Return current case
    def current_case(self):
        return self.cases[self.current_index]

    # Got to the next case
    def next_case(self):
        # If the current index is the last element of the set of cases
        if self.current_index < self.n_cases - 1:
            self.current_index = self.current_index + 1
            return True
        else:
            return False

    # Return JSON with action of the case and the associated path.
    def get_case(self):
        cse = self.current_case()
        obj = {
            "action": cse.action,
            "path": cse.path
        }
        return obj


# A TestingCase consists of several trials the user can do
class TestingCase:
    def __init__(self, session, action, file_path, tolerance):
        self.file_path = file_path  # Which case
        self.trials = []  # The trials that have been submitted by the user
        self.errors = 0  # How many times wrong, according to tolerance
        self.error = None  # What was the error in the last submission
        self.tolerance = tolerance  # Fault tolerance of the path
        self.path = []
        self.session = session
        self.action = action

    # Load the case file and return a list of coordinates for the path.
    def load_case(self):
        file = open(self.file_path, 'rU')
        # Map the CSV file onto JSON
        reader = csv.DictReader(file)
        for row in reader:
            row['x'] = int(row['x'])
            row['y'] = int(row['y'])
            self.path.append(row)
            # self.path.append(json.dumps(row))  # To stringify the JSON object

    # Generate a trial, calculate error with user input and verify the result. Afterwards, collect it under trials.
    def try_trial(self, user_input):
        trial = TestingTrial(self.path, self.tolerance)
        trial.calc_error(user_input)
        res = trial.verify()
        self.trials.append(trial)
        if res == "tolerated":
            if not self.session.next_case():
                return "session done"
            else:
                return res
        else:
            return res


# Each submitted input is validated in a TestingTrial.
class TestingTrial:
    def __init__(self, case_data, tolerance):
        self.case_data = case_data
        self.tolerance = tolerance
        self.error = None

    # Check user input with the path of the case. The input is an JSON array of X Y key fields describing the
    # coordinates.
    def calc_error(self, user_input):
        distances = []
        # Check distance error for every point in case path
        for casePoint in self.case_data:
            case_x = casePoint['x']
            case_y = casePoint['y']
            lowest_distance = float("inf")
            for inputPoint in user_input:
                input_x = inputPoint['x']
                input_y = inputPoint['y']
                distance = math.sqrt((case_x - input_x) ** 2 + (case_y - input_y) ** 2)
                if lowest_distance > distance:
                    lowest_distance = distance
            distances.append(lowest_distance)
        self.error = sum(distances)

    # Verify the gathered results of the trial
    def verify(self):
        result = self.tolerance - self.error
        if result >= 0:
            return "tolerated"
        else:
            return "not tolerated"