import base64
import os
import pickle


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
    state = {}


## Main program command loop
cmd = None

def dummy_enroll(arg1, arg2, *args):
    print 'first arg is {}'.format(arg1)
    print 'second arg is {}'.format(arg2)

command_mapping = {
    'enroll': dummy_enroll,
}

def print_help():
    print '#### Please use one of following commands ####'
    print '    enroll <user_name> <template_path>'
    print '    add_app <user_name> <application>'
    print '    remove_app <user_name> <application>'
    print '    verify_app <user_name> <application> <template_path>'
    print '##############################################'

while cmd != 'quit':
    cmd = raw_input('enter a command: ')
    cmd = cmd.split()
    try:
        func = command_mapping[cmd[0]]
        func(*cmd[1:])
    except KeyError:
        print_help()

dump_state(state)
