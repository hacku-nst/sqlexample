# schapp/models.py
# Design of database layout

from django.db import models

class School(models.Model):
    school_id = models.IntegerField()
    school = models.CharField(max_length=60, null=True, default='')
    district_id = models.IntegerField()
    district = models.CharField(max_length=46, null=True, default='')

    class Meta:
         ordering = ('school_id',)

    def __str__(self):
        return '%d %s %d %s' % (self.school_id, self.school, self.district_id, self.district)


class Performance(models.Model):
    district_id = models.IntegerField()
    district = models.CharField(max_length=32, null=True, default='')
    school_id = models.IntegerField()
    school = models.CharField(max_length=65, null=True, default='')
    academic_year = models.IntegerField(null=True)
    subject = models.CharField(max_length=21, null=True, default='')
    subgroup = models.CharField(max_length=32, null=True, default='')
    grade_level = models.CharField(max_length=3, null=True, default='')
    participation_rate_2014_to_2015 = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    percentage_meets_or_exceeds_2014_to_2015 = models.DecimalField(max_digits=4, decimal_places=1, null=True)


    class Meta:
         ordering = ('district_id',)

    def __str__(self):
        #return '%d %s %d %s %d %s %s %s %0.2f %0.2f' % (self.school_id, self.school, self.district_id, self.district, self.academic_year, self.subject, self.subgroup, self.grade_level, self.participation_rate_2014_to_2015, self.percentage_meets_or_exceeds_2014_to_2015)
        return '%d %s %d %s %d %s %s %s' % (self.district_id, self.district, self.school_id, self.school, self.academic_year, self.subject, self.subgroup, self.grade_level)


