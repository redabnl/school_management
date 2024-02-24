# school_management

### backend

backend server for now with login register
-> mvc structure with different controller for each actor in the system (admin, student, professor)

### Admin controller

register function : add new student/ teacher in database

### student controller

login to his account and redirect to home page (Profile)
ask for a new course to take
look for a course, professor, student
post a feedback about a professor (anonymous feedback to help the administration improve their work)
mark his attendance (student_id, face recognition service[alrealdy built with ai face recognition])
submitt a homework or an exam
see his week schedule (not sure if we doing this)

### Professor controller

login to his account and redirect to home page (Profile)
add a new course -> insert to professorPerCourse table
send a request to admin for a new course to take (if he already have a class see he can take another group too having the same course in the same session)
view all course teaches (classes in which he's teaching)
Post a new couse documentation for a specific course
assign new homeworks or exams to submitt
check student's progression (only students for classes he's taking)
send email to all class student
submitt a new mark for a quizz or an exam
Update his weekly schedule (not sure if wedoing this too )

### FRontend
