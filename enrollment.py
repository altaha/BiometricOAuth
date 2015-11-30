from cryptography.fernet import Fernet


def enroll_user(state, username, template_file):
    if username in state['users']:
        print '{} is already enrolled'.format(username)
        print 'enrollment will be updated'

    user_state = {}
    user_state['template_file'] = template_file
    user_state['cb_template_file'] = _transform_cb(template_file)
    user_state['applications'] = {}
    state['users'][username] = user_state
    return state

def authorize_application(state, username, application):
    try:
        if application in state['users'][username]['applications']:
            print '{} is already authorized for user'.format(application)
            print 'enrollment will be updated'

        key = Fernet.generate_key()
        user_dict = {application: key}
        state['users'][username]['applications'].update(user_dict)

        state['applications'][application] = {}
        application_dict = {username: key}
        state['applications'][application].update(application_dict)

    except KeyError:
        print 'username {} is not registered'.fomat(username)
    finally:
        return state

def revoke_application(state, username, application):
    try:
        if application not in state['users'][username]['applications']:
            print '{} is not authorized for for user'.format(application)
            return state

        key = Fernet.generate_key()
        user_dict = {application: ''}
        state['users'][username]['applications'].update(user_dict)
    except KeyError:
        print 'KeyError in revoke application'
    finally:
        return state

def login_application(state, username, application, template_file):
    try:
        if application not in state['applications']:
            print '{} does not exist'.format(application)
            return state
        if username not in state['applications'][application]:
            print '{} was never auhtroized for user {}'.format(
                application, ausername)
            return state

        key1 = state['applications'][application][username]
        key2 = state['users'][username]['applications'][application]
        if key1 == key2:
            print '!!!!!! Login SUCCESS !!!!!!'
        else:
            print '!!!!!! Login FAILED !!!!!!'
    except KeyError:
        print 'KeyError in login application'
    finally:
        return state

def _transform_cb(template_file):
    return None
