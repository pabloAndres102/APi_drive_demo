from rest_framework.routers import DefaultRouter
from API_App.api.views import post_api_viewset

router_post = DefaultRouter()

router_post.register(prefix='post', basename='post', viewset=post_api_viewset)