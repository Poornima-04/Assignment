import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comment


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment



class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        description = graphene.String()
        publish_date = graphene.String()
        author = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, title, description, publish_date, author):
        post = Post(
            title=title,
            description=description,
            publish_date=publish_date,
            author=author
        )

        post.save()

        return CreatePost(post=post)
    

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        title = graphene.String()
        description = graphene.String()
        publish_date = graphene.String()
        author = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, title=None, description=None, publish_date=None, author=None):
        post = Post.objects.get(id=id)

        if title:
            post.title = title

        if description:
            post.description = description

        if publish_date:
            post.publish_date = publish_date

        if author:
            post.author = author

        post.save()

        return UpdatePost(post=post)


class CreateComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.Int()
        text = graphene.String()
        author = graphene.String()

    comment = graphene.Field(CommentType)

    def mutate(self, info, post_id, text, author):
        post = Post.objects.get(id=post_id)

        comment = Comment(
            post=post,
            text=text,
            author=author
        )

        comment.save()

        return CreateComment(comment=comment)
    
class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    success = graphene.Boolean()

    def mutate(self, info, id):
        comment = Comment.objects.get(id=id)
        comment.delete()

        return DeleteComment(success=True)


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=graphene.Int())

    def resolve_posts(root, info):
        return Post.objects.all()
    def resolve_post(root, info, id):
        return Post.objects.get(id=id)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)