import Appointment
import Participant
import TimeSlotFinder

#Create dummy praticipants 
p1 = Participant("Juergen", [])
p2 = Participant("Harald", [])
p3 = Participant("Markus", [])

#Create dummy appointments
for i in range(0,100):   
    start = random.randint(10,50)
    end = random.randint(70,100)
    a = Appointment(start, end, "A test appointment")
    p1.addAppointment(a)
for i in range(0,100):   
    start = random.randint(10,50)
    end = random.randint(70,100)
    a = Appointment(start, end, "A test appointment")
    p2.addAppointment(a)
for i in range(0,100):   
    start = random.randint(10,50)
    end = random.randint(70,100)
    a = Appointment(start, end, "A test appointment")
    p3.addAppointment(a)

print("Done creating appointments")

#Merge and negate appointments of all participants

participants = []

participants.append(p1)
participants.append(p2)
participants.append(p3)

appointments = []

for participant in participants:
    participant.mergeAppointments()
    participant.negateAppointments(0,150)
   # print(*participant.negatedAppointments)

for participant in participants:
    appointments.append(participant.negatedAppointments)


print(*getAllIntersections(appointments))
