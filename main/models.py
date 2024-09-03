from django.db import models

class TodoList(models.Model):
    Name = models.CharField(max_length=100)
    Discription = models.TextField()
    Deadline = models.DateTimeField()

class Categories(models.Model):
     name = models.CharField(max_length= 150)
     Discription = models.TextField()
     def __str__(self):
        return self.name

class Tasks(models.Model):
    status = [
        ('Done', 'Done'),
        ('In Progress', 'In Progress'),
        ('Not Started', 'Not Started')
    ]
    Title = models.CharField(max_length=100)
    Discription = models.TextField()
    Deadline = models.DateTimeField()
    Status = models.CharField(max_length=50, choices=status)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.Title
    

class Comments(models.Model):
    Discription = models.TextField()
    CreationDate = models.DateTimeField(auto_now_add=True)
    Task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    