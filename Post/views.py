from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.response  import Response
from rest_framework.views import APIView
from rest_framework import permissions,status

# Create your views here.

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for any request.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user making the request is the author of the post.
        return obj.author == request.user


class allPostsView(ListAPIView):
    serializer_class = postSerializer
    queryset = Post.objects.all()


class singlePostView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = singlePostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthorOrReadOnly]  # Apply the custom permission


class createPostView(CreateAPIView):
    serializer_class = postSerializer
    def post(self,request):
        serializer = postSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(author = self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class createCommentView(APIView):
    serializer_class = commentSerializer
    def get(self,request,post_slug):
        post = Post.objects.get(slug = post_slug)
        serializer = postSerializer(post, many = False)
        return Response(serializer.data)
    
    def post(self,request,post_slug):
        post = Post.objects.get(slug = post_slug)
        serializer = commentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(author = self.request.user,post = post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class deleteCommentView(APIView):
    serializer_class = commentSerializer
    def get(self,request,post_slug):
        post = Post.objects.get(slug = post_slug)
        comment = Comment.objects.get(post=post, author = self.request.user)
        serializer = commentSerializer(comment, many = False)
        return Response(serializer.data)

    def delete(self,request,post_slug):
        post = Post.objects.get(slug = post_slug)
        comment = Comment.objects.get(post=post, author = self.request.user)
        comment.delete()
        return Response({'message': 'The item has been deleted'}, status = status.HTTP_204_NO_CONTENT)


class createThreadView(APIView):
    serializer_class = commentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    def get(self,request,post_slug):
        post = Post.objects.get(slug = post_slug)
        serializer = postSerializer(post, many = False)
        return Response(serializer.data)
    
    def post(self,request,post_slug):
        post = Post.objects.get(slug = post_slug)
        serializer = commentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author = self.request.user,post = post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


 
class repostView(APIView):
    serializer_class = repostSerializer
    def get(self,request,post_slug):
        post = Post.objects.get(slug = post_slug)
        serializer = postSerializer(post, many = False)
        return Response(serializer.data)

    def post(self, request, post_slug):
        post = Post.objects.get(slug = post_slug)
        if Post.objects.filter(repost_post__repost_author=self.request.user, repost_post__post=post).exists():
            return Response({'detail': 'You have already reposted this post.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = repostSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.validated_data['repost'] = True
            serializer.save(repost_author = self.request.user,post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class qouteTweetView(APIView):
     serializer_class = quoteTweetSerializer
     def get(self,request,post_slug):
        post = Post.objects.get(slug = post_slug)
        serializer = postSerializer(post, many = False)
        return Response(serializer.data)
     
     def post(self, request, post_slug):
        post = Post.objects.get(slug = post_slug)
        if Post.objects.filter(repost_post__repost_author=self.request.user, repost_post__post=post).exists():
            return Response({'detail': 'You have already reposted this post.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = quoteTweetSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.validated_data['repost'] = True
            serializer.save(repost_author = self.request.user,post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class replyCommentView(APIView):
    serializer_class = commentSerializer
    def get(self,request,post_slug,comment_slug):
        post = Post.objects.get(slug = post_slug)
        comment = Comment.objects.get(post=post,comment_slug=comment_slug)
        serializer = commentSerializer(comment,many = False)
        return Response(serializer.data)
    
    def post(self,request,post_slug,comment_slug):
        post = Post.objects.get(slug = post_slug)
        comment = Comment.objects.get(post=post,comment_slug=comment_slug)
        serializer = commentSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author = self.request.user,post=post,parent_comment = comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        