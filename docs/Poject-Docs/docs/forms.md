# forms
## class

## LoginForm
```
'''
    In forms.py
    Class: Defined as a Login form using WTForms
            variables: 
                    username: WTF StringField requires String input
                    password: WTF StringFeild ...
                    rememebr_me: BooleanField 
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
'''
```

## SignupForm
```
'''
    *In forms.py
    Class: Defined as a Login form using WTForms
            variables: 
                    username: WTF StringField requires String input
                    email: WTF StringField requires String input, and Email validation.
                    password: WTF StringFeild ...
                    rememebr_me: BooleanField 
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
'''
```

## UpdateUserForm
```
'''
    *In forms.py
    Class: Defined as a Login form using WTForms
            variables: 
                    username: WTF StringField requires String input
                    email: WTF StringField requires String input, and Email validation.
                    password: WTF StringFeild ...
                    rememebr_me: BooleanField 
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
'''
```
## MDForm
```
'''
    *In forms.py
    Class: Defined as a Mark Down form using WTForms
            variables: 
                    mdfile: WTF FileField requires a File input
                    submit: Submitfield for submiting a file
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
```
## NoteForm
```
'''
    *In forms.py
    Class: Defined as a NoteForm form 
            variables: 
                    note: WTF StringField requires String input and text area
                    title:  WTF StringField requires String input
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
```

## ShareForm
```
'''
    *In forms.py
    Class: Defined as a ShareForm form 
            variables: 
                    username: WTF StringField requires String input
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
```
## UnshareForm
```
'''
    *In forms.py
    Class: Defined as a UnshareForm form 
            variables: 
                    username: WTF StringField requires String input
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
```
## FlashCardForm
```
'''
    *In forms.py
    Class: Defined as a FlashCardForm form 
            variables: 
                    question: WTF StringField requires String input and text area
                    answer:  WTF StringField requires String input and text area
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
```
## TimeForm
```
'''
    *In forms.py
    Class: Defined as a TimeForm form 
            variables: 
                    countdown: TimeField for adding time in Minute : Second format
                    submit: Submitfield for submiting data 
            Parameters:
                    FlaskForm, however WTF-Flask takes care of arguments at the time of object instantiation.
    '''
```