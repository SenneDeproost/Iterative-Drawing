from TrainingSession import *

ses = TrainingSession("Senne")
ses.load_cases()
print(ses.cases[0].path)
ses = TrainingSession("Senne")
ses.load_cases()
print("-----")
print(ses.cases[0].path)

print("-----------------------------------")

print(ses.current_case().path)
ses.next_case()
print(ses.current_case().path)
ses.next_case()
print(ses.current_case().path)
print(ses.next_case())


