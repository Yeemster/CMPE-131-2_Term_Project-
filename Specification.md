# Specification Document 
## Project Name: Study Time 
### Date: 9/14/2021
### URL to team repository: https://github.com/razzacktiger/CMPE-131-2_Term_Project-.git
### Team Members: 
* Haroon Razzack
* Joshua Yee
* Lovepreet Uppal

### Problem Statement: 
People can’t focus studying and it would be useful to have a software to help them stay on task.
### Non-functional Requirements: 
Language options, response time under 5 seconds. 

## Use Case Name: Login Authentication
### Summary
This gives the user the ability to login.
### Actors
1. User
1. System
### Preconditions
1. The client/user needs to be in connection with the website server or application
1. Server needs to display the login page. 
### Triggers
* Click on the login button.
### Primary Sequence
1. User runs the software
1. System prompts the user to login
1. User enters their username and password, then clicks the login button or enter key. 
1. System verifies the username and password.
1. System shows the home page of the application.
### Primary Postconditions
* The system displays the home screen to the user.
### Alternate Sequences
1. If user enters incorrect username or password
   - System display error message 
   - System prompts the user to enter a valid user or password
   - System prompts the user the ability to reset password.
### Alternate Trigger
N/A
### Alternate Postconditions
* The user is not allowed to enter the home page. 

## Use Case Name: Sign Up Process
### Summary
This gives the user the option to sign up.
### Actors
1. User
2. System
### Preconditions
1. The client needs to be connected with the website server or application.
1. Server needs to display the sign up menu.
### Triggers
* The user clicking on the sign up button. 
### Primary Sequence
1. User runs the software.
1. System prompts the user to signup
1. User clicks on the signup button.
1. System displays a signup menu 
1. User inputs their email, username, password.
1. System creates the user's account and stores the information in a database. 
### Primary Postconditions
* The user is signed up with the software
* The system displays the home screen with the user logged in.
### Alternate Sequences
1. If the user enters an already existing username
    - The system displays an error message saying the username is already taken
    - The system prompts the user to choose a different username 
1. If the user enters an already existing email
    - The system displays an error message saying the email is already taken
    - The system prompts the user to choose a different email
### Alternate Trigger
N/A
### Alternate Postconditions
* The user cannot use software with out an account.

## Use Case Name: Delete Account Option
### Summary 
This will give the user an option to delete their account permanently
### Actors
1. User
1. System
### Preconditions
* The user must already have an account for it to be deleted. 
* The client/user needs to be in connection with the website server or application
* The client/user needs to be correctly authenticated or logged in
### Triggers
* Clicks on delete account button 
### Primary Sequence
1. User clicks on delete account button 
1. System prompts the user if they really want to delete their account. 
1. User confirms that they want to delete.
1. System deletes their account from the database and logs them out. 
### Primary Postconditions
* The systems logs the user out of the account displaying the login menu
### Alternate Sequences
1. If the user declines the confirmation to deleting the account
* System exits the user out of the delete account confirmation prompt.
* System brings the user back to the home menu.
### Alternate Trigger
N/A
### Alternate Postconditions
1. The user is brought back to the home page.

## Use Case Name: Create  Flash Cards
### Summary 
This takes the users inputted mark down file and creates flash cards
### Actors
1. User
2. System
### Preconditions
* User needs to have correct formatting for software to create flash cards
* The client/user needs to be in connection with the website server or application
* The client/user needs to be correctly authenticated or logged in
### Triggers
* User needs to click on the generate flash cards button 
### Primary Sequence
1. User clicks on generate flash cards button 
1. System opens a prompt telling the user to upload a markdown file
1. User uploads a markdown file in correct format
1. System creates flash cards with the information on the user's uploaded file
### Primary Postconditions
1. The system displays a screen displaying flash cards. 
### Alternate Sequences
1. The user does not input a correctly formatted file
    - The system prompts the user that the file they uploaded is invalid
### Alternate Trigger
N/A
### Alternate Postconditions
1. The user is returned to the main menu

## Use Case Name: Share Flash Cards
### Summary 
This lets the user share their flash cards to other accounts
### Actors
1. User
1. System
### Preconditions
* The client/user needs to be in connection with the website server or application
* The client/user needs to be correctly authenticated or logged in
* User needs to have flash cards
### Triggers
* User clicks on the share button while on their flash cards
### Primary Sequences
1. User opens their file with their flash cards
1. System displays their flash cards and a share button
1. User clicks on the share button 
1. System displays a screen prompting the user to enter an email to share with
1. The user enters in the email they want to share their flash cards to
2. System prompts the user editing permissions.
3. User chooses right of access, between edit, view, and comment.
4. The user clicks send button
5. The system shares the flash card file with the inputted email account
### Primary Postconditions
* The system displays a message saying it was shared successfully.
### Alternate Sequences
1. If the user enters an invalid email
    - System display an error message
    - System prompts the user to enter a valid email 
