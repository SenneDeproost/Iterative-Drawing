from django.db import models


# Model for training sessions. models.TextField is used to store JSON in text form into the database.
class TrainingSession(models.Model):
    trainingCases = models.TextField()          # List of ID's for the training cases
    numberOfCases = models.IntegerField()       # How many cases in a training session
    trialsPerCase = models.TextField()          # How many trials before case submission
    errorsPerCase = models.TextField()          # How many wrong submissions according to tolerance
    errorTolerance = models.IntegerField()      # Tolerance of error
