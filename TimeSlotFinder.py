from typing import List
from Appointment import Appointment
from Participant import Participant

class TimeSlotFinder:

    #Find intersections of two lists of appointments
    def getIntersections(A: List[Appointment], B: List[Appointment]):
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if lo <= hi:
                ans.append(Appointment(lo, hi, "Description"))

            # Remove the interval with the smallest endpoint
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1
        return ans


    #Find all intersection in a list of participants
    def getAllIntersections(participants: List[Participant]):

        allAppointments = []

        for participant in participants:
            allAppoinments.append(participant.appointments)

        ans = List[Appointment]
        for inx, i in enumerate(allAppointments):
            if (inx==0):
                ans = i
            else:
                ans = getIntersections(ans, i)
        return ans


    #Finds earliest Timeslot beginning earliest at start
    #return null if none found
    def findTimeSlot(earliest: int, duration: int, participants: List[Participant]):

        #Get intersections of participants
        intersections = getAllIntersections(participants)

        #Iterate free slots and check for beginning time and duration
        for intersection in intersections:
            if (intersection.start <= earliest && intersection.end >= earliest+duration):
                return Appointment(earliest, earliest+duration, "Slot")
            else if(intersection.start > earliest && intersection.start+duration <= intersection.end):
                return(Appointment(start, start+duration, "Slot"))
            else:
                return(null)
