from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-слаг")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Poster(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название плаката")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена (руб.)")
    image = models.ImageField(upload_to='posters/', verbose_name="Изображение плаката")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posters', verbose_name="Категория")
    is_available = models.BooleanField(default=True, verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Плакат"
        verbose_name_plural = "Плакаты"

    def __str__(self):
        return self.title