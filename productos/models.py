from django.db import models



class AuthGroup(models.Model):
    name = models.CharField(max_length=150, unique=True)  

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'auth_group'  # Nombre de la tabla en la base de datos


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'auth_group_permissions'  # Nombre de la tabla en la base de datos
        unique_together = (('group', 'permission'),)  # Asegura que no haya duplicados


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'auth_permission'  # Nombre de la tabla en la base de datos
        unique_together = (('content_type', 'codename'),)  # Asegura que no haya duplicados


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150, unique=True)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'auth_user'  # Nombre de la tabla en la base de datos


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'auth_user_groups'  # Nombre de la tabla en la base de datos
        unique_together = (('user', 'group'),)  # Asegura que no haya duplicados


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'auth_user_user_permissions'  # Nombre de la tabla en la base de datos
        unique_together = (('user', 'permission'),)  # Asegura que no haya duplicados


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'django_admin_log'  # Nombre de la tabla en la base de datos


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'django_content_type'  # Nombre de la tabla en la base de datos
        unique_together = (('app_label', 'model'),)  # Asegura que no haya duplicados


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'django_migrations'  # Nombre de la tabla en la base de datos
        

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'django_session'  # Nombre de la tabla en la base de datos


class Productos(models.Model):
    id = models.BigAutoField(primary_key=True) # Llave primaria
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_stock = models.IntegerField()
    fecha_creacion = models.DateField()
    fecha_ultima_modificacion = models.DateField()

    class Meta:
        managed = False  # No gestionar la base de datos automáticamente
        db_table = 'productos'

    
