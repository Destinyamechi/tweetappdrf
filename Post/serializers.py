from rest_framework import serializers
from .models import *


class commentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source = 'author.username',read_only = True)
    class Meta:
        model = Comment
        fields = ('author_name','content','created_at',)
        read_only_fields = ('created_at','post',)




class postSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source = 'author.username',read_only = True)
    class Meta:
        model = Post
        fields = ('author_name','content','slug','created_at',)
        read_only_fields = ('created_at',)


class repostSerializer(serializers.ModelSerializer):
    repost_post = postSerializer(many = False,read_only = True)
    author = serializers.CharField(source = 'repost_author.username',read_only=True)
    class Meta:
        model = Repost
        fields = ('repost_post','repost','author','reposted_at',)
        read_only_fields = ('repost','repost_author','reposted_at',)


class quoteTweetSerializer(serializers.ModelSerializer):
    quotetweet_post = postSerializer(many = False,read_only = True)
    author = serializers.CharField(source = 'repost_author.username',read_only = True)
    class Meta:
        model = QouteTweet
        fields = ('quotetweet_post','quote_tweet','repost','author','reposted_at',)
        read_only_fields = ('repost','repost_author','reposted_at',)


class singlePostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source = 'author.username',read_only = True)
    comments = commentSerializer(many = True, read_only = True)
    repost_post = repostSerializer(many = True, read_only = True)
    quotetweet_post = quoteTweetSerializer(many = True, read_only = True)
    class Meta:
        model = Post
        fields = ('author_name','content','created_at','comments','repost_post','quotetweet_post',)
        read_only_fields = ('created_at',)






