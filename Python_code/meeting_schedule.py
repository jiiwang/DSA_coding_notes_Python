from collections import defaultdict
from typing import List

"""
Schedule Meeting API

1. Specify input:
A list of Room IDs: do not assume they are intergers; they could be string
Everytime call schedule_meeting(start_time, end_time): expect return a reservation identifier (incl. room_id), reserve it or return an error if no room is available


"""

class MeetingRoom:
    def __init__(self, room_list:List[str]):
        self.room_list = room_list
        self.room_nums = len(room_list)
        self.meetings_by_room = defaultdict(list) # key: room_ID, value: a list of pairs (start_time, end_time)      
    
    def schedule_meeting(self, start_time:int, end_time:int):
        print(f"start time: {start_time}, end time: {end_time}")
        for room_ID in self.room_list:
            # check whether the value exists for a key in a hashmap
            if not self.meetings_by_room[room_ID]:
                self.meetings_by_room[room_ID].append([start_time, end_time])
                return self.generate_reserve_ID(start_time, end_time, room_ID)
            else:
                meeting_idx = self.check_room(start_time, end_time, room_ID)
                if meeting_idx != -1:
                    self.reserve_room(start_time, end_time, room_ID, meeting_idx)
                    return self.generate_reserve_ID(start_time, end_time, room_ID)
      	
        return "error_msg: cannot schedule meeting"
      
    def check_room(self, start_time:int, end_time:int, room_ID:str):
        meetings = self.meetings_by_room[room_ID]  # [(1,3), (6, 7)]
        # print(meetings)
        m = len(meetings)
        
        # corner case
        if end_time <= meetings[0][0]:
            return 0
        
        for i in range(m-1):
            if start_time >= meetings[i][1] and end_time <= meetings[i+1][0]:
               # schedule meeting here
               return i+1
		
        if start_time >= meetings[-1][1]:
            return m
        
        return -1
    
    def reserve_room(self, start_time:int, end_time:int, room_ID:str, meeting_idx:int):            
        # self.meetings_by_room[room_ID] = self.meetings_by_room[room_ID][0: meeting_idx] + [start_time, end_time] + self.meetings_by_room[room_ID][meeting_idx: ]
        self.meetings_by_room[room_ID].insert(meeting_idx, [start_time, end_time])
    
    def generate_reserve_ID(self, start_time:int, end_time:int, room_ID:str):
        return room_ID + "_" + str(start_time) + str(end_time)

# test case
room_list = ["room1", "room2", "room3"]

scheduler = MeetingRoom(room_list)

print(scheduler.schedule_meeting(0, 2))
print(scheduler.schedule_meeting(0, 1))
print(scheduler.schedule_meeting(1, 4))
print(scheduler.schedule_meeting(0, 3))
print(scheduler.schedule_meeting(0, 1))
print(scheduler.schedule_meeting(2, 4))


      
""" Comments from Qinyu Hu
1. Ask more clear that "let's talk about the inputs"
2. Keep active communication with interviewer: hey this is what I am thinking, blah blah blah, what do you think. A long silent will make the interviewer concern about your communication and collaboration skill. Consistently ask the interviewer's opinion and making sure you two are in the same page
3. I asked specifically for data structure design: follow the instructions closely and priotize the interviewer's ask first; if you two have diverged opinion, talk clearly about why and ask which one should we go for first
4. Design high-level solution first, fill-in details later; modularized soultion; the API design is important. What are the needed simplicity here, what are the unnecessary ones
5. Timing: 45min, 30min implementation + 15min debugging
6. Be familiar with Python
"""

    # class MeetingRoom(object):
    #   def  __init__(self, ):
    #     pass
      
    #   def schedule_meeting(start_time, end_time):
    #     # step 0: validation if input is valid or not
    #     # step 1: go through each meeting room, find if it's available for input or not
    #     # step 2: reserve a room from all avialable ones