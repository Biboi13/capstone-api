from django.db import models

# Create your models here.

#table_1
class VCT(models.Model):
	vct_name = models.CharField(max_length=200)
	vct_active_users = models.CharField(max_length=200)
	vct_developer = models.CharField(max_length=200)
	
	def __str__(self):
		return self.vct_name
#table_2
class Prob_occur(models.Model):
	probl_occur_name = models.CharField(max_length=200)

	def __str__(self):
		return self.probl_occur_name
#table_3

class Respondance_type(models.Model):
	res_type = models.CharField(max_length=200)

	def __str__(self):
		return self.res_type

#table_4
class Respondance(models.Model):
    res_name       = models.CharField(max_length=200)
    res_place      = models.CharField(max_length=200)
    res_used_vct   = models.ForeignKey(VCT, on_delete=models.CASCADE)
    res_internet_bandwidth = models.CharField(max_length=200)
    res_problem_occurred   = models.ForeignKey(Prob_occur, on_delete=models.CASCADE)
    res_satifactory        = models.CharField(max_length=200)
    res_started_using_vct_name = models.DateField('date published')
    res_recommend_vct          = models.CharField(max_length=200)
    res_type  = models.ForeignKey(Respondance_type, on_delete=models.CASCADE)
    
    def __str__(self):
	    return self.res_name