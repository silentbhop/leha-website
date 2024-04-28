from django.db import models

class MediaFiles(models.Model):
    title = models.CharField('Название', max_length=100)
    file = models.FileField('Файл', upload_to='files')
    date = models.DateField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
