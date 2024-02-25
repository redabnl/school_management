# school_management

### BACKEND

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

### login FORM

Component LoginForm
State: - email: string - password: string - error: string - isProfessor: boolean (true if professor, false if student)

Function handleToggleChange
Update state to reflect the change in user type (professor or student)
Modify form appearance based on the toggle state

Function handleEmailChange
Update state with email from the event target value

Function handlePasswordChange
Update state with password from the event target value

Function handleSubmit
Prevent default form submission behavior
Determine endpoint based on isProfessor state
Send POST request to the appropriate Flask server endpoint with email and password
On success:
Redirect user to their dashboard
On failure:
Update state with error message

Render - Toggle switch for user type (Student / Professor) - Form container with dynamic class based on isProfessor state for styling - Email input field bound to state and change handler - Password input field bound to state and change handler - Submit button bound to submit handler - Display error message if present

EndComponent
<<<<<<< HEAD

> > > > > > > # a020bc3 (last commit changes with login successful)
> > > > > > >
> > > > > > > a020bc3 (last commit changes with login successful)
