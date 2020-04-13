class Appointment:
    def __init__(self, start, end, description):     
        #start in minutes from 0
        self.start = start
        #end in minutes from 0
        self.end = end
        #description is a short description of the appointment
        self.description = description

    def getDuration(self):
        return self.end - self.start

    def __str__(self):
        return "[\"" + self.description + "\", " + str(self.start) + ", " + str(self.end) + "]\n"

