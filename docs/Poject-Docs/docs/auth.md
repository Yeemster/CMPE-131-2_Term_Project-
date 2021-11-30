# auth.py 

## def login():
```
    '''
    Generates the template for the login page, if user is validated, it redirects to the work page
            Parameters:
                    No paramters but contains a routing tag with "/login and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form and user.
    '''
```
## def signup():
```
    '''
    Generates the template for the sign up page, if user submits valid data, it logs the user in and redirects to the work page
            Parameters:
                    No paramters but contains a routing tag with "/sign-up and methods of 'GET' and 'POST' passed through.
            Returns:
                    render_template(): Renders the html template given arguments form, user (current user).
    '''
```
## def logout():
```
    '''
    Generates functionality for the logout template page, if user is signed in, it logs 
    the user out and redirects the user to the home page
            Parameters:
                    No paramters but contains a routing tag with "/logout" parameter
            Returns:
                    render_template(): Redirects the user to the home page
    ''' 
```
## def update(id):
```
    '''
    Generates functionality for the update user template page, if user is signed in, it prompts the user with updating form. 
    the fills out the neccessary changes to their account and the system redirects the user to the login page
            Parameters:
                    id (int): system passes in the given user's ID number associated in the User models table. 
                    Contains a routing tag with '/update/<int:id>' parameter. Also Contains a @login_required tag to check authentication.
            Returns:
                    render_template(): Renders the html template given arguments form, user (current user) and user_to_update.
    '''
```
## def delete(id):
```
    '''
    Generates functionality for the delete user template page, if user is signed in, it deletes the account. Thus user is now logged out.
            Parameters:
                    id (int): system passes in the given user's ID number associated in the User models table. 
                    Contains a routing tag with '/delete/<int:id>' parameter. Also Contains a @login_required tag to check authentication.
            Returns:
                    render_template(): Renders the html template given arguments form, user (current user) and user_to_update.
    '''
```
## def account():
```
    """
    Returns render_template() for html 
    account page consisting of user settings links
    """
```