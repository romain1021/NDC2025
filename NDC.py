import pyxel
import random

class Entity:
    x = 0
    y = 0
    life = 0
    items = []
    speed = 0
    strenght = 0
    name = ""

    def __init__(self, x, y, life, items, speed, strenght, name):
        self.x = x
        self.y = y
        self.life = life
        self.items = items
        self.speed = speed
        self.strenght = strenght
        self.name = name

    def update(self):
        pass

    def draw(self):
        pass

class Player(Entity):
    spriteX = 0
    spriteY = 0
    animPlayer = [[0, 16], [16, 16], [32, 16], [48, 16]]
    var = 0
    width = 16

    def __init__(self, x, y, life, items, speed, strenght, name):
        self.x = x
        self.y = y
        self.life = life
        self.items = items
        self.speed = speed
        self.strenght = strenght
        self.name = name
        self.spriteX = 0
        self.spriteY = 16
    
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.collisionMur() == 0:
                self.width = 16
                self.x += self.speed
                self.spriteX = self.animPlayer[self.var][0]
                self.spriteY = self.animPlayer[self.var][1]
            elif self.collisionMur() == 2:
                self.x = 250 - 16

        if pyxel.btn(pyxel.KEY_LEFT):
            if self.collisionMur() == 0:
                self.width = -16
                self.x -= self.speed
                self.spriteX = -self.animPlayer[self.var][0]
                self.spriteY = self.animPlayer[self.var][1]
            elif self.collisionMur() == 1: 
                self.x = 0 + 16

        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed

        if self.var == 3:
                self.var = 0
        else:
            self.var += 1

    def draw(self):
        pass

    # def collision(self, x1, x2, y1, y2):
    #     # if self.x >= x1:
    #     if self.x < x1 | self.x + 16 > x2:
    #         return 1
    #     # elif self.x <= x2:
    #     #     return 1
    #     elif self.y < y1 | self.y + 16 > y2:
    #         return 1
    #     # elif self.y <= y:
    #     #     return 1
    #     else:
    #         return 0
    
    def collisionMur(self):
        if self.x <= 0 +1:
            return 1
        if self.x +16 >= 255:
            return 2
        else: 
            return 0


class Monster(Entity):
    spriteX = 0
    spriteY = 0
    animMonster = [[64, 16], [80, 16], [96, 16], [112, 16]]
    var = 0
    width = 16

    def __init__(self, x, y, life, items, speed, strenght, name):
        self.x = x
        self.y = y
        self.life = life
        self.items = items
        self.speed = speed
        self.strenght = strenght
        self.name = name

    def update(self):
        rt = random.randint(0, 1)
        if rt == 0 :
            if self.collisionMur() == 0:
                self.width = 16
                self.x += self.speed
                self.spriteX = self.animMonster[self.var][0]
                self.spriteY = self.animMonster[self.var][1]
            elif self.collisionMur() == 2:
                self.x = 250 - 16

        if rt == 1:
            if self.collisionMur() == 0:
                self.width = -16
                self.x -= self.speed
                self.spriteX = -self.animMonster[self.var][0]
                self.spriteY = self.animMonster[self.var][1]
            elif self.collisionMur() == 1: 
                self.x = 0 + 16

        if self.var == 3:
                self.var = 0
        else:
            self.var += 1

    def draw(self):
        pass

    def collisionMur(self):
        if self.x <= 0 +1:
            return 1
        if self.x +16 >= 255:
            return 2
        else: 
            return 0
        
class Object:
    x = 0
    y = 0
    isCollected = False
    items = []

    def __init__(self, x, y, isCollected, items):
        x = x
        y = y
        isCollected = isCollected
        items = items
    
    def update(self):
        pass

    def draw(self):
        pass

class Game: 
    player = Player(30, 224, 1, [], 3, 1, "truc")
    monster = Monster(90, 224, 1, [], 3, 1, "mob")
    def __init__(self):
        pyxel.init(256, 256, title = "Cave Doom")
        pyxel.load("2.pyxres")
        pyxel.run(self.update, self.draw)        
    
    def update(self):
        self.player.update()
        self.monster.update()

        if self.player.x < (self.monster.x +16) and (self.player.x +16) > self.monster.x:
            print('aie1')
        elif self.player.x +16 < (self.monster.x) and (self.player.x) > self.monster.x +16:
            print('aie2')

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.player.x, self.player.y, 0, self.player.spriteX, self.player.spriteY, self.player.width, 16, 2)
        pyxel.blt(self.monster.x, self.monster.y, 0, self.monster.spriteX, self.monster.spriteY, self.monster.width, 16, 2)
        tm = 0
        for _ in range(16):
            pyxel.blt(tm, 240, 0, 0, 112, 16 , 16)
            tm += 16

Game()