### Alternate Trigger
N/A
### Alternate Postconditions
1) The user does not share their flash cards with another account 

## Use Case Name: Create and Print Flash Cards
### Summary 
This lets the user create a pdf of their flash cards and print it
### Actors
1. User
1. System
### Preconditions 
* User has flash cards already 
* The client/user needs to be in connection with the website server or application
* The client/user needs to be correctly authenticated or logged in
* User has a printer that is properly connected to their system
### Triggers
* Clicks on the create PDF button
### Primary Sequence
1. User clicks on create PDF button while on their flash cards file
1. System displays preview of PDF formatted flash cards.
1. User clicks on print button
1. System prints out the flash cards
### Primary Postconditions
1. The system creates a PDF
1. The system prints out flash cards
### Alternate Sequences
1. The user doesn't click on the print button
    - The user maintains in the PDF version of the flash cards
1. If the user does not have a connected or compatible printer
    - The system displays an error message 
    - The system prompts the user to connect a working printer
### Alternate Trigger
N/A
### Alternate Postconditions
1. The user doesn't get it printed and is returned to PDF version of flash cards.

## Use Case Name: Search Text in files
### Summary
This gives the user the ability to search for a particular text or phrase in any notes document. 
### Actors
1. User
1. System
### Preconditions
1. The client/user needs to be in connection with the website server or application
1. The client/user needs to be correctly authenticated or logged in
1. The server needs to display the notes and the client needs to have the notes bar selected
### Triggers
* User clicks on the search text button or short key.

### Primary Sequence
1. User clicks on the search text button under notes.
1. System prompts user with a menu allowing for file selection.
1. User selects or types the desired file and text.
1. System iterates through all of the text in the specified files.
1. System places all instances of the desired text in a database or data structure.
1. System displays each case of the desired successively based on user input.
1. User iterates through each of the desired text.
1. System then highlights each desired case.
1. System prompts the user for the opportunity to edit the desired cases
1. User selects another text to search for otherwise it presses an exit button  
1. System disables the highlight of each case and closes the search prompt.
### Primary Postconditions
* The system returns the user to it’s previous page or state.
### Alternate Sequences
1. User types in file or text that is missing from the database, directory or file, 
    - System display error message 
    - System prompts the user with a message such as “no such search result has been found”
    - System maintains the search accessibility for the user to enter another input.
1. User logs out of the system
    - System disables the highlight of each case and closes the search prompt. 
1. User exits out of the browser 
    - System logs the user out 
### Alternate Trigger
* The user inputs a specified short key which enables the search text feature
### Alternate Postconditions
* The user is not allowed to return to its previous page or state.

## Use Case Name: Hours tracked per day
### Summary
The system tracks how long each user has been actively engaging with the software via working each day and displays the data.
### Actors
1. User
1. System
### Preconditions
1. The client/user needs to be in connection with the website server or application
1. The client/user needs to be correctly authenticated or logged in to application
1. The client/user needs to activated the pomodoro time tracking feature 
### Triggers
* User activates time tracking feature.
* User requests the System to display hours worked per day via a button.
### Primary Sequence
1. User starts the pomodoro timer 
1. System adds up the minutes timed or spent working while the timer is running .
1. System stores the time data in a database linked for each date.
1. User requests the time worked for each day via a button.
1. System displays the data in a comprehensible manner for each day or time period selected. 
### Primary Postconditions
After user requests the system for time info, 
System redirects the User to a page with the tracked time data.
### Alternate Sequences
1. User does not activate the time tracking feature and requests the time information. 
    - System does not track/add up the time worked 
    - System does not display the time info 
    - System prompts the user with a message to turn the time tracking feature on and use pomodoro timer. 
1. User logs out of the system
    - System stops the pomodoro timer 
1. User exits out of the browser 
    - System logs the user out 
### Alternate Trigger
N/A
### Alternate Postconditions
N/A

