# -*- coding: utf-8 -*-
import json

# index를 활용하여, hero를 관리하는 예제입니다.
hero_name = ['아이언맨', '데드풀', '울버린']
hero_health = [100, 300, 200]
hero_damage = [200, 30, 50]
hero_inventory = [
    {'gold': 500, 'weapon': '레이저'},
    {'gold': 300, 'weapon': '장검'},
    {'gold': 350, 'weapon': '클로'}
]


# 히어로가 죽으면 호출되는 함수
def hero_dies(hero_index):
    del hero_name[hero_index]
    del hero_health[hero_index]
    del hero_damage[hero_index]
    # <--- 개발자가 실수로 del hero_inventory[hero_index]를 빠뜨렸네요.


hero_dies(0)  # 0번 히어로를 죽입니다.
print(hero_name[0])
print(hero_health[0])
print(hero_damage[0])
print(json.dumps(hero_inventory[0], ensure_ascii=False))

# 데드풀
# 300
# 30
# {"weapon": "레이저", "gold": 500} <--- 0번 히어로는 죽었으니,
# 장검과 300 gold가 나와야 하는데, 개발자가 빼먹어서 버그가 생겼습니다.
