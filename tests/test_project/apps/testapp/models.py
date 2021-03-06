from django.db import models

class TestModel(models.Model):
    test1 = models.CharField(max_length=1, blank=True, null=True)
    test2 = models.CharField(max_length=1, blank=True, null=True)
    
class ExpressiveTestModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    never_shown = models.TextField()
    
class Comment(models.Model):
    parent = models.ForeignKey(ExpressiveTestModel, related_name='comments')
    content = models.TextField()

class AbstractModel(models.Model):
    some_field = models.CharField(max_length=32, default='something here')
    
    class Meta:
        abstract = True
        
class InheritedModel(AbstractModel):
    some_other = models.CharField(max_length=32, default='something else')
    
    class Meta:
        db_table = 'testing_abstracts'

class PlainOldObject(object):
    def __emittable__(self):
        return {'type': 'plain',
                'field': 'a field'}

class ListFieldsModel(models.Model):
    kind = models.CharField(max_length=15)
    variety = models.CharField(max_length=15)
    color = models.CharField(max_length=15)

class Issue58Model(models.Model):
    read = models.BooleanField(default=False)
    model = models.CharField(max_length=1, blank=True, null=True)

class ConditionalFieldsModel(models.Model):
    field_one = models.CharField(max_length=15)
    field_two = models.CharField(max_length=15)
    fk_field = models.ForeignKey(TestModel)

class CircularA(models.Model):
    link = models.ForeignKey('testapp.CircularB', null=True)
    name = models.CharField(max_length=15)

class CircularB(models.Model):
    link = models.ForeignKey('testapp.CircularC', null=True)
    name = models.CharField(max_length=15)

class CircularC(models.Model):
    link = models.ForeignKey('testapp.CircularA', null=True)
    name = models.CharField(max_length=15)

