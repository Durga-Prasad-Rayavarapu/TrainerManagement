from django.db import models


# Create your models here.
class CityInfo(models.Model):
    City_Name = models.CharField(max_length=50)

    class Meta:
        db_table = 'City_info'

    def __str__(self):
        return f'City={self.City_Name}'


class CourseInfo(models.Model):
    Course_Name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Course_Info'

    def __str__(self):
        return f'{self.Course_Name}'


class Trainer_Register(models.Model):
    Trainer_Name = models.CharField(max_length=50)
    Trainer_Age = models.IntegerField(default=None)
    Trainer_Phone = models.BigIntegerField(default=None)
    Trainer_Password = models.CharField(max_length=50)
    Trainer_Email = models.CharField(max_length=50)
    Trainer_city = models.ForeignKey(CityInfo, on_delete=models.CASCADE, default=None)

    class Meta:
        db_table = 'Trainer_Registration_info'

    def __str__(self):
        return f'{self.Trainer_Name}'



class Trainer_Assign(models.Model):
    tname = models.ForeignKey(Trainer_Register, on_delete=models.CASCADE, default=None)
    tbatch_no = models.IntegerField(default=None)
    course = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField()

    class Meta:
        db_table = 'Trainer_Data'

    def __str__(self):
        return f'TrainerName = {self.tname}\n Batch_No {self.tbatch_no}\n Date = {self.date}\n course={self.course}'
