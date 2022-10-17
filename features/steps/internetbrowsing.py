from behave import given, when, then
from os import remove
import subprocess
from dogtail.procedural import *


@given('the tor browser is running')
def step_impl(context):
    # SETUP
    if context.activeapplications['torbrowser'] is None:
        raise AssertionError("failed to detect the browser running, which is required for the test")  
    focus.application("torbrowser")

@when('we send the terminate signal to the browser')
def step_impl(context):
    # SETUP
    torbrowser=context.activeapplications['torbrowser']
    torbrowser.terminate()
        
# todo, have tor browser close properly
@then('the tor browser closes successfully')
def step_impl(context):
    torbrowser=context.activeapplications['torbrowser']
    pid = torbrowser.wait()
    assert(pid == 0)
