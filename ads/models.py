from django.db import models

# from media.models import Media


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    age = models.CharField(max_length=3)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    # locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username

    @property
    def locations_name(self):
        return self.locations.name if self.locations else None


# class Media(models.Model):
#     name = models.CharField(max_length=20, null=True)
#     image = models.ImageField(upload_to='images/', null=True)
#
#     class Meta:
#         verbose_name = "Медиа"
#         verbose_name_plural = "Медиа"
#
#     def __str__(self):
#         return self.name


class Ad(models.Model):
    # STATUS = [
    #     ("False", "Отсутствует"),
    #     ("True", "В наличии"),
    #     ("needs verification", "Требуется проверить на наличие")
    # ]
    # STATUS = [
    #     (False, "Отсутствует"),
    #     (True, "В наличии")
    # ]
    name = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    # is_published = models.CharField(max_length=18, choices=STATUS, default="needs verification")
    is_published = models.BooleanField(default=False)
    # image = models.ForeignKey(Media, on_delete=models.DO_NOTHING, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Представление"
        verbose_name_plural = "Представления"

    def __str__(self):
        return self.name

    @property
    def author_name(self):
        return self.author.username if self.author else None
