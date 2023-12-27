import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)    # 질문내용
    pub_date = models.DateTimeField('date published')   # 생성날짜

    def __str__(self):
        '''
        질문 메세지를 출력하기 위한 세팅
        '''
        return self.question_text
    
    def was_published_recently(self):
        '''
        어제 이후의 질문만을 출력하기 위한 세팅
        '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    '''
    Question의 답변을 위한 클래스
    Question의 외래키로 사용하고 있으며, 1개의 질문에 대해 n개의 답변이 가능하므로, 일 대 다의 관계임
    CASCADE : Question에서 질문이 삭제되면 Choice 내에서도 관련된 데이터가 삭제됨
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 선택지에 해당하는 질문
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)                              # 투표 수

    def __str__(self):
        return self.choice_text