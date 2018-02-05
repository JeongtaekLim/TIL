# [Django: How to add ForeignKey to multiple models](https://medium.com/@bhrigu/django-how-to-add-foreignkey-to-multiple-models-394596f06e84)

기본적으로, 한종류 이상의 모델에 대한 관계는 ForeignKey를 통해 생성한다.

하지만, 만약 __Article__ 와 __Post__ 모델을 가지고 있다고 가정해 보자

```python
class Article(models.Model):
    content = models.CharField(max_length=100)
class Post(models.Model):
    content = models.CharField(max_length=100)
```

이제, 우린 __Comment__ 모델도 가지고있다. __Article__ 과 __Post__ 는 둘다 __Comment__ 를 가질 수 있다.

우린, __Generic Relation__ 이라는개념을 사용한다. 

```python
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
class Comment(models.Model):
    comm = models.CharField(max_length=50)
    
    content_type =   models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')

```

위 세 줄은 generic relation을 사용할때는 항상 동일하게 적용된다.

`ContentType`은, `contenttypes` app에 속해있는 model이다. `ContentType`의 instance는 연결을 원하는 다른 model들을 querying하거나 returning하는 method를 가지고 있다.

## To relate a Commnet to an Article instance:
```python 
>>> art = Article.objects.get(id=1)
>>> c = Comment(content_object=art, comm='asdf')
>>> c.save()
>>> c.content_object
<Article: article1>
```

## To relate a Comment to Post instance:
```python
>>> pos= Post.objects.get(id=1)
>>> c= Comment(content_object=pos, comm='new comment')
>>> c.save()
>>> c.content_object
<Post: post1>
```

## Reverse Generic Relations
이제, 특정 __Article__ 또는 __Post__ 에서 __Comment__ 를 얻어오는 방법을 알아보자. 이는 __GenericRelation__ 을 통해 가능하다.

```python 
from django.contrib.contenttypes.fields import GenericRelation
class Article(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)
class Post(models.Model):
    content = models.CharField(max_length=100)
    comments = GenericRelation(Comment)
```

## Limit to specific models

By stack overflow, [How can I restrict Django's GenericForeignKey to a lit of models](https://stackoverflow.com/questions/6335986/how-can-i-restrict-djangos-genericforeignkey-to-a-list-of-models)

```python
class TaggedItem(models.Model):
        tag = models.SlugField()
        limit = models.Q(app_label = 'app', model = 'a') | models.Q(app_label = 'app', model = 'b') | models.Q(app_label = 'app2', model = 'c')
        content_type = models.ForeignKey(ContentType, limit_choices_to = limit)
        object_id = models.PositiveIntegerField()
        content_object = generic.GenericForeignKey('content_type', 'object_id')

```