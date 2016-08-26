from django.db import models

# Create your models here.
status = (
    ('1','1'),
    ('0','0'),
    
)


# class User(models.User):
#     user_id			=       models.AutoField(primary_key=True, editable=False)
#     first_name        	=       models.CharField(max_length=45,null=True,blank=True)
#     last_name        	=       models.CharField(max_length=45,null=True,blank=True)
#     email        		=       models.CharField(max_length=45,null=True,blank=True)
# 	status			    =       models.CharField(max_length=1,default="1",choices=status)
#     created_date       	=       models.DateTimeField(null=True,blank=True)
# 	fb_token			=       models.CharField(max_length=100,null=True,blank=True)
# 	twitter_token		=       models.CharField(max_length=100,null=True,blank=True)
# 	google_token		=       models.CharField(max_length=100,null=True,blank=True)

#     def __unicode__(self):
#         return unicode(self.country_id)