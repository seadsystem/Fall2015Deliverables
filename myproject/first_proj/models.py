# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AppTable(models.Model):
    date = models.TextField()
    use = models.FloatField()

    class Meta:
        managed = False
        db_table = 'app_table'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Better(models.Model):
    date_time = models.TextField(db_column='date & time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    use_kw_field = models.FloatField(db_column='use [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'better'


class DbTableTest(models.Model):
    date = models.TextField()
    use = models.FloatField()

    class Meta:
        managed = False
        db_table = 'db_table_test'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fhrs(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    date_time = models.TextField(db_column='date & time', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    use_kw_field = models.FloatField(db_column='use [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gen_kw_field = models.FloatField(db_column='gen [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    maxvrmsa_v_field = models.FloatField(db_column='maxvrmsa [v]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    maxvrmsb_v_field = models.FloatField(db_column='maxvrmsb [v]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    netmeter_kw_field = models.FloatField(db_column='netmeter [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    consumption_kw_field = models.FloatField(db_column='consumption [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    powers_kw_field = models.FloatField(db_column='powers [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    powerg_kw_field = models.FloatField(db_column='powerg [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    panel1_kw_field = models.FloatField(db_column='panel1 [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    panel2_kw_field = models.FloatField(db_column='panel2 [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    panel3_kw_field = models.FloatField(db_column='panel3 [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vrmsa_v_field = models.FloatField(db_column='vrmsa [v]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    vrmsb_v_field = models.FloatField(db_column='vrmsb [v]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    i11_a_field = models.FloatField(db_column='i11 [a]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    i12_a_field = models.FloatField(db_column='i12 [a]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    i21_a_field = models.FloatField(db_column='i21 [a]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    i22_a_field = models.FloatField(db_column='i22 [a]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    i31_a_field = models.FloatField(db_column='i31 [a]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    i32_a_field = models.FloatField(db_column='i32 [a]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    f2_hz_field = models.FloatField(db_column='f2 [hz]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    f1_hz_field = models.FloatField(db_column='f1 [hz]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    shed_kw_field = models.FloatField(db_column='shed [kw]', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'fhrs'
