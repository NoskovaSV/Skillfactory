from django.db import models

class AbstractBaseUser(models.Model):
    pass

class User(AbstractBaseUser):
    username = models.CharField('username')

class Author(models.Model):
    authors = models.OneToOneField(User)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        article_rating = self.article_rating
        return article_rating * 3
        return author_comments
        return comment_rating

class Category(models.Model):
    category_name = models.CharField(max_length=255, default="Default value", unique=True)

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # choice = models.ModelChoiceField(queryset= choice.objects.all(), required=False)
    A = 1
    B = 2
    choices = ((A, "article")), (B, "news")
    choice_field = models.IntegerField(default=0)
    creation_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through="PostCategory")
    header = models.CharField(max_length=255, default="Default value")
    text = models.TextField()
    post_rating = models.IntegerField(default=0)

def like(self):
    post_rating = self.post_rating
    return post_rating += 1

def dislike(self):
    post_rating = self.post_rating
    return post_rating -= 1

def preview(self):
    preview = self.preview
    return preview = models.CharField(max_length=124).append("...")

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

def like(self):
    comment_rating = self.comment_rating
    return comment_rating += 1

def dislike(self):
    comment_rating = self.comment_rating
    return comment_rating -= 1


