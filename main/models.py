from django.db import models

type_choices = [('CLUB', 'Club'), ('DEPARTMENT', 'Department'), ('DEPT_ASSOC', 'Departmental Association'),
                ('CULT_ASSOC', 'Cultural Association')]


class SearchForm(models.Model):
        type = models.CharField(
            max_length = 30,
            choices = type_choices,
            default = 0,
        )
        interests = models.CharField(max_length = 20, default = "leisure")

class StudSearchForm(models.Model):
        type = models.CharField(
            max_length = 30,
            choices = type_choices,
            default = 0,
        )
        interests = models.CharField(max_length = 20, default = "leisure")



# Create your models here.
