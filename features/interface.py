### This interface contains all of the
### implemented Gherkin lines. 
### Please use it to determine if you
### need to implemented new portions
### 
### (May need future organziation)

############################
### internetbrowsing.py
############################

#checks if the tor browser is running
@given('the tor browser is running')
def step_impl(context):

#currently unfunctional please see internetbrowsing.py
@when('we send the terminate signal to the browser')
def step_impl(context):
        
#checks PID of the browser after it is closed
@then('the tor browser closes successfully')
def step_impl(context):

##################
###terminal.py
##################

#executes shell commands with a command and parameters variable
@when('I run the command "{cmd}" with the options "{params}" programmatically')
def step_impl(context, cmd, params):

#executes with sudo abilities
@when('I run the command "{cmd}" with the options "{params}" programmatically with root permissions my password being "{rootPW}"')
def step_impl(context, cmd, params, rootPW):

#checks for a user's existence
@then('the user "{user}" exists')
def step_impl(context,user):

#checks for the lack thereof a user
@then('the user "{user}" no longer exists')
def step_impl(context,user):

#confirms CLI output of a terminal command (no root)
@then('there is CLI output')
def step_impl(context):

#presses enter during the whonix check (possibly needs revision)
@then('the GUI window appears and is dismissed')
def step_impl(context):

###############
### util.py
###############

#checks with DPKG that 'application' is installed
@given('the application "{application}" is installed')
def step_impl(context, application):

#checks that the application 'application' is running
@given('"{application}" is running')
def step_impl(context, application):

#checks that the application 'application' is not running
@given('"{application}" is not running')
def step_impl(context, application):

#simply checks if the file at filepath exists, delete it if it does
#given is meant to put the system into a known state
@given('the file "{filepath}" does not exist')
def step_impl(context, filepath):
    
#sets the test path
@given('the test file location is at "{filepath}"')
def step_impl(context, filepath):

#checks if a file doesn't exist
@given('the test file does not exist')
def step_impl(context):

#checks if a file exists
@then('the file "{filepath}" exists')
def step_impl(context, filepath):

#Compares and oracle (correct test result) to a test result
#within a file
@then('the file "{filepath}" contains the "{oracletext}"')
def step_impl(context, filepath, oracletext):

# checks that the application 'application' is running
@then('"{application}" is running')
def step_impl(context, application):

#checks that the application 'application' is not running
@then('"{application}" is not running')
def step_impl(context, application):
    
#opens a program via terminal call
@when('I open the application "{application}" programmatically')
def step_impl(context, application):

#a functional key is pressed
@when('I press "{key}"')
def step_impl(context, key):

# emulate the user pressing the keycombo 'keycombo'
@when('I press the key combination "{keycombo}"')
def step_impl(context, keycombo):
    

# emulate the user typing the text 'text'
@when('I type "{text}"')
def step_impl(context, text):
    








