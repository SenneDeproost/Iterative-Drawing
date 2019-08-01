import csv
import hashlib
import json
import os

from testing.TestingSession import TestingSession
from training.TrainingSession import TrainingSession

exp_dir = "/home/senne/Projects/follow_the_leader/experiments/"

class Experiment:
    def __init__(self):
        actions = self.prev_user() + "/actions.json"
        self.training = TrainingSession()
        self.testing = TestingSession()
        #self.training.load_cases()
        #self.testing.load_cases()
        self.training.load_cases(actions_file=actions)
        self.testing.load_cases(actions_file=actions)

    def reset(self):
        actions = self.prev_user() + "/actions.json"
        # Load with data from previous session
        self.training.load_cases(actions_file=actions)
        self.testing.load_cases(actions_file=actions)
        # self.training.load_cases()
        # self.testing.load_cases()

    # Save the gathered data of the experiment in several files.
    def save(self, session):
        # User information
        first_name = session['first_name']
        last_name = session['last_name']
        age = session['age']
        email = session['email']
        timestamp = session['timestamp']

        # User ID for hash
        id = first_name + last_name + str(timestamp)
        hash = hashlib.sha1(id.encode("UTF-8")).hexdigest()
        # Create directory for user data
        data_path = os.path.join(exp_dir, hash[:10])
        os.mkdir(data_path)

        # Create experiment data file. Paths are saved in separate files.
        info_file = open(data_path + "/info.json", 'w')
        # Action file can be used to find the path corresponding to the action
        actions_file = open(data_path + "/actions.json", 'w')

        data = {
            "user": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "email": email,
                "timestamp": timestamp
            },
            "training": [],
            "testing": []
        }

        actions = {}

        # Add training cases
        for case in self.training.cases:
            action = case.action
            path_data = case.user_input
            id = action + "_training"
            # hash = hashlib.sha1(id.encode("UTF-8")).hexdigest()

            # Add file name to the info file.
            data['training'].append(id + ".csv")
            # Add path to file
            path_file = open(data_path + "/" + id + ".csv", 'w')
            f = csv.writer(path_file)

            # Write CSV Header, If you dont need that, remove this line
            f.writerow(["x", "y", "t"])
            for x in path_data:
                f.writerow([x["x"],
                            x["y"],
                            x["t"]])
            path_file.close()

        # Add testing cases
        for case in self.testing.cases:
            action = case.action
            path_data = case.user_input
            id = action + "_testing"
            # hash = hashlib.sha1(id.encode("UTF-8")).hexdigest()
            # Add file name to the info file.
            data['testing'].append(id + ".csv")
            # Add path to file
            path_file = open(data_path + "/" + id + ".csv", 'w')
            f = csv.writer(path_file)

            # Write CSV Header, If you dont need that, remove this line
            f.writerow(["x", "y", "t"])
            for x in path_data:
                f.writerow([x["x"],
                            x["y"],
                            x["t"]])
            path_file.close()

            # Associate actions with gathered paths
            actions[action] = id + ".csv"

        # Write actions to actions.json
        json.dump(actions, actions_file)
        actions_file.close()

        # Write to info file
        json.dump(data, info_file)

    def prev_user(self):
        all_subdirs = [exp_dir + d for d in os.listdir(exp_dir)]
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        return latest_subdir


experiment = Experiment()
