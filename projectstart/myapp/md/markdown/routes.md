# routes.py

## routes list

### 1. home() - route("/")
```
"""
Return H1 header that says welcome! (should be in html)
"""
```

### 2. work() - route("/work")
```
"""
Return html template that passes in MDForm and the current user, 
allows links to user settings and import Markdown for rendering. 
"""
```

## To Do Functions

### 3. todolist() - route("/todolist")
```
"""
            Displays the option to input text for a todo list, and displays the list of todos from the database. 

            Parameters: 
                    No Parameters but contains a routing tag with “/todolist” and the methods of ‘GET’ and ‘POST’
            Returns:
                    render_template(): Renders the html template, which displays the ToDos in order.
"""

```

### 4. add_todo() - route("/todolist/add")
```
"""
            Adds the new ToDo to the ToDo model and adds it to the database and commits. 

            Parameters:
                    No Parameters but contains a routing tag with “/todolist/add” and the method of ‘POST’
            Returns:
                    After being added it redirects to the todolist method, which then displays the new to do along with all the previous ones. 
"""
```

### 5. reload_todo(todos_id) - route("/todolist/change/<int:todos_id>")
```
"""
            Reloads the status of completion for the selected To Do

            Parameter:
                    The selected todos id so that it knows which todo to reload. This method also contains a routing tag with "/todolist/change/<int:todos_id>".
            Returns:
                    After being reloaded it redirects to the todolist method, which then displays the updated to do along with all the previous ones. 
"""
```	

### 6. delete_todo(todos_id) - route("/todolist/delete/<int:todos_id>")
```
"""
            Deletes the selected  To Do from the database and displays a delete message

            Parameter: 
                    The selected todos id so that it knows which todo to delete. This method also contains a routing tag with "/todolist/delete/<int:todos_id>".
            Returns:
                    After being deleted it redirects to the todolist method, which then displays the list of todos without the deleted one
"""
```

## Notes Functions


### 7. noteslist() - route("/noteslist")
```
'''
            Generates a notes list that is uniques to each user in the data base
            Parameters:
                    No paramters but contains a routing tag with "/noteslist and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and noteslist.
'''
```

### 8. notes_preview(id) - route("/noteslist/preview/<int:id>")
```
'''
            Function allows the user to preview notes added to the notes list
            Parameters:
                    Contains paramaters 'id' which is passed in by the routing tag "/noteslist/preview/<int:id>"
            Returns:
                    render_template(): Renders the html template given parameters MDContent and user.
'''

```

### 9. add_note() - route("/noteslist/add")
```
'''
            Function allows user to add notes to the list and assign that user as an owner of the note
            Parameters:
                    No paramters but contains a routing tag with "/noteslist/add" and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and mdform.
'''
```

### 10. import_note() - route("/noteslist/add/import")
```
'''
            Allows the user to upload a file from the computer and adds all the data to the note 
            Parameters:
                    No paramters but contains a routing tag with "/noteslist/add/import" and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and mdform.
'''
```

### 11. update_note(id) - route("/noteslist/update/<int:id>")
```
'''
            Function allows the user to edit notes previously created
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/update/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_update.
'''
```

### 12. delete_notes(id) - route('/noteslist/delete/<int:id>')
```
'''
            Function allows the user to delete a note previously created
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/delete/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    redirect (): redirects to notelist()
'''
```

### 13. share_note(id) - route("/noteslist/share/<int:id>")
```
'''
            Allows users to share notes with each other and edit them 
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/share/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_share.
'''
```

### 14. unshare_note(id) - route("/noteslist/unshare/<int:id>")
```
'''
            Allows the user to unshare a note which was previously shared with other users
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/noteslist/unshare/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and note_to_unshare.
'''
```	

### 15. validate_username(username)
```
'''
            Function checks if username entered by the user is correct or not
            Parameters:
                    (str) username 
            Returns:
                    True or False
'''
```

## Flash Cards Functions

### 16. flashcardslist() - route("/flashcardslist")
```
'''
            Generates a flashcard list that is uniques to each user in the data base
            Parameters:
                    No paramters but contains a routing tag with "/flashcardslist" and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters form, user, and flashcardslist.
'''
```

### 17. flashcards_preview(id) - route("/flashcardslist/preview/<int:id>")
```
'''
     The function lets user preview a flashcasd previously created in markdown 
     Parameters:
                Contains parameter 'id' passed in through a routing tag
                "/flashcardslist/preview/<int:id>" with "methods of 'GET' and 'POST'
            
     Returns:
            render_template(): Renders the html template given parameters MDContent and user.
'''
```

### 18. add_flashcard() - route("/flashcardslist/add")
```
 '''
     The function lets user add a flashcard to their list  
     Parameters:
            No paramters but contains a routing tag "/flashcardslist/add" with "methods of 'GET' and 'POST'
     Returns:
            render_template(): Renders the html template given parameters form, and user.
'''
```

### 19. update_flashcard(id) - route("/flashcardslist/update/<int:id>")
```
'''
          Function allows the user to update the flash cards previously created
          Parameters:
                   Contains parameter 'id' passed in through a routing tag
                    "/flashcardslist/update/<int:id>" with "methods of 'GET' and 'POST'
          Returns:
                  render_template(): Renders the html template given parameters form, user, and flashcard_to_update.
'''
```

### 20. delete_flashcards(id) - route('/flashcardslist/delete/<int:id>')
```
'''
            The function allows the user to delete flashcards in the list
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/flashcardslist/delete/<int:id>" with "methods of 'GET' and 'POST'
            Returns:
                    redirect(): redirects to flashcardslist()
'''
```

### 21. share_flashcards(id) - route('/flashcardslist/share/<int:id>')
```
'''
            The function allows the user to share flashcards with desired username
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/flashcardslist/share/<int:id>" with "methods of 'GET' and 'POST'.
            Returns:
                    returns render_template() passing html file (flashcards/share_flashcard.html) with arguments form and user.
'''
```

### 22. unshare_flashcards(id) - route('/flashcardslist/unshare/<int:id>')
```
'''
            The function allows the user to unshare flashcards with desired username
            Parameters:
                    Contains parameter 'id' passed in through a routing tag
                    "/flashcardslist/unshare/<int:id>" with "methods of 'GET' and 'POST'.
            Returns:
                    returns render_template() passing html file (flashcards/unshare_flashcard.html) with arguments form and user.
'''
```
## Timer Functions

### 23. countdown() - route('/ptimer')
```
'''
            Timer function routes the user to an HTML template (Timer/ptimer.html)
            Parameters:
                    No paramters but contains a routing tag with '/ptimer' and methods of 'GET' and 'POST'
            Returns:
                    render_template(): Renders the html template given parameters user (current_user).
'''
```
