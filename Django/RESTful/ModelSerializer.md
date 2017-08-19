# ModelSerializer

If you want to override model serializer,
```json
{
    ...
    "user": 1, // you may want to hide id and show name
    "language": 2 // you may want to get language name rather than id
},
```
```json
{
    ...
    "user": "jtlim",
    "language": "c_cpp"
},
```

```python
class MySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    language = serializers.ReadOnlyField(source='language.name')

    class Meta:
        model = MyModel
        fields = (..., 'user', 'language')
```