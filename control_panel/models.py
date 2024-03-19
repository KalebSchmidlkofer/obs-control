from django.db import models


SOURCE_TYPE = (
  (0,'mic'),
  (1,'GameCapture'),
  (2,'WindowCapture'),
  (3,'AudioOutput')
  )

class scene(models.Model):
  name = models.CharField(max_length=100)
  active = models.BooleanField(default=False)
  

  def __str__(self):
    return self.name
  
class source(models.Model):
  id = models.IntegerField(primary_key=True)
  scene = models.ForeignKey(scene, on_delete=models.CASCADE, default=None, null=True)
  type = models.IntegerField(choices=SOURCE_TYPE, default=0)
  
  def __str__(self):
      return str(self.type)