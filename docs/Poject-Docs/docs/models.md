# models.py

## Model Classes

### 1. User(UserMixin, db.Model)
```
'''
      User class holds the id, username, email, password, notes, todos, and flashcards of each user created.
      Has many to many relationships with class notes via association table.
'''
```

### 2. Note(db.Model)
```
'''
      Note class form holds the title, data, id, date, owner, and user_id for each note created by user from routes.py
      Parameter: None
      Return: None
'''
```

### 3. ToDo(db.Model)
```
'''
  	  The ToDo Class is a class which holds the id, rank, title, completion, user_id, and users for each To Do that is added from routes.py
  	  Parameter: None
      Return: None
'''
```

### 4. FlashCard(db.Model)
```
'''
      FlashCard class form holds the question, answer, id, date, and user_id for each flash card created from routes.py
      Parameter: None
      Return: None
'''
```

### 5. Notes (db.Table)
```
'''
     This is an association table for many-to-many relationships and houses users, notes and flashcard ids
'''
```