import hashlib
import os
import json, csv

from testing.TestingSession import TestingSession
from training.TrainingSession import TrainingSession


class Experiment:
    def __init__(self, training_session, testing_session):
        self.training = training_session
        self.testing = testing_session
        self.exp_dir = "/home/senne/Projects/follow_the_leader/experiments/"

    def reset(self):
        self.training = TrainingSession()
        self.testing = TestingSession()
        self.training.load_cases()
        self.testing.load_cases()

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
        data_path = os.path.join(self.exp_dir, hash)
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
            id = action + str(timestamp) + "training"
            hash = hashlib.sha1(id.encode("UTF-8")).hexdigest()

            # Add file name to the info file.
            data['training'].append(hash + ".csv")
            # Add path to file
            path_file = open(data_path + "/" + hash + ".csv", 'w')
            f = csv.writer(path_file)

            # Write CSV Header, If you dont need that, remove this line
            f.writerow(["x", "y", "t"])
            for x in path_data:
                f.writerow([x["x"],
                            x["y"],
                            "t"])
            path_file.close()

        # Add testing cases
        for case in self.testing.cases:
            action = case.action
            path_data = case.user_input
            id = action + str(timestamp) + "testing"
            hash = hashlib.sha1(id.encode("UTF-8")).hexdigest()
            # Add file name to the info file.
            data['testing'].append(hash + ".csv")
            # Add path to file
            path_file = open(data_path + "/" + hash + ".csv", 'w')
            f = csv.writer(path_file)

            # Write CSV Header, If you dont need that, remove this line
            f.writerow(["x", "y", "t"])
            for x in path_data:
                f.writerow([x["x"],
                            x["y"],
                            "t"])
            path_file.close()

            # Associate actions with gathered paths
            actions[action] = hash + ".csv"

        # Write actions to actions.json
        json.dump(actions, actions_file)
        actions_file.close()

        # Write to info file
        json.dump(data, info_file)

    def prev_user(self):
        all_subdirs = [d for d in os.listdir(self.exp_dir) if os.path.isdir(d)]
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        return latest_subdir




experiment = Experiment(TrainingSession(), TestingSession())
