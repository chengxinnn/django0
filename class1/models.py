# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bookhouse(models.Model):
    house_id = models.AutoField(db_column='House_ID', primary_key=True)  # Field name made lowercase.
    house_name = models.CharField(db_column='House_Name', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.house_name
    class Meta:
        managed = False
        db_table = 'bookhouse'


class Bookinfo(models.Model):
    book_id = models.IntegerField(db_column='Book_ID', primary_key=True)  # Field name made lowercase.
    book_name = models.CharField(db_column='Book_Name', max_length=60)  # Field name made lowercase.
    book_author = models.CharField(db_column='Book_Author', max_length=60)  # Field name made lowercase.
    book_price = models.FloatField(db_column='Book_Price')  # Field name made lowercase.
    book_house = models.CharField(db_column='Book_House', max_length=50)  # Field name made lowercase.
    book_number = models.IntegerField(db_column='Book_Number')  # Field name made lowercase.
    book_type = models.CharField(db_column='Book_Type', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.book_name
    class Meta:
        managed = False
        db_table = 'bookinfo'


class Booktype(models.Model):
    type_id = models.AutoField(db_column='Type_ID', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='Type_Name', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.type_id
    class Meta:
        managed = False
        db_table = 'booktype'


class Class1Bookinfo(models.Model):

    class Meta:
        managed = False
        db_table = 'class1_bookinfo'


class Class1Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class1_person'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Users(models.Model):
    user_id = models.IntegerField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=50)  # Field name made lowercase.
    user_password = models.CharField(db_column='User_Password', max_length=50)  # Field name made lowercase.
    def __str__(self):
        return self.user_name
    class Meta:
        managed = False
        db_table = 'users'
