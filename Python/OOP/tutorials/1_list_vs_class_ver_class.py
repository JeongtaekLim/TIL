# -*- coding: utf-8 -*-


# class 정의
class Character:

    def __init__(self, name, health, damage, inventory):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory

    def __repr__(self):
        return self.name


# Character 클래스의 오브젝트 생성
heroes = []
heroes.append(Character('아이언맨', 100, 200, {'gold': 500, 'weapon': '레이저'}))
heroes.append(Character('데드풀', 300, 30, {'gold': 300, 'weapon': '장검'}))
heroes.append(Character('울버린', 200, 50, {'gold': 350, 'weapon': '클로'}))

print(heroes)  # 히어로 리스트 확인
del heroes[0]  # 히어로 리스트에서 아이언맨 삭제
print(heroes)  # 히어로 리스트 재확인
