# Datetime

## Parsing
```
import datetime
import re

from django.utils import six
from django.utils.timezone import get_fixed_timezone, utc

datetime_re = re.compile(
    r'(?P<year>\d{4})-(?P<month>\d{1,2})-(?P<day>\d{1,2})'
    r'[T ](?P<hour>\d{1,2}):(?P<minute>\d{1,2})'
)
match = date_re.match(value)
    if match:
        kw = {k: int(v) for k, v in six.iteritems(match.groupdict())}
        return datetime.datetime(**kw)
```