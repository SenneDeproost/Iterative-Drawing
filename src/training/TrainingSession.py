import csv
import json
import math
import random


# A training session consists of several training cases. These cases are randomly drawn from the case directory or can
# specified as a list of case files.
class TrainingSession:
    def __init__(self):
        self.actions = []
        self.tolerance = 1000  # Default error tolerance
        self.n_cases = 2  # Default number of test cases
        self.case_dir = "/home/senne/Projects/follow_the_leader/data/cases/"  # Directory for training cases
        self.results = []  # Results of the training session
        self.cases = []  # Initialize with no cases loaded
        self.current_index = 0  # Index of the set of cases

    # Load TrainingCases
    def load_cases(self, actions_file=("/home/senne/Projects/follow_the_leader/data/cases/" + "actions.json"), *args):
        self.cases = []  # Dirty solution to out-of-range bug
        self.actions = json.load(open(actions_file))
        self.current_index = 0
        action_dir = actions_file[:-12]  # Parent folder of the action file
        # Load actions.json
        if args:
            # If a list of cases is given, load them into the session
            for arg in args:
                self.cases.append(TrainingCase(self, arg, action_dir + self.actions[arg], self.tolerance))
        else:
            # Chose actions from case_dir, according to actions dictionary
            action_names = self.actions.keys()
            files = []
            # For every name of action in the dictionary
            for name in action_names:
                files.append(TrainingCase(self, name, action_dir + self.actions[name], self.tolerance))
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


# A TrainingCase consists of several trials the user can do
class TrainingCase:
    def __init__(self, session, action, file_path, tolerance):
        self.file_path = file_path  # Which case
        self.trials = []  # The trials that have been submitted by the user
        self.errors = 0  # How many times wrong, according to tolerance
        self.error = None  # What was the error in the last submission
        self.tolerance = tolerance  # Fault tolerance of the path
        self.path = []
        self.session = session
        self.action = action
        self.user_input = []

    # Load the case file and return a list of coordinates for the path.
    def load_case(self):
        print(self.file_path)
        file = open(self.file_path, 'rU')

        # Map the CSV file onto JSON
        reader = csv.DictReader(file)
        for row in reader:
            row['x'] = int(float(row['x']))
            row['y'] = int(float(row['y']))
            # row['t'] = int(row['t'])
            self.path.append(row)
            # self.path.append(json.dumps(row))  # To stringify the JSON object

    # Generate a trial, calculate error with user input and verify the result. Afterwards, collect it under trials.
    def try_trial(self, user_input):
        trial = TrainingTrial(self.path, self.tolerance)
        trial.calc_error(user_input)
        res = trial.verify()
        self.trials.append(trial)
        self.session.results.append(res)
        if res == "tolerated":
            # Add user input to the input of previous sessions
            self.user_input = user_input
            if not self.session.next_case():
                return "session done"
            else:
                return res
        else:
            return res


# Each submitted input is validated in a TrainingTrial.
class TrainingTrial:
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
            return "not tolerated"  # Should be "not tolerated"
