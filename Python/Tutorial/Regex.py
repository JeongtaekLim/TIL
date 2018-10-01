# -*- coding: utf-8 -*-
import re
original = "성은 <%=profile.last_name%>, 이름은 <%=profile.first_name%>이신 너님 안녕하세요, 알고리즘랩스에서 문자를 보내드립니다."
p = re.compile('<%=(.+?)\.(.+?)%>')

first_name = '정택'
last_name = '임'
match = None
match = p.finditer(original)
modified = ""
curIdx = 0
for m in match:
    # m.group(0): <%=profile.last_name%>
    # m.group(1): profile
    # m.group(2): last_name
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.start(), m.end())
    c = ""
    if m.group(2) == 'first_name':
        c = first_name
    elif m.group(2) == 'last_name':
        c = last_name
    clen = m.end() - m.start()
    modified += original[curIdx: m.start()] + c
    print(modified)
    curIdx = m.end()
modified += original[curIdx:]
print(modified)