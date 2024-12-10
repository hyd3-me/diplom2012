from django.contrib.auth.models import User

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
