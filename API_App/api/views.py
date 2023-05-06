from rest_framework.viewsets import ModelViewSet
from API_App.models import Post
from API_App.api.serializers import PostSerializer 

class post_api_viewset(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()