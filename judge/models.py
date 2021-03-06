#coding=utf-8
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from oj.contest.models import Contest
from oj.problem.models import Problem

# Create your models here.

LANGUAGE_CHOICES = (
	('c++', 'C++(GNU C++ 4.0)'),
	('c', 'C(GNU C 4.0)'),
	('python', 'Python (Python 2.4)'),
	('java', 'Java (Not supported yet)'),
)

RESULT_CHOICES = (
	('AC', '正确'),
	('TLE', '超出时间'),
	('MLE', '超出内存'),
	('RE', '运行错误'),
	('CE', '编译错误'),
	('WA', '答案错误'),
	('PE', '格式错误'),
	('OT', '时间结束'),
	('RV', '违规'),
	('WAIT', '等待测试'),
	('TESTING','正在测试'),
	('JE', '判题系统内部错误'),
)

class Judge(models.Model):
	user = models.ForeignKey(User, verbose_name = u'用户')
	problem = models.ForeignKey(Problem, verbose_name = u'判题')
	language = models.CharField('程序设计语言', default= 'c++',max_length = 100, choices=LANGUAGE_CHOICES)
	sourcecode = models.TextField('源代码')
	submittime = models.DateTimeField('提交时间')
	result = models.CharField('判题结果',default = 'WAIT', max_length = 100, blank = True, choices = RESULT_CHOICES)
	result_detail = models.TextField('判题结果详细描述', blank = True)
	incontest = models.ForeignKey(Contest, verbose_name = u'比赛', null = True, blank=True)
	
	def __unicode__(self):
		return u'%6d %10s %10s %8s %15s %5s' % (self.id, self.user, self.problem, self.language, self.submittime, self.result)

	class Admin:
		list_filter = ('user','submittime',u'result')
		list_display = ('id', u'user', u'problem', 'language', u'result')

	class Meta:
		ordering = ['-id']
		verbose_name = verbose_name_plural = u'判题'

class JudgeForm(ModelForm):
	class Meta:
		model = Judge
