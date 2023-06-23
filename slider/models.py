from django.db import models
from tinymce import models as tiny_models


class Slider(models.Model):
    name = models.CharField(verbose_name='Название блока', max_length=50)
    heading = models.CharField(verbose_name='Заголовок блока', max_length=100)
    text = tiny_models.HTMLField(verbose_name='Текст', max_length=7000)
    img = models.ImageField(verbose_name='Баннер', upload_to='promo/', null=True, max_length=255)
    position = models.IntegerField(verbose_name='Позиция в очереди', default=1)
    url = models.URLField(verbose_name='Ссылка в Сибирь', max_length=255, null=True)
    active_from = models.DateField(verbose_name='Действует с')
    active_to = models.DateField(verbose_name='Действует до')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'slider'
        verbose_name = 'промо-блок'
        verbose_name_plural = 'Промо-блоки'
