from django.contrib.auth.models import User
import bcrypt

from proj_fix import proj_data as data
from app_fixgroups import models as fix_models


def try_me(fn):
    # return func resp or err
    def do_func(*args):
        try:
            return fn(*args)
        except Exception as e:
            #logger.error(e)
            print(e)
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

@try_me
def create_group(name, pwd_str):
    hashed = bcrypt.hashpw(pwd_str.encode('utf-8'), bcrypt.gensalt())
    return 0, fix_models.FixGroup.objects.create(name=name, h_pwd=hashed)

@try_me
def check_pwd4group(group_obj, pwd):
    status = bcrypt.checkpw(pwd.encode('utf-8'), group_obj.h_pwd)
    if not status:
        return 1, group_obj
    return 0, group_obj
