from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from TwitterAPI.utils import CustomResponse
from TwitterAPI.serializers.like import PostLikeSerializer, CommentLikeSerializer
from TwitterAPI.models.like import PostLike, CommentLike
from TwitterAPI.models.posts import Post
from TwitterAPI.models.comments import Comments


class PostLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        user = request.user
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return CustomResponse.error(
                status=True,
                message="Post not found"
            )
        
        like, created = PostLike.objects.get_or_create(
            user=user,
            post=post,
            defaults={'is_like': True}
        )
        if not created:
            like.is_like = not like.is_like
            like.save()

            serializer = PostLikeSerializer(like)
            return CustomResponse.success(
                status=True,
                message="Post like updated",
                data=serializer.data
            )
        

class CommentLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, commant_id):
        user = request.user
        try:
            comment = Comments.objects.get(id=commant_id)
        except Comments.DoesNotExist:
            return CustomResponse.error(
                status=False,
                message="Comment not found"
            )
        
        
        like, created = CommentLike.objects.get_or_create(
            user=user,
            comment=comment,
            defaults={'is_like': True}
        )
        if not created:
            like.is_like = not like.is_like 
            like.save()


        serializer = CommentLikeSerializer(like)
        return CustomResponse.success(
            status=True,
            message="Comment like updated",
            data=serializer.data
        )
