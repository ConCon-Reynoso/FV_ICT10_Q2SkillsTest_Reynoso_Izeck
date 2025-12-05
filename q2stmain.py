from pyscript import document, display

socsci_club = {
    "Name of the club" : "Social Science Club",
    "Description" : "A club for students passionate about social sciences.",
    "Schedule" : "Tuesday & Thursday, 3:00-4:00 PM",
    "Venue" : "Room 409",
    "Club Moderator" : "Mr. Roberto Lim",
    "Number  of members" : 22
}

math_club = {
    "Name of the club" : "Mathematics Club",
    "Description" : "A club for students who love mathematics.",
    "Schedule" : "Monday, 2:30-3:00 PM",
    "Venue" : "Room 404",
    "Club Moderator" : "Mr. Nicole Gabuya",
    "Number of members" : 15
}

basketball_varsity = {
    "Name of the club" : "Basketball Varsity",
    "Description" : "The varsity for true hoopers.",
    "Schedule" : "Monday, 3:00-4:00 PM",
    "Venue" : "Quadrangle",
    "Club Moderator" : "Mr. Adrian Ruiz",
    "Number of members" : 16
}

cocc = {
    "Name of the club" : "Cadet Officer Candidate Corps (COCC)",
    "Description" : "For students aspiring to be officers in the armed forces.",
    "Schedule" : "Wednesday, 2:30-4:30 PM",
    "Venue" : "Quadrangle or Teatro Preciosa",
    "Club Moderator" : "SSgt. Jemima David",
    "Number of members" : 15
}

dance_club = {
    "Name of the club" : "Dance Club",
    "Description" : "A club for students who love dancing.",
    "Schedule" : "Tuesday, 3:00-5:00 PM",
    "Venue" : "Teatro Preciosa",
    "Club Moderator" : "Mr. Alfred Cases",
    "Number of members" : 27
}

marching_band = {
    "Name of the club" : "Marching band",
    "Description" : "A club for musically inclined students.",
    "Schedule" : "Tuesday & Wednesday, 3:00-4:30 PM",
    "Venue" : "Band Room",
    "Club Moderator" : "Mr. Emilio Alumno",
    "Number of members" : 35
}

def show_club_info(e):
    document.getElementById('club-info')


print(socsci_club)
print(math_club)