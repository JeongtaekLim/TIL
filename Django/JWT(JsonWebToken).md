### JWT installation
JWT is JSON Web Token. It can replace original Django login
```
$ pip install djangorestframework-jwt
```
In your django Settings.py
```
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
```
In your urls.py
```
from rest_framework_jwt.views import obtain_jwt_token
#...

urlpatterns = patterns(
    '',
    # ...

    url(r'^api-token-auth/', obtain_jwt_token),
)
```
