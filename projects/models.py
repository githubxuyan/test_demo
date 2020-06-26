from django.db import models


# Create your models here.
# 一个mysql软件中，可以有多个数据库
# 一个数据库，有多个表
# 一张表，有多条数据


class Projects(models.Model):
    name = models.CharField(verbose_name='hello world', name=None, primary_key=False,
                            max_length=100, unique=False, blank=False, null=False,
                            db_index=False, rel=None, editable=True,
                            serialize=True, unique_for_date=None, unique_for_month=None,
                            unique_for_year=None, choices=None, help_text='', db_column=None,
                            db_tablespace=None, auto_created=False, validators=(),
                            error_messages=None)
    leader = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '表表表'
        db_table = 'table'
