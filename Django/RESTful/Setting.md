# Setting

## Installation
* package install
```
pip install djangorestframework
```
* edit settings.py
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
## Parser

From Postman, you may want to send data as `form-data` or `x-www-form-urlencoded`

You need to tell Django which parser is used for parsing that data.

[django-rest-framwork document](http://www.django-rest-framework.org/api-guide/parsers/#formparser)

1. Describe it in class 

```py
class FestivalDetail(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        data = request.data

        return Response(data)
```

2. Describe it in `settings.py`
```py
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.JSONParser',
    )
}
```