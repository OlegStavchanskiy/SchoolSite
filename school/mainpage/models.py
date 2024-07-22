from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    date = models.CharField(max_length=10)  # Новое поле с правильным форматом даты
    # Другие поля для урока

    def __str__(self):
        return str(self.date)


class Class(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)


class Journal(models.Model):
    student_id = models.IntegerField()  # Поле для хранения id студента
    lesson_date = models.CharField(max_length=12)  # Поле для хранения даты занятия
    subject = models.CharField(max_length=100)  # Поле для хранения предмета
    grade = models.PositiveSmallIntegerField(default=0) # Поле для хранения предмета

    def __str__(self):
        return f"{self.student_id} - {self.subject} - {self.lesson_date}"


class Schedule(models.Model):
    day_choices = (
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
    )

    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=day_choices)
    lesson_1 = models.CharField(max_length=50)
    lesson_2 = models.CharField(max_length=50)
    lesson_3 = models.CharField(max_length=50)
    lesson_4 = models.CharField(max_length=50)
    lesson_5 = models.CharField(max_length=50)
    lesson_6 = models.CharField(max_length=50)
    lesson_7 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.class_field} - {self.day}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > 300:
            return self.text[:300]
        else:
            return self.text
