from django.db import models

class Themes(models.Model):
    title = models.CharField(max_length=200,verbose_name='ThemeTitle',unique=True,null=True)
    description1 = models.TextField(verbose_name='ThemeDescription1',null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'themes'
        verbose_name = 'Theme'
