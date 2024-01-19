from django.db import models
from django.contrib.auth.models import User

#above 'User' is imported as it is needed in below table as primary key
#else not needed

class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregnancies = models.FloatField()
    glucose = models.FloatField()
    BP = models.FloatField()
    skin_thickness= models.FloatField()
    Insulin = models.FloatField()
    BMI = models.FloatField()
    DPF = models.FloatField()
    age = models.FloatField()
    result_value = models.CharField(max_length=20)  # Adjust the max length as needed
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.user.username} at {self.timestamp}"
    

    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback #{self.id} for {self.user}"