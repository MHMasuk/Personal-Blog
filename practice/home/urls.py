from django.conf.urls import url
from home import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contract/$', views.ContractView.as_view(), name='contract'),
    url(r'^create/$', views.CreatePostView.as_view(), name='create'),
    url(r'^update/(?P<pk>[-\d]+)/$', views.UpdatePostView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[-\d]+)/$', views.DeletePostView.as_view(), name='delete'),
]