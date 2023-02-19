from django.db.models import Model, IntegerField, CharField, \
    BooleanField, ForeignKey, CASCADE, ImageField

from users.models import User


# ----------------------------------------------------------------
# Category model
class Category(Model):
    name: CharField = CharField(max_length=100)

    class Meta:
        verbose_name: str = 'Категория'
        verbose_name_plural: str = 'Категории'

    def __str__(self):
        return self.name


# ----------------------------------------------------------------
# Advertisement model
class Advertisement(Model):
    name: CharField = CharField(max_length=400)
    author: ForeignKey = ForeignKey(User, on_delete=CASCADE)
    price: IntegerField = IntegerField()
    description: CharField = CharField(max_length=1000)
    is_published: BooleanField = BooleanField()
    image: ImageField = ImageField(upload_to='images/')
    category: ForeignKey = ForeignKey(Category, on_delete=CASCADE)

    class Meta:
        verbose_name: str = 'Объявление'
        verbose_name_plural: str = 'Объявления'

        ordering: list[str] = ['-price']

    def __str__(self):
        return self.name
