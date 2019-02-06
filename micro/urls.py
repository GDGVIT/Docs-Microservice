from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("import_doc/", views.import_doc,name="import_doc"),
    path("paste_link/", views.paste_link, name="paste_link"),
    path("create_new/", views.create_new, name="create_new"),
    path("showform/", views.showform, name="showform")

]