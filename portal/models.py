# ruff: noqa: RUF012
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """Расширенный профиль пользователя (текущий сотрудник)."""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name="Пользователь"
    )
    employee = models.OneToOneField(
        'Employee',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='user_profile',
        verbose_name="Карточка сотрудника"
    )
    favorite_projects = models.ManyToManyField(
        'Project',
        blank=True,
        related_name='favorited_by',
        verbose_name="Избранные проекты"
    )
    missed_dates = models.JSONField(
        default=list,
        blank=True,
        verbose_name="Пропущенные даты (ТРЗ)"
    )

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return f"Профиль {self.user.username}"

class Employee(models.Model):
    """Сотрудник компании."""
    name = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность")
    team = models.ForeignKey(
        'Team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members',
        verbose_name="Команда"
    )
    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates',
        verbose_name="Руководитель"
    )
    city = models.CharField(max_length=100, blank=True, verbose_name="Город")
    birthday = models.DateField(null=True, blank=True, verbose_name="День рождения")
    email = models.EmailField(blank=True, verbose_name="Email")
    telegram = models.CharField(max_length=100, blank=True, verbose_name="Telegram")

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.position})"

class Team(models.Model):
    """Команда"""
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    mascot_icon = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Иконка маскота (SF Symbol)"
    )
    leaders = models.ManyToManyField(
        Employee,
        related_name='led_teams',
        blank=True,
        verbose_name="Руководители"
    )

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ['name']

    def __str__(self):
        return self.name

class WallPost(models.Model):
    """Пост на корпоративной стене."""
    tag = models.ForeignKey(
        'Tag',
        on_delete=models.PROTECT,
        verbose_name="Тег",
        related_name="posts"
    )
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    company = models.CharField(max_length=255, blank=True, verbose_name="Компания")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class InfoArticle(models.Model):
    """Статья в разделе «Полезная информация»."""
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    contacts = models.ManyToManyField(
        Employee,
        blank=True,
        related_name='info_articles',
        verbose_name="Контактные лица"
    )

    class Meta:
        verbose_name = "Информационная статья"
        verbose_name_plural = "Информационные статьи"

    def __str__(self):
        return self.title

class Project(models.Model):
    """Проект для учёта трудозатрат."""
    name = models.CharField(max_length=255, verbose_name="Название проекта")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['name']

    def __str__(self):
        return self.name

class TimeAllocation(models.Model):
    """Запись о трудозатратах за конкретный день и проект."""
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='allocations',
        verbose_name="Сотрудник"
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='allocations',
        verbose_name="Проект"
    )
    date = models.DateField(verbose_name="Дата")
    hours = models.PositiveIntegerField(
        default=0,
        verbose_name="Процент времени (0–100)"
    )

    class Meta:
        verbose_name = "Трудозатрата"
        verbose_name_plural = "Трудозатраты"
        unique_together = ['employee', 'project', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.employee.name} — {self.project.name} ({self.date})"

class Tag(models.Model):
    """Тег поста."""
    name = models.CharField(max_length=50, unique=True, verbose_name="Название")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

    def __str__(self):
        return self.name