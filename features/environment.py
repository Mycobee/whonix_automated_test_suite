# -- FILE: features/environment.py
# -- much of this file is ripped from behave tutorials, edits to come

import subprocess
import time

BEHAVE_DEBUG_ON_ERROR = False

### BEHAVE LIFECYCLE METHODS, SEE DOCUMENTATION

# these methods are called automatically throughout execution


### SET UP ####
def before_all(context):
    userdata = context.config.userdata
    setup_debug_on_error(context.config.userdata)
    
    # set the sleep multiplier from the CLI
    context.sleepmult = userdata.getfloat("SLEEPMULT", 1.0)

    # initalize empty dicts, for later use
    context.activeapplications={}

    context.pids={}

def before_feature(context, feature):
    ### perform some switching based on what feature is about to run

    # tag-switching, torbrowser tag means it uses the tor browser
    if "torbrowser" in context.tags: #this uses the tor browser, set it up
        browserprocess = subprocess.Popen(['torbrowser'],shell=True)
        time.sleep(5.0 * context.sleepmult)
        context.activeapplications['torbrowser']=(browserprocess)

def after_feature(context, step):
    ### perform some switching based on what

    # tag-switching, torbrowser tag means it uses the tor browser
    if "torbrowser" in context.tags: #this used the tor browser, shut it down
        browserprocess = context.activeapplications['torbrowser']
        if browserprocess.poll() is None:
            browserprocess.kill()
        del context.activeapplications['torbrowser']


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import pdb
        pdb.post_mortem(step.exc_traceback)

### END LIFECYLCE METHODS

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")



