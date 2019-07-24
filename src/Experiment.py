from testing.TestingSession import TestingSession
from training.TrainingSession import TrainingSession


class Experiment:
    def __init__(self, training_session, testing_session):
        self.training = training_session
        self.testing = testing_session

    def save(self):
        print("Saving experiment to the database")


experiment = Experiment(TrainingSession(), TestingSession())
