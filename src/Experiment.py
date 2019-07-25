from testing.TestingSession import TestingSession
from training.TrainingSession import TrainingSession


class Experiment:
    def __init__(self, training_session, testing_session):
        self.training = training_session
        self.testing = testing_session

    def reset(self):
        self.training = TrainingSession()
        self.testing = TestingSession()
        self.training.load_cases()
        self.testing.load_cases()
        print(self.training.cases)

    def save(self, session):
        print("Saving experiment to the database")
        print(session)
        print(self.training.results)
        print(self.testing.results)



experiment = Experiment(TrainingSession(), TestingSession())
