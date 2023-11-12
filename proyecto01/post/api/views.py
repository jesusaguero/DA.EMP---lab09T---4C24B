from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerializer

class PostApiViewset(ModelViewSet):
    #creamos un seralizador, nos va a indicar los datos
    #que nos va a devolver
    #todos los datos de la base de datos
    serializer_class = PostSerializer
    queryset=Post.objects.all()
