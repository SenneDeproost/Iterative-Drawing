import time

""" 
A Session is created after the registration of a user. Both Training and Testing classes are used to draw upon a 
set of examples the user can be trained and tested on.
"""

class Participant:
    def __init__(self, form):
        self.first_name = form.cleaned_data.get('first_name')
        self.last_name = form.cleaned_data.get('last_name')
        self.age = form.cleaned_data.get('age')
        self.email = form.cleaned_data.get('email')


class Session:
    # Session is initialized with the information obtained by the participant's form.
    def __init__(self, form):
        self.timestamp = time.time()             # Timestamp to record session time
        self.participant = Participant(form)     # Participant details
        self.status = 'registered'               # Record status of the participant (registered, trained or tested)

        self.training = self.create_training()
        self.testing = self.create_testing()

    def create_training(self):
        print("Generating training session")

    def create_testing(self):
        print("Generating testing session")

    def save(self):
        print("Saving session into database")
