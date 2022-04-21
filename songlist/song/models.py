from django.db import models

class Songs(models.Model):
    Initial_Choices = (
        (1,"A"),
        (2,"B"),
        (3,"C"),
        (4,"D"),
        (5,"E"),
        (6,"F"),
        (7,"G"),
        (8,"H"),
        (9,"I"),
        (10,"J"),
        (11,"K"),
        (12,"L"),
        (13,"M"),
        (14,"N"),
        (15,"O"),
        (16,"P"),
        (17,"Q"),
        (18,"R"),
        (19,"S"),
        (20,"T"),
        (21,"U"),
        (22,"V"),
        (23,"W"),
        (24,"X"),
        (25,"Y"),
        (26,"Z"),
    )
    Song_ID = models.AutoField('Song_ID',db_column='Song_ID',primary_key=True)
    Song_Name = models.CharField('Song_name',db_column='Song_Name',max_length=255,null=False,unique=True)
    Language = models.CharField('Language',db_column='Language',max_length=255,null=False)
    Singer = models.CharField('Singer',db_column='Singer',max_length=255,null=False)
    Initial = models.SmallIntegerField('Initial',db_column='Initial',choices = Initial_Choices,null=True)
    Remark = models.CharField('Remark',db_column='Remark',max_length=255,null=True,blank=True)
    class Meta:
        db_table = 'Songs'
