from .import views
from django.urls import path


app_name =  "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("state1/", views.state_view, name="state_view"),
    path("state2/", views.statee_view, name="statee_view"),
    path("unite/", views.unite_view, name="unite_view"),
    path("kings/", views.kings_view, name="kings_view"),
    path("history/", views.history_view, name="history_view"),
    path("museums/", views.museums_view, name="museums_view"),
    path("education/", views.education_view, name="education_view"),
    path('book_visit/', views.book_visit, name='book_visit'),
    path("login/", views.login_view, name="login"),
    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),    




]