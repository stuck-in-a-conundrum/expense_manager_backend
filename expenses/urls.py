from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from expenses import views
from expenses.serializers import ExpenseCreateSerializer

urlpatterns = [
    path('expenses/', views.ExpensesGetList.as_view()),
    path('expense/<int:id>/', views.ExpenseDetail.as_view()),
    path('expense/create/', views.ExpenseCreateView.as_view()),
    path('saving/create/', views.SavingCreateView.as_view()),
    path('saving/<int:id>/', views.SavingDetail.as_view()),
    path('savings/', views.SavingsGetList.as_view()),
]