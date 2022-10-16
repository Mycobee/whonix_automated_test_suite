from behave import *
from dogtail.procedural import *
import time 
import subprocess 
import re
import os.path
import pwd

#@given('"{application}" is running')
#def step_impl(context, application):


@when('I run the command "{cmd}" with the options "{params}" programmatically')
def step_impl(context, cmd, params):
    #executes the command with the parameters
    command = cmd + " " + params
    context.termApp = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
    context.termApp.wait()
    time.sleep(.5 * context.sleepmult)
    pass


@when('I run the command "{cmd}" with the options "{params}" programmatically with root permissions my password being "{rootPW}"')
def step_impl(context, cmd, params, rootPW):
    #executes the command with the parameters
    command = cmd + " " + params
    termAppRoot = subprocess.Popen(command.split(),stdout=subprocess.PIPE)
    time.sleep(.5 * context.sleepmult)
    type(rootPW)
    time.sleep(context.sleepmult * .4)
    keyCombo("<enter>")
    termAppRoot.wait()
    pass




@then('the user "{user}" exists')
def step_impl(context,user):
    try:
        pwd.getpwnam(user)
        pass
    except KeyError:
        assert False


@then('the user "{user}" no longer exists')
def step_impl(context,user):
    try:
        pwd.getpwnam(user)
        assert False
    except KeyError:
        pass

#todo use the CLI output to verfiy possible issues
@then('there is CLI output')
def step_impl(context):
    output = context.termApp.communicate
    assert output is not None 
    pass

#might be an unneeded implementation here
#could use the util with the @when keyCombo
#but there isn't a @then currently
@then('the GUI window appears and is dismissed')
def step_impl(context):
    time.sleep(.5 * context.sleepmult)
    keyCombo("<enter>")
