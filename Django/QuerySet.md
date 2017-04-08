* Start shell
```
$ python manage.py shell
```
* Import
```
>>> from django.contrib.auth.models import User
>>> from blog.models import Post
```
* Create
```
>>> post = Post(title='One more post',
slug='one-more-post',
body='Post body.',
author=user)
```
* Save
```
post.save()
```
* Filter
```
>>> Post.objects.filter(publish__year=2015, author__username='admin')
```
```
>>> Post.objects.filter(publish__year=2015).filter(author__username='admin')
```
* Create model manager
``models.py``
```
class PublishedManager(models.Manager):
def get_queryset(self):
    return super(PublishedManager, self).get_queryset()\
                .filter(status='published')
```