## Use Case Name: Visualize hours worked per project 
### Summary
The system tracks how long each user has been actively working on each project and displays the data in a visually appealing way.
### Actors
1. User
1. System
### Precondition 
1. The client/user needs to be in connection with the website server or application
1. The client/user needs to be correctly authenticated or logged in to application
1. The client/user needs to activated the pomodoro time tracking feature and have a project selected. 
### Triggers
* User activates time tracking feature.
* User requests the System to display hours worked for each project via a button.
### Primary Sequence
1. User selects a project to be worked on
1. User starts the pomodoro timer 
1. The system checks whether the user is working on a particular project 
1. If so, System adds up the minutes spent working on that project.
1. System stores the time data in a database linked for each project or date.
1. User requests the time worked for each project via a button.
1. System displays the data in a comprehensible manner for each project selected. 
### Primary Postconditions
* After user requests the system for time info, System redirects the User to a page with the tracked time data.
### Alternate Sequences
1. At step 5, User does not activate the time tracking feature and requests the time information for each project . 
    - System does not track/add up the time worked 
    - System does not display the time info , 
    - System prompts the user with a message to turn the time tracking feature on and use pomodoro timer. 
1. User does not select any project before tracking and requests the time information for each project . 
    - System does not track/add up the time worked 
    - System does not display the time info 
    - System prompts the user with a message telling it to select a project to receive the information.  
1. Both cases 1 and 2 occur. 
    - System does not track/add up the time worked.
    - System does not display the time info 
    - System prompts the user with a message to select a project to  		    receive the information and turn the time tracking feature on/use 	    the pomodoro timer.
1. User logs out of the system
    - System stops the pomodoro timer 
1. User exits out of the browser 
    - System logs the user out 
### Alternate Trigger
N/A
### Alternate Postconditions
N/A

## Use Case Name: To-do Tracker
### Summary
The system tracks each activity’s designated time allotted and whether  the activity was completed through the pomodoro timer or marked down as completed. 
### Actors
User
System
### Preconditions
* The client/user needs to be in connection with the website server or application
* The client/user needs to be correctly authenticated or logged in to application
* The client/user needs to have the to-do tracker activated via settings
### Triggers
The To-do list option is activated in the settings or clicked by a button
### Primary Sequence
1. The system displays the To-do list on the dashboard
1. User adds an activity to the time block section.
1. The system adds that activity to the To-do list 
1. User starts the pomodoro timer 
1. User works on the activity 
1. User finishes the activity and marks it done
1. The system updates the To-do list and removes the activity 
1. The system displays the To-do list on the dashboard again.
### Primary Postconditions
The To-do list content remains on the dashboard until deactivated
### Alternate Sequences
1. The User does not complete an overdue task on the to-do list
1. The system prompts the User via a message that a certain task is overdue and needs resolving given a specific time period. 
* ### Alternate Trigger
N/A
### Alternate Postconditions
N/A

## Use Case Name: Visualize time-blocks
### Summary
System displays the time blocks to the user.
### Actors
* User
* System

### Preconditions
1. The client/user needs to be in connection with the website server or application

2. The client/user needs to be correctly authenticated or logged in to application

3. The client/user needs to have the time-blocks feature activated via settings

### Triggers
* The Time-blocks option is activated in the settings and clicked on by a button
### Primary Sequence
1. User clicks on the time-block button.
1. System updates the time-block database  
1. System displays the Time-blocks on a separate page 
1. User hovers over a time block 
1. System then shows the custom time-block settings 
1. User exits the time-block page via a button 
### Primary Postconditions
* The Time block bar is minimized or closed out after being visualized 
### Alternate Sequences
1. User clicks on time-block button but has not activated the time-block feature. 
    - System displays error message 
### Alternate Trigger
N/A
### Alternate Postconditions
N/A

## Use Case Name: Logout Account Option
### Summary 
This will give the user an option to log/sign out of their account
### Actors
1. User
1. System
### Preconditions. 
* The client/user needs to be in connection with the website server or application
* The client/user needs to be correctly authenticated or logged in already
### Triggers
* User clicks on Sign out button
### Primary Sequence
1. User clicks on Log out account button 
1. System prompts the user if they really want to sign out their account. 
1. User confirms that they want to sign out.
1. System logs out their account 
1. System updates the system with the date and time of the user sign out 
### Primary Postconditions
* The systems logs the user out of the account displaying the login menu
### Alternate Sequences
1. If the user declines the confirmation to log out the account
    - System exits the user out of the log out  account confirmation prompt.
    - System brings the user back to the home menu or previous page.
1. User exits the browser or closes the application session
    - System logs the user out 
    - System terminates all running processes including the pomodoro timer
