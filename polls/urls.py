#app에서 처리해야 될 url 패턴 분석 한 것 처리하는 곳
#인덱스 뷰가 어떤 url을 처리하는 지 넣어줌

from django.urls import path
from.import views

app_name = 'polls'

#인덱스 함수가 오면 url로 이동해줘라
urlpatterns=[
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #ex: /polls/5/results.
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]