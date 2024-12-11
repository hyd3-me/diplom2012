from django.contrib.auth.models import User

from proj_fix import proj_data as data


def try_me(fn):
    # return func resp or err
    def do_func(*args):
        try:
            return fn(*args)
        except Exception as e:
            #logger.error(e)
            return 1, e
    return do_func

@try_me
def get_user(user_id):
    return 0, User.objects.get(id=user_id)

@try_me
def get_all_users():
    return 0, User.objects.all()

@try_me
def create_user(tupl_name_pwd=data.USER1):
    return 0, User.objects.create_user(
        username=tupl_name_pwd[0], password=tupl_name_pwd[1])