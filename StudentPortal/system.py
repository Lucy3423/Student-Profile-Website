from student import Student
from club import Club
from bulletin_notice import Bulletin_notice

class System:
    def __init__(self):
        self.students:Student = []
        self.bulletin_notices: Bulletin_notice = []
        self.social_science_clubs: Club = []
        self.science_clubs: Club = []
        self.sport_clubs: Club = []
        self.music_clubs: Club = []
        self.all_clubs = [self.science_clubs, self.social_science_clubs, self.music_clubs, self.sport_clubs] 
    
    def set_up_students(self):
        student_club_structure1 = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
        student_club_structure = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
        
        self.students.append(Student("Lily", "Green", "21/09/2008", 0, "Lily", "Green", "lower 6", ["French", "Maths", "Computing"], student_club_structure1))
        self.students.append(Student("John", "Brown", "04/05/2007", 1, "John", "Brown", "upper 5", ["DT", "Maths", "Art", "English", "German"], student_club_structure))
        return self.students
    
    def set_up_bulletin_entries(self):
        self.bulletin_notices.append(Bulletin_notice("11/08/2025", "School Uniform Update", "upper 4", "We have recently changed the school uniform to allow girls in all year groups to wear trousers instead of the skirt if they wish to."))
        self.bulletin_notices.append(Bulletin_notice("09/08/2025", "Pack Lunches", "all", "This is a reminder that if your child wishes to have pack lunches next term, you must opt out of school lunches by 20/08/2025. Failing to do so will lead to automatique payment for the next term's lunches at school."))
        self.bulletin_notices.append(Bulletin_notice("20/010/2025", "Halloween Disco", "upper 6", "There will be a Halloween disco next Friday (29/08/25) starting at 6:30pm until 8pm. Students are encouraged to dress up in fun costumes for the event."))
        self.bulletin_notices.append(Bulletin_notice("06/09/2025", "New Club: Pickleball", "all", "Next Wednesday our new Pickball club will be starting at lunch time from 12:05 -> 12:25. We're looking forward to seeing you there!"))


    def set_up_clubs(self):
        self.science_clubs.append(Club(1, "coding club", 2, "monday"))
        self.science_clubs.append(Club(2, "space design", 2, "tuesday"))
        self.science_clubs.append(Club(3, "canSAT", 3, "wednesday"))        
        self.science_clubs.append(Club(4, "physics olympiad", 2, "thursday"))
        self.science_clubs.append(Club(5, "silver crest award", 1, "friday"))

        self.social_science_clubs.append(Club(6, "history podcast", 2, "tuesday")) 
        self.social_science_clubs.append(Club(7, "m u n", 2, "friday"))   
        self.social_science_clubs.append(Club(8, "debating", 2, "wednesday"))   
        self.social_science_clubs.append(Club(9, "fem soc", 2, "thursday"))   
        self.social_science_clubs.append(Club(10, "amnesty international", 2, "monday"))   

        self.music_clubs.append(Club(11, "choir", 0, "wednesday"))
        self.music_clubs.append(Club(12, "orchestra", 3, "thursday"))
        self.music_clubs.append(Club(13, "rock band", 3, "monday"))
        self.music_clubs.append(Club(14, "wind ensemble", 3, "tuesday"))
        self.music_clubs.append(Club(15, "cantante", 3, "wednesday"))

        self.sport_clubs.append(Club(10, "netball", 0, "wednesday"))
        self.sport_clubs.append(Club(11, "basketball", 3, "friday"))
        self.sport_clubs.append(Club(12, "hockey", 1, "monday"))
        self.sport_clubs.append(Club(13, "badminton", 1, "tuesday"))
        self.sport_clubs.append(Club(14, "lacrosse ", 1, "monday"))



    def login(self, username, password):
        found = False
        student_id = 0
        for student in self.students:
            if student.username == username and student.password == password:
                found = True
                student_id = student.student_id
        return found, student_id
    
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
    
    def identify_club_time_slot(self, club: Club):
        if club.time_slot == 0:
            time_slot = "8:am -> 8:45am"
        elif club.time_slot == 1:
            time_slot = "12:05pm -> 12:25pm"
        elif club.time_slot == 2:
            time_slot = "12:25pm -> 1:05pm"
        else:
            time_slot = "3:50pm -> 5:00pm"
        
        return time_slot

    def identify_club_day_index(self, club):
        if club.day == "monday":
            day_index = 0
        elif club.day == "tuesday":
            day_index = 1
        elif club.day == "wednesday":
            day_index = 2
        elif club.day == "thursday":
            day_index = 3
        else:
            day_index = 4
        
        return day_index

    # a method to find the correct club to add
    def find_chosen_club(self, club_id, student:Student):
        chosen_club = self.all_clubs[0][0]
        for category in self.all_clubs:
            for club in category:
                if club.club_id == club_id:
                    chosen_club = club
                    club_day_index=self.identify_club_day_index(chosen_club) 
                    valid = any(chosen_club.name in row for row in student.clubs) 
                    if valid == True:
                        "<h3> You already have a club at that time! </h3>"
                    else:
                        student.clubs[club_day_index][chosen_club.time_slot] = chosen_club.name.title()
                        print(student.clubs)
                    break
        return student

    def identify_time_greeting(self, time):
        hour = int(time[:2])
        print(hour)
        greeting = "Hello"
        # morning greeting from 05:00 --> 12:00 non-inclusive
        if hour >= 5 and hour < 12:
            greeting = "Good Morning"
        # afternoon greeting from 12:00 --> 17:00 ""
        elif hour >= 12 and hour < 17:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"
        
        return greeting
        















 
    
