from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

# Create your models here.
student_types = [
    ('leader', 'cohort leader'),
     ('deputy', 'vice leader'),
    ('secretary', 'secretary'),
    ('President', 'President'),
     ('member', 'member'), ]

class Student(models.Model):
  username = models.CharField(max_length=100, unique=True)
  first_name = models.CharField(max_length=200, null=True, blank=True)
  last_name = models.CharField(max_length=200, verbose_name='last name')
  status = models.BooleanField(default=True)
  email = models.EmailField(unique=True, null=True)
  student_type =models.CharField(max_length=100, choices=student_types, default='member')
  date_join = models.DateTimeField(default=now, blank=True)

  class Meta:
   ordering = ['-date_join']
  slug = models.SlugField(unique=True, blank=True)

  def save(self, *args, **kwargs):
        if not self.slug:
            # Generating slug from full name, ensure uniqueness
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
            # You might want to add extra code to ensure uniqueness, e.g., append a unique ID if needed
        super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"





class Student_Profile(models.Model):
  student = models.OneToOneField(Student,on_delete=models.CASCADE)
  bio = models.TextField()
  date_of_birth =models.DateField()
  address = models.CharField(max_length=300)
  rating = models.FloatField(default=0.0)
  profile_picture = models.ImageField(upload_to='student_profile')
  date_join = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.student.username}"






class Program(models.Model):
  courses = models.CharField(max_length=500)
  grade = models.IntegerField(default=0.0)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.courses}"








class CohortGroup(models.Model):
  name = models.CharField(max_length=200)
  date_join = models.DateTimeField(auto_now_add=True)
  students = models.ManyToManyField(Student, related_name='cohort_groups')
  def __str__(self):
    return f"{self.name}"