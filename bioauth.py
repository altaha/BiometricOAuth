import base64
import os
import pickle

from enrollment import (
    authorize_application,
    enroll_user,
    login_application,
    revoke_application,
)


## Load program state from file
state_file = 'state.txt'

def load_state():
    try:
        s_f = open(state_file, 'r')
        state64 = s_f.read()
        statepickle = base64.b64decode(state64)
        state = pickle.loads(statepickle)
        s_f.close()
        return state
    except:
        print 'Caught exception during state load'
        return None

def dump_state(state):
    statepickle = pickle.dumps(state)
    state64 = base64.b64encode(statepickle)
    s_f = open(state_file, 'w')
    s_f.write(state64)
    s_f.close()

state = load_state()
if state is None:
    state = {
        'users': {},
        'applications': {},
    }


## Main program command loop
cmd = ['']

command_mapping = {
    'enroll': enroll_user,
    'authorize_app': authorize_application,
    'login_app': login_application,
    'revoke_app': revoke_application,
}

def print_help():
    print '#### Please use one of following commands ####'
    print '    enroll <user_name> <template_path>'
    print '    authorize_app <user_name> <application>'
    print '    revoke_app <user_name> <application>'
    print '    login_app <user_name> <application> <template_path>'
    print '##############################################'

while cmd[0] != 'quit':
    cmd = raw_input('enter a command: ')
    cmd = cmd.split()
    try:
        func = command_mapping[cmd[0]]
        state = func(state, *cmd[1:])
    except KeyError:
        print_help()

dump_state(state)
