from django.urls import path

from apps.views import find_mode, find_d, x2_y10, x8_y10, x16_y10, index

urlpatterns = [
    path('find-mode', find_mode, name='find_mode'),
    path('find-d', find_d, name='find_d'),
    path('x2-y10', x2_y10, name='x2_y10'),
    path('x8-y10', x8_y10, name='x8_y10'),
    path('x16-y10', x16_y10, name='x16_y10'),
    path('', index, name='main_page')
]