### Alternate Trigger
N/A
### Alternate Postconditions
1. The user is brought back to the home page or previous page

## Use Case Name: Share notes
## Summary
Allows users to share their notes with other people
## Actors
System
User
## Preconditions
* The client/user needs to be in connection with the website server or application
* The client/user needs to be correctly authenticated or logged in already
* User needs to have notes
## Triggers
* Share button while on their notes

## Primary Sequence
1. The system displays the notes and share button.
2. User clicks on the share button while on their notes.
3. The system displays a screen prompting the user to enter an email.
4. The user enters the email of the person they want to share their file with.
5. The user clicks on the send button.
6. The system shares the notes with the other person.
7. The system adds notes to the person’s account.

## Primary Postconditions
* The system displays a message saying successfully shared.
## Alternate Sequences

1. The user enters an invalid email. 
   - The system displays an error message
   - The system prompts user back to notes

### Alternate Trigger
N/A
### Alternate Postconditions
The user does not share their notes

## Use Case Name: Convert markdown notes to pdf
### Summary
The system takes users markdown notes and creates a pdf document
### Actors
User
System
### Preconditions
* The client/user needs to be in connection with the website server or application
* The client/user needs to be correctly authenticated or logged in already
* User has already created markdown notes
### Triggers
Click on the export as PDF button
### Primary Sequence
1. The User clicks on the export as PDF button
1. The system displays a textbox to change the name of the file.
1. The user clicks on the save button.
1. The system saves the notes as a pdf document
### Primary Postconditions
* System displays a message saying file successfully saved.
### Alternate Sequences
1. The user doesn’t click the save button.
    - The user maintains the markdown notes.
### Alternate Trigger
Click on the cancel button
### Alternate Postconditions
* The user does not convert markdown notes to pdf.

## Use Case Name: Time-Block
## Summary
Users will be able to add time blocks to their calendars. 
## Actors
User
System
 ## Preconditions
* The client/user needs to be in connection with the website server or application. 
* The client/user needs to be correctly authenticated or logged in to the application.
## Triggers
* The user clicks on the time-block option. 
## Primary Sequence
1. The user navigates to the time-block section.
1. The system prompts the user to the time-block page.
1. The user clicks on a button to create a time block
1. System prompts the user with options such as date, time, activity name and color.
1. The system updates the time-block database.
## Primary Postconditions
* System notifies the user that they have created a time-block successfully
*  The time-block can be visualized by the ‘‘Visualize time-block’ use case. 

## Alternate Sequences
* The user creates a time-block with a time conflict.
    - The system does not add the time-block.
    - The system displays an error message to resolve the conflict.
### Alternate Trigger
N/A
### Alternate Postconditions
The system prompts user with a message to change the time or date of the event.

## Use Case Name: Pomodoro Timer
## Summary
The system sets a timer for the user to work on tasks and then sets a break time.
## Actors
* System
* User

## Preconditions
* The client/user needs to be in connection with the website server or application.
* The client/user needs to be correctly authenticated or logged in to the application.

## Triggers
* User activates the pomodoro timer.
## Primary Sequence
1. The user clicks the button to start the timer.
1. The system starts a 25 minutes timer.
1. The user starts working on their tasks.
1. The system displays a message when the 25 minutes are over.
1. The system starts a 5 minutes break timer.
1. The system prompts the user to start the timer again or end the program.

## Primary Postconditions
* The system closes the pomodoro timer when the user ends the program. 
## Alternate Sequences
1. User stops the timer before 25 minutes or 5 minute break 
1. User logs out of the system
    - System stops the pomodoro timer and any other process
1. User exits out of the browser 
    - System logs the user out
### Alternate Trigger
### Alternate Postconditions

Use Case Name: Render Markdown Notes
## Summary
The system will input/create markdown files and render them in a notes format such that text would auto-format markdown syntax for the completed preview.  
## Actors
User
System
## Preconditions
* The client/user needs to be in connection with the website server or application.
* The client/user needs to be correctly authenticated or logged in to the application.
* The client/user needs to be navigated to the notes page
## Triggers
User clicks on create markdown file button 
 ## Primary Sequence
User clicks on create note.
System creates a markdown file.
System displays the markdown file as a black page.
User types input into the file using markdown syntax.
System takes the syntax and converts it into a formatted visualization.
## Primary Postconditions
* System displays the text back onto the screen 
## Alternate Sequences
User inputs the markdown file. 
### Alternate Trigger
User clicks on input markdown file button 
### Alternate Postconditions
System displays the text back onto the screen.

