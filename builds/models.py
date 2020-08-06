from django.db import models

# Create your models here.


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Билд')
    char1 = models.CharField(max_length=50, verbose_name='Профа первого чара')
    items1 = models.TextField(null=True, blank=True, verbose_name='Шмот первого чара')
    char2 = models.CharField(max_length=50, verbose_name='Профа второго чара')
    items2 = models.TextField(null=True, blank=True, verbose_name='Шмот второго чара')
    char3 = models.CharField(max_length=50, verbose_name='Профа третьего чара')
    items3 = models.TextField(null=True, blank=True, verbose_name='Шмот третьего чара')
    char4 = models.CharField(max_length=50, verbose_name='Профа четвертого чара')
    items4 = models.TextField(null=True, blank=True, verbose_name='Шмот четвертого чара')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')


    class Meta:
        verbose_name_plural = 'Билды'
        verbose_name = 'Билд'
        ordering = ['published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
