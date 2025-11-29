from django.urls import path
from .views import SolveEquationView, HistoryListView, HistoryDetailView

urlpatterns = [
    path('solve/', SolveEquationView.as_view(), name='solve_equation'),
    path('history/', HistoryListView.as_view(), name='history_list'),
    path('history/<str:pk>/', HistoryDetailView.as_view(), name='history_detail'),
]
