from django.urls import path

from apps.vianda import views

app_name = 'vianda'
urlpatterns = [
    # path("login", views.login_view, name="login"),
    path("registrar_vianda/", views.registrar_vianda, name="registrar_vianda"),
    path("listar_vianda/", views.listar_vianda, name="listar_vianda"),
 ]