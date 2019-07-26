import hashlib
import os
import json

from testing.TestingSession import TestingSession
from training.TrainingSession import TrainingSession


class Experiment:
    def __init__(self, training_session, testing_session):
        self.training = training_session
        self.testing = testing_session
        self.exp_dir = "home/senne/Projects/follow_the_leader/experiments/"

    def reset(self):
        self.training = TrainingSession()
        self.testing = TestingSession()
        self.training.load_cases()
        self.testing.load_cases()

    # Save the gathered data of the experiment in several files.
    def save(self, request):
        # User information
        first_name = request.session['first_name']
        last_name = request.session['last_name']
        age = request.session['age']
        email = request.Session['email']
        timestamp = request.session['timestamp']
        # User ID for hash
        id = first_name + last_name + str(timestamp)
        hash = hashlib.sha1(id.encode("UTF-8")).hexdigest()
        # Create directory for user data
        data_path = self.exp_dir + hash
        os.mkdir(data_path)
        # Create experiment data file. Paths are saved in separate files.
        file = open(data_path + "/info.json", 'w')
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
        # Add training cases
        for case in self.training.cases:
            action = case.action
            path_data = case.user_inputs
            id = action + timestamp
            hash = hashlib.sha1(id.encode("UTF-8")).hexdigest()
            # Add file name to the info file.
            data['training'].append(hash)
            path_file = open(data_path + "/" + hash + ".csv", 'w')
            json.dumps(path_data, path_file)

        # Dump data to json object
        data = json.dumps(data)


experiment = Experiment(TrainingSession(), TestingSession())
