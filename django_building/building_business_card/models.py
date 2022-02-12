from django.db import models


class Wallpaper(models.Model):

    name = models.CharField(max_length=20)
    image = models.ImageField()


class Contact(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='Name')
    phone = models.BigIntegerField(verbose_name='Phone')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.phone} {self.email}"

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class Project(models.Model):

    title = models.CharField(max_length=100, verbose_name='Project')
    about = models.TextField(max_length=255, verbose_name='Description')
    place = models.CharField(max_length=100, verbose_name='Place')
    project_link = models.CharField(max_length=500, verbose_name='Link')
    start = models.IntegerField(verbose_name='Year of start')
    end = models.IntegerField(verbose_name='Year of end', null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = '-end',
        verbose_name = 'project'
        verbose_name_plural = 'projects'


class OldProject(models.Model):

    title = models.CharField(max_length=100, verbose_name='Project')
    about = models.TextField(max_length=255, verbose_name='Description')
    place = models.CharField(max_length=100, verbose_name='Place')
    start = models.IntegerField(verbose_name='Year of start')
    end = models.IntegerField(verbose_name='Year of end', null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = '-end',
        verbose_name = 'old project'
        verbose_name_plural = 'old projects'


class Vacancy(models.Model):

    position = models.CharField(max_length=100, verbose_name='должность')

    def __str__(self):
        return f"{self.position}"

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'


class NewEmployee(models.Model):

    position = models.ForeignKey(Vacancy, on_delete=models.DO_NOTHING, verbose_name='Доступные должности')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    phone = models.BigIntegerField(verbose_name='телефон')
    year = models.IntegerField(max_length=10, verbose_name='год рождения')
    location = models.CharField(max_length=100, verbose_name='город, в котором сейчас находитесь')

    def __str__(self):
        return f"{self.position} | {self.first_name} {self.last_name} {self.phone}"

    class Meta:
        verbose_name = 'new employee'
        verbose_name_plural = 'new employees'