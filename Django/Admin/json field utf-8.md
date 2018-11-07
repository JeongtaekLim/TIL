# json field utf-8

json field의 경우, 한글을 입력하면 utf-8 value를 보여주지 않는 이슈가 있다.

http://blog.qax.io/unescaped-utf-8-in-djangos-admin-with-jsonfield/

```py
import json

from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.forms.jsonb import (
    InvalidJSONInput,
    JSONField as JSONFormField,
)


class UTF8JSONFormField(JSONFormField):

    def prepare_value(self, value):
        if isinstance(value, InvalidJSONInput):
            return value
        return json.dumps(value, ensure_ascii=False)


class UTF8JSONField(JSONField):
    """JSONField for postgres databases.

    Displays UTF-8 characters directly in the admin, i.e. äöü instead of
    unicode escape sequences.
    """

    def formfield(self, **kwargs):
        return super().formfield(**{
            **{'form_class': UTF8JSONFormField},
            **kwargs,
        })
```