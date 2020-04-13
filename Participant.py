from typing import List
from Appointment import Appointment

class Participant:
    #A participant has the following properties:
    #Name
    #Appointments
    def __init__(self, name, appointments: List[Appointment]):
        self.name = name
        self.appointments = appointments
        self.mergedAppointments = []
        self.negatedAppointments = []

    def addAppointment(self, appointment):
        self.appointments.append(appointment)


    #Accepts list of appointments and merges them if possible.
    #Returns array of merged appointments
    def mergeAppointments(self):
        self.appointments.sort(key=lambda x: x.start)

        merged = []

        for appointment in self.appointments:
            # if the list of merged appointments is empty or if the current
            # appointment does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < appointment.start:
                 merged.append(appointment)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1].end = max(merged[-1].end, appointment.end)
                merged[-1].description = "Merged '" + merged[-1].description + "' and '" + appointment.description + "'"
        self.mergedAppointments = merged


    #Expects list of intervals sorted by start
    def negateAppointments(self, start: int, end: int):
        ans = []
        
        for inx, a in enumerate(self.mergedAppointments):
            if (inx==0):
                ans.append(Appointment(start,a.start,"Description"))
            else:
                ans.append(Appointment(self.mergedAppointments[inx-1].end, a.start, "Descripion"))
        ans.append(Appointment(self.mergedAppointments[-1].end,end, "Description"))
        self.negatedAppointments = ans
