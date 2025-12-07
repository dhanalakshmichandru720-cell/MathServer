from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # URL to open the rectangle area page
    path('areaofrectangle/', views.rectarea, name='areaofrectangle'),

    # Root URL for the same function (optional)
    path('', views.rectarea, name='areaofrectangle_root'),
]
