URL to team repository: https://github.com/razzacktiger/CMPE-131-2_Term_Project-.git
##Team Members: 
Haroon Razzack
Joshua Yee
Lovepreet Uppal
Date: 9/10/2021
Product Name: Study Time 
Problem Statement: People can’t focus studying and it would be useful to have a software to help them stay on task.
Non-functional Requirements: Language options, response time under 5 seconds. 
Use Case Name: Login Authentication
## Summary
This gives the user the ability to login.
## Actors
User
System
## Preconditions
The client needs to be in connection with the website server or application
Needs sufficient hardware
Server needs to display the login page. 
## Triggers
	Click on the login button.
## Primary Sequence
User runs the software
System prompts the user to login
User enters their username and password, then clicks the login button or enter key. 
System verifies the username and password.
System shows the home page of the application.
 
## Primary Postconditions
The system displays the home screen to the user.
 
 
## Alternate Sequences
If user enters incorrect username or password
System display error message 
System prompts the user to enter a valid user or password
System prompts the user the ability to reset password.
### Alternate Trigger
N/A
### Alternate Postconditions
The user is not allowed to enter the home page. 
 
<<<<<<< HEAD

Use Case Name: Sign Up Process
## Summary
This gives the user the option to sign up.
## Actors
1. User
2. System
## Preconditions
1. The client needs to be connected with the website server or application
2. The user needs sufficient hardware
3. Server needs to display the sign up menu.
## Triggers
The user clicking on the sign up button. 
## Primary Sequence
1. User runs the software.
2. System prompts the user to signup
3. User clicks on the signup button.
4. System displays a signup menu 
5. User inputs their email, username, password.
6. System creates the user's account and stores the information in a database. 
## Primary Postconditions
* The user is signed up with the software
* The system displays the home screen with the user logged in.
## Alternate Sequences
1. If the user enters an already existing username
a. The system displays an error message saying the username is already taken
b. The system prompts the user to choose a different username 
2. If the user enters an already existing email
a. The system displays an error message saying the email is already taken
b. The system prompts the user to choose a different email
### Alternate Trigger
N/A
### Alternate Postconditions
The user cannot use software with out an account.

Use Case Name: Delete Account Option
## Summary 
This will give the user an option to delete their account permanently
## Actors
1. User
2. System
## Preconditions
1. The client needs to be connected with the website server or application
2. The user needs sufficient hardware
3. Server needs to display the sign up menu.
4. The user must already have an account for it to be deleted. 
## Triggers
Clicks on delete account button 
## Primary Sequence
1. User clicks on delete account button 
2. System prompts the user if they really want to delete their account. 
3. User confirms that they want to delete.
4. System deletes their account from the database and logs them out. 
## Primary Postconditions
1. The systems logs the user out of the account displaying the login menu
## Alternate Sequences
1. If the user declines the confirmation to deleting the account
a. System exits the user out of the delete account confirmation prompt.
b. System brings the user back to the home menu.
## Alternate Trigger
N/A
## Alternate Postconditions
1. The user is brought back to the home page.

Use Case Name: Create  Flash Cards
## Summary 
This takes the users inputted mark down file and creates flash cards
## Actors
1. User
2. System
## Preconditions
* Needs sufficient hardware
* User needs to have correct formatting for software to create flash cards
## Triggers
* User needs to click on the generate flash cards button 
## Primary Sequence
1. User clicks on generate flash cards button 
2. System opens a prompt telling the user to upload a markdown file
3. User uploads a markdown file in correct format
4. System creates flash cards with the information on the user's uploaded file
## Primary Postconditions
1. The system displays a screen displaying flash cards. 
## Alternate Sequences
1. The user does not input a correctly formatted file
a. The system prompts the user that the file they uploaded is invalid
### Alternate Trigger
N/A
### Alternate Postconditions
1. The user is returned to the main menu

User Case Name: Share Flash Cards
## Summary 
This lets the user share their flash cards to other accounts
## Actors
1. User
2. System
## Preconditions
* The client needs to be in conneciton with the website server or application
* Needs sufficient hardware 
* User needs to have flash cards
## Triggers
* User clicks on the share button while on their flash cards
## Primary Sequences
1. User opens their file with their flash cards
2. System displays their flash cards and a share button
3. User clicks on the share button 
4. System displays a screen prompting the user to enter an email to share with
5. The user enters in the email they want to share their flash cards to
6. The user clicks send button
7. The system shares the flash card file with the inputted email account
## Primary Postconditions
1. The system displays a message saying it was shared successfully.
## Alternate Sequences
1. If the user enters an invalid email
a) System display an error message
b) System prompts the user to enter a valid email 
## Alternate Trigger
N/A
### Alternate Postconditions
1) The user does not share their flash cards with another account 

Use Case Name: Create and Print FLash Cards
## Summary 
This lets the user create a pdf of their flash cards and print it
## Actors
1. User
2. System
## Preconditions 
* Needs sufficient hardware
* User has a created flash cards already using create flash cards use case
## Triggers
* Clicks on the create PDF button
## Primary Sequence
1. User clicks on create PDF button while on their flash cards file
2. System displays preview of PDF formatted flash cards.
3. User clicks on print button
4. System prints out the flash cards
## Primary Postconditions
1. The system creates a PDF
2. The system prints out flash cards
## Alternate Sequences
1. The user doesn't click on the print button
a. The user maintains in the PDF version of the flash cards
2. If the user does not have a connected or compatible printer
a. The system displays an error message 
b. The system prompts the user to connect a working printer
### Alternate Trigger
N/A
### Alternate Postconditions
1. The user doesn't get it printed and is returned to PDF version of flash cards.
