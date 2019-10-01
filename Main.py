import sys, logging, os, random, math, open_color, arcade

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Shooter"
STARTING_LOCATION = (200, 100)
BULLET_DAMAGE = 10
NUM_ENEMIES = 5
ENEMY_HP = 100
HIT_SCORE = 10
KILL_SCORE = 100

class Bullet(arcade.Sprite):
    def __init__(self, position, velocity, damage):
        super().__init__("assets/new_bullet.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):
        self.center_x += self.dx
        self.center_y += self.dy


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/space-ship.gif", 0.5)
        (self.center_x, self.center_y) = STARTING_LOCATION
        
        

class Enemy(arcade.Sprite):
    def __init__(self, position):
        super().__init__("assets/jelly fish animation.gif", 0.3)
        self.hp = ENEMY_HP
        (self.center_x, self.center_y) = position
    

class Window(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.set_mouse_visible(False)
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player = Player()
        self.score = 0
        arcade.set_background_color(open_color.teal_3)



    def setup(self):
        for i in range(NUM_ENEMIES):
            x = 60 * (i+1) + 20
            y = 500
            enemy = Enemy((x,y))
            self.enemy_list.append(enemy)            
        

    def update(self, delta_time):
        self.bullet_list.update()
        self.player.update()
        self.enemy_list.update()
        for e in self.enemy_list:
            damage = arcade.check_for_collision_with_list(e, self.bullet_list)
            for d in damage: 
                e.hp = e.hp - BULLET_DAMAGE
                self.score = self.score + HIT_SCORE
                if e.hp == 0: 
                    e.kill()
                    self.score = self.score + KILL_SCORE

        

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.score), 20, SCREEN_HEIGHT - 40, open_color.white, 16)
        self.player.draw()
        self.bullet_list.draw()
        self.enemy_list.draw()




    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x        

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            x = self.player.center_x
            y = self.player.center_y + 15
            bullet = Bullet((x,y),(0,10),BULLET_DAMAGE)
            self.bullet_list.append(bullet)


    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_key_press(self, key, modifiers):
       # if key == arcade.key.LEFT:
           # self.player.center_x = self.player.center_x + 1
        #elif key == arcade.key.RIGHT:
           # self.player.center_x = self.player.center_x - 1
       # elif key == arcade.key.UP:
           # self.player.center_y = self.player.center_y + 1
       # elif key == arcade.key.DOWN:
       #     self.player.center_y = self.player.center_y - 1
        pass
    def on_key_release(self, key, modifiers):
        pass


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()




if __name__ == "__main__":
    main()
