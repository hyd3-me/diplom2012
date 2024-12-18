from django.contrib.auth.models import User
import bcrypt
import datetime

from proj_fix import proj_data as data
from app_fixgroups import models as fix_models
from app_controldate import models as cd_models
from app_revision import models as rev_models


def try_me(fn):
    # return func resp or err
    def do_func(*args, **kwargs):
        try:
            return fn(*args)
        except Exception as e:
            #logger.error(e)
            print(e)
            return 1, e
    return do_func

@try_me
def now_plus_day(day_):
    time_zone_plus3 = datetime.timezone(datetime.timedelta(hours=3))
    return 0, datetime.datetime.now(tz=time_zone_plus3) + datetime.timedelta(days=day_)

@try_me
def get_today():
    return 0, datetime.date.today().isoformat()

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
def create_group(name, pwd_str, user_obj):
    hashed = bcrypt.hashpw(pwd_str.encode('utf-8'), bcrypt.gensalt())
    return 0, fix_models.FixGroup.objects.create(
        name=name, h_pwd=hashed, owner=user_obj)

@try_me
def check_pwd4group(group_obj, pwd):
    status = bcrypt.checkpw(pwd.encode('utf-8'), group_obj.h_pwd)
    if not status:
        return 1, group_obj
    return 0, group_obj

@try_me
def create_staff(group_obj, user_obj, rank=0):
    return 0, fix_models.Staff.objects.create(group=group_obj, user=user_obj, rank=rank)

@try_me
def get_staff_by_user(user_obj):
    return 0, user_obj.staff_set.all()

@try_me
def create_group_and_staff(name, pwd_str, user_obj):
    err, group = create_group(name, pwd_str, user_obj)
    err, staff = create_staff(group, user_obj, 7)
    return 0, (group, staff)

@try_me
def join_group(group_obj, user_obj):
    return create_staff(group_obj, user_obj)

@try_me
def get_group_by_name(name):
    return 0, fix_models.FixGroup.objects.get(name=name)

@try_me
def get_group_by_id(group_id):
    return 0, fix_models.FixGroup.objects.get(pk=group_id)

@try_me
def adddate(name, end_date, staff, group):
    return 0, cd_models.ControlDate.objects.create(
        name=name, e_date=end_date, owner=staff, group=group)

@try_me
def get_group_from_staff(staff):
    return 0, staff.group

@try_me
def get_end_date_by_group(group):
    return 0, cd_models.ControlDate.objects.filter(group=group).order_by('e_date')

@try_me
def get_qs_groups_by_user(user):
    err, qs_staff = get_staff_by_user(user)
    return 0, [staff.group for staff in qs_staff]

@try_me
def create_revision(name, group_obj):
    return 0, rev_models.Revision.objects.create(name=name, group=group_obj)