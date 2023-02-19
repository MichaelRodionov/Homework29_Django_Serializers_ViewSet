from django.db.models import Model, CharField, IntegerField, DecimalField, ManyToManyField, TextChoices


# ----------------------------------------------------------------
# Location model
class Location(Model):
    name: CharField = CharField(max_length=50)
    lat: DecimalField = DecimalField(max_digits=10, decimal_places=6, null=True)
    lng: DecimalField = DecimalField(max_digits=10, decimal_places=6, null=True)

    class Meta:
        verbose_name: str = 'Локация'
        verbose_name_plural: str = 'Локации'

    def __str__(self):
        return self.name


# ----------------------------------------------------------------
# User model
class User(Model):

    class Roles(TextChoices):
        ADMIN = 'admin', 'Админ'
        MODERATOR = 'moderator', 'Модератор'
        MEMBER = 'member', 'Пользователь'

    first_name: CharField = CharField(max_length=20)
    last_name: CharField = CharField(max_length=50)
    username: CharField = CharField(max_length=50)
    password: CharField = CharField(max_length=50)
    role: CharField = CharField(max_length=50)
    age: IntegerField = IntegerField()
    locations: ManyToManyField = ManyToManyField(Location)

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'

    def __str__(self):
        return self.username
