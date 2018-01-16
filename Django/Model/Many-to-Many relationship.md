# Many-to-Many relationship

* Documentation

https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/


* `count()`

```python
Article.objects.filter(publications__title__startswith="Science").count()
```