# `SerializerMethodField`

If you are

* Using model serializer
* Wanting to add extra field on output

For example,
* `Model.py`
```python
class MyModel(models.Model):
    title = models.CharField(max_length=250)
```

* Before JSON result

```json
[
  {
    "title": "None",
    
    <!-- This is default field by Django -->
    "id": 1,
  }
]
```

* After JSON result
```json
[
  {
    "title": "None",
    "id": 1,

    <!-- New field -->
    "num_pages": 1
  }
]
```

* `Serializer.py`
```python
class MyModelSerializer(serializers.ModelSerializer):
    num_pages = serializers.SerializerMethodField()

    def get_num_pages(self, obj):
        return self.context['num_pages']

    class Meta:
        model = MyModel
        fields = ['title', 'id', 'num_pages']
```
* Extended version of `Serializer.py`
```python
class MyModelSerializer(serializers.ModelSerializer):
    num_pages = serializers.SerializerMethodField()
    num_items = serializers.SerializerMethodField()

    def get_num_pages(self, obj):
        return self.context['num_pages']

    def get_num_items(self, obj):
        return obj.items.all().count()

    class Meta:
        model = MyModel
        fields = ['title', 'id', 'num_pages', 'num_items']
```


* Documentation(django_rest_framwork)

http://www.django-rest-framework.org/api-guide/fields/#serializermethodfield

* Stackoverflow

http://stackoverflow.com/questions/18396547/django-rest-framework-adding-additional-field-to-modelserializer