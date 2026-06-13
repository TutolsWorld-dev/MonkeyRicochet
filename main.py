
import pygame
from sys import exit
from random import choice
import webbrowser



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/PlayerXD/monkey1.png").convert_alpha()
        self.transform_image = pygame.transform.scale(self.image, (100, 100))
        self.image = self.transform_image
        self.rect= self.transform_image.get_rect(midbottom=(245, 680))

        #monkey_hitbox
        self.monkey_hitbox = self.rect.copy()  # Копируем размеры и позицию основного rect
        self.hitboks_position = 8  # Величина, на которую нужно уменьшить хитбокс слева
        self.left_side_hitboks = 13
        self.monkey_hitbox.width -= self.left_side_hitboks
        self.monkey_hitbox.left += self.hitboks_position

        self.first_platform_state = first_platform_state
        self.player_jump_state ="default"
        self.player_main_collision_state = player_main_collision_state
        self.player_gravity =0
        self.player_right_or_left_jump= 0


    def draw_rect(self):
        #проверка всех прямоугольников
       pygame.draw.rect(screen, (255, 0, 0), self.monkey_hitbox, 2)

    def keys_input(self):
        keys = pygame.key.get_pressed()
        if first_platform_state == "None" and self.player_jump_state == "default" and game_state :
            if keys[pygame.K_w] :
                self.player_gravity = -16
                self.player_right_or_left_jump =5
                self.player_jump_state = "jump"
        elif keys[pygame.K_w] and self.monkey_hitbox.right>=390 and self.player_jump_state == "default" and first_platform_state == "None": #and player_main_collision_state == True:
                   self.player_gravity = -16
                   self.player_right_or_left_jump = -5
                   self.player_jump_state = "jump"
                   global player_main_collision_state
                   player_main_collision_state =False

    def gravity_settings(self):
     if first_platform_state == "collide":
       if self.rect.bottom >= 680:
          self.rect.bottom = 680
       if self.monkey_hitbox.bottom >=680:
           self.monkey_hitbox.bottom = 680



     if platforms_go and self.player_jump_state == 'jump' and player_main_collision_state == False:
          self.player_right_or_left_jump += 0
          self.rect.x += self.player_right_or_left_jump
          self.monkey_hitbox.x += self.player_right_or_left_jump

          self.player_gravity +=1
          self.rect.y += self.player_gravity
          self.monkey_hitbox.y += self.player_gravity
          if player_main_collision_state :
              self.player_gravity = -0
              self.player_right_or_left_jump += 0
              self.player_right_or_left_jump += 0
              self.rect.x += self.player_right_or_left_jump
              self.monkey_hitbox.x += self.player_right_or_left_jump
              self.player_jump_state = "default"
              self.player_gravity += 0
              self.rect.y += self.player_gravity
              self.monkey_hitbox.y += self.player_gravity

     else:
         if first_platform_state == "None" and player_main_collision_state == True:
             self.rect.y += 2
             self.monkey_hitbox.y +=2
             self.player_jump_state = "default"
             #if self.player_state == "jump":
                 #player_main_collision_state = False

    def update(self):
        self.keys_input()
        self.gravity_settings()
        self.draw_rect()

class Null_Stick(pygame.sprite.Sprite):
    def __init__(self):
       super().__init__()
       self.start_platform_rect_spis = []
       self.hitboks_first = []

       stick = pygame.image.load("graphics/Sprites/stick.png").convert_alpha()


       #stick1

       self.norm_stick1_1 = pygame.transform.scale(stick, (170, 250))
       self.stick_rec1_1 = self.norm_stick1_1.get_rect(midbottom=(115, 400))
       self.start_platform_rect_spis.append(self.stick_rec1_1)

       self.stick1_hitbox = self.stick_rec1_1.copy()# Копируем размеры и позицию основного rect



       self.hitboks_position = 75  # Величина, на которую нужно уменьшить хитбокс слева
       self.left_side_hitboks = 150
       self.hitboks_height = 50
       self.hitboks_y_pos = 30

       self.stick1_hitbox.width -= self.left_side_hitboks
       self.stick1_hitbox.left += self.hitboks_position
       self.stick1_hitbox.height -= self.hitboks_height
       self.stick1_hitbox.bottom += self.hitboks_y_pos




       #stick2
       self.norm_stick1_2 = pygame.transform.scale(stick, (170, 170))
       self.stick_rec1_2 = self.norm_stick1_2.get_rect(midbottom=(390, 600))
       self.start_platform_rect_spis.append(self.stick_rec1_2)

       self.stick2_hitbox = self.stick_rec1_2.copy()  # Копируем размеры и позицию основного rect
       self.hitboks_position = 75  # Величина, на которую нужно уменьшить хитбокс слева
       self.left_side_hitboks = 150
       self.stick2_hitbox.width -= self.left_side_hitboks
       # для ізмененія положенія
       self.stick2_hitbox.left += self.hitboks_position
       self.stick2_hitbox.height -= self.hitboks_height
       self.stick2_hitbox.bottom += self.hitboks_y_pos




       #stick3
       self.norm_stick1_3 = pygame.transform.scale(stick, (170, 140))
       self.stick_rec1_3 = self.norm_stick1_3.get_rect(midbottom=(390, 125))
       self.start_platform_rect_spis.append(self.stick_rec1_3)

       self.stick3_hitbox = self.stick_rec1_3.copy()  # Копируем размеры и позицию основного rect
       self.hitboks_position = 75 # Величина, на которую нужно уменьшить хитбокс слева
       self.left_side_hitboks = 150
       self.stick3_hitbox.width -= self.left_side_hitboks
       # для ізмененія положенія
       self.stick3_hitbox.left += self.hitboks_position
       self.stick3_hitbox.height -= self.hitboks_height
       self.stick3_hitbox.bottom += self.hitboks_y_pos

       # stick4
       self.norm_stick1_4 = pygame.transform.scale(stick, (170, 170))
       self.stick_rec1_4 = self.norm_stick1_4.get_rect(midbottom=(390, -150))
       self.start_platform_rect_spis.append(self.stick_rec1_4)

       self.stick4_hitbox = self.stick_rec1_4.copy()  # Копируем размеры и позицию основного rect
       self.hitboks_position = 75 # Величина, на которую нужно уменьшить хитбокс слева
       self.left_side_hitboks = 150
       self.stick4_hitbox.width -= self.left_side_hitboks
       self.stick4_hitbox.height -= self.hitboks_height
       self.stick4_hitbox.bottom += self.hitboks_y_pos
       # для ізмененія положенія
       self.stick4_hitbox.left += self.hitboks_position

       self.hitboks_first.append(self.stick1_hitbox)
       self.hitboks_first.append(self.stick2_hitbox)
       self.hitboks_first.append(self.stick3_hitbox)
       self.hitboks_first.append(self.stick4_hitbox)

    def draw_platforms(self):
        screen.blit(self.norm_stick1_1, self.stick_rec1_1)
        screen.blit(self.norm_stick1_2, self.stick_rec1_2)
        screen.blit(self.norm_stick1_3, self.stick_rec1_3)
        screen.blit(self.norm_stick1_4,self.stick_rec1_4)

        pygame.draw.rect(screen, (255, 0, 0), self.stick1_hitbox, 2)
        pygame.draw.rect(screen, (255, 0, 0), self.stick2_hitbox, 2)
        pygame.draw.rect(screen, (255, 0, 0), self.stick3_hitbox, 2)
        pygame.draw.rect(screen, (255, 0, 0), self.stick4_hitbox, 2)


    def platforms_moving(self):
        if platforms_go == True:
           #Always have first position

           self.sticks_lowering = 2
           self.stick_rec1_1.y +=self.sticks_lowering
           self.stick_rec1_2.y += self.sticks_lowering
           self.stick_rec1_3.y += self.sticks_lowering
           self.stick_rec1_4.y += self.sticks_lowering

           self.stick1_hitbox.y += self.sticks_lowering
           self.stick2_hitbox.y += self.sticks_lowering
           self.stick3_hitbox.y += self.sticks_lowering
           self.stick4_hitbox.y += self.sticks_lowering

           if self.stick_rec1_3.bottom >= 210:
            global timer_stage
            timer_stage = "start"





    def update(self):
        self.platforms_moving()
        self.draw_platforms()


class Platforms(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.type = type
        self.images = []
        self.rects = []
        self.go_down = 2
        self.bullets_speed = 5
        self.index = 0
        self.stick_rect_spis =[]
        self.bullets_list = []
        self.thorns_list = []


        stick = pygame.image.load("graphics/Sprites/stick.png").convert_alpha()
        right_gun = pygame.image.load("graphics/Sprites/Gun_right.png").convert_alpha()
        left_gun = pygame.image.load("graphics/Sprites/Gun_left.png").convert_alpha()
        right_bullet = pygame.image.load("graphics/Sprites/bullet_right.png").convert_alpha()
        left_bullet = pygame.image.load("graphics/Sprites/bullet_left.png").convert_alpha()
        right_obstacle = pygame.image.load("graphics/Sprites/obstacle_right.png").convert_alpha()
        left_obstacle = pygame.image.load("graphics/Sprites/obstacle_left.png").convert_alpha()



        #don't put here any conditions
        if self.type == "plat1":
          # construction1
          #stick1
          stick_img1 = pygame.transform.scale(stick, (170, 225))
          stick_rec1 = stick_img1.get_rect(midbottom=(115, -50))
          self.images.append(stick_img1)
          self.rects.append(stick_rec1)
          self.stick_rect_spis.append(stick_rec1)

          #stick2
          stick_img2 = pygame.transform.scale(stick, (170, 150))
          stick_rec2 = stick_img2.get_rect(midbottom=(390,-250 ))
          self.images.append(stick_img2)
          self.rects.append(stick_rec2)
          self.stick_rect_spis.append(stick_rec2)

          #stick3
          stick_img3 = pygame.transform.scale(stick, (170, 150))
          stick_rec3 = stick_img3.get_rect(midbottom=(390, -500))
          self.images.append(stick_img3)
          self.rects.append(stick_rec3)
          self.stick_rect_spis.append(stick_rec3)


          print(1)
        elif self.type == "plat2":
          #stick1
          stick_img1 = pygame.transform.scale(stick, (170, 225))
          stick_rec1 = stick_img1.get_rect(midbottom=(115, -50))
          self.images.append(stick_img1)
          self.rects.append(stick_rec1)
          self.stick_rect_spis.append(stick_rec1)
          #stick2
          stick_img2 = pygame.transform.scale(stick, (170, 150))
          stick_rec2 = stick_img2.get_rect(midbottom=(390, -400))
          self.images.append(stick_img2)
          self.rects.append(stick_rec2)
          self.stick_rect_spis.append(stick_rec2)

          #stick3
          stick_img3 = pygame.transform.scale(stick, (170, 150))
          stick_rec3 = stick_img3.get_rect(midbottom=(390, -650))
          self.images.append(stick_img3)
          self.rects.append(stick_rec3)
          self.stick_rect_spis.append(stick_rec3)

          print(2)
        elif self.type =="plat3":
            #stick1
            stick1 = pygame.transform.scale(stick, (170, 250))
            stick_rec1 = stick1.get_rect(midbottom=(115, -400))
            self.images.append(stick1)
            self.rects.append(stick_rec1)
            self.stick_rect_spis.append(stick_rec1)

            # stick2
            stick2 = pygame.transform.scale(stick, (170, 170))
            stick_rec2 = stick2.get_rect(midbottom=(390, -610))
            self.images.append(stick2)
            self.rects.append(stick_rec2)
            self.stick_rect_spis.append(stick_rec2)

            # stick3
            stick3 = pygame.transform.scale(stick, (170, 140))
            stick_rec3 = stick3.get_rect(midbottom=(390, -180))
            self.images.append(stick3)
            self.rects.append(stick_rec3)
            self.stick_rect_spis.append(stick_rec3)
            print(3)

        elif self.type == "plat4":

            #stick1
            stick1 = pygame.transform.scale(stick, (170, 250))
            stick_rec1 = stick1.get_rect(midbottom=(115, -600))
            self.images.append(stick1)
            self.rects.append(stick_rec1)
            self.stick_rect_spis.append(stick_rec1)

            # stick2
            stick2 = pygame.transform.scale(stick, (170, 170))
            stick_rec2 = stick2.get_rect(midbottom=(390, -450))
            self.images.append(stick2)
            self.rects.append(stick_rec2)
            self.stick_rect_spis.append(stick_rec2)

            # stick3
            stick3 = pygame.transform.scale(stick, (170, 170))
            stick_rec3 = stick3.get_rect(midbottom=(115, -300))
            self.images.append(stick3)
            self.rects.append(stick_rec3)
            self.stick_rect_spis.append(stick_rec3)

            # stick4
            stick4 = pygame.transform.scale(stick, (170, 170))
            stick_rec4 = stick4.get_rect(midbottom=(390, -100))
            self.images.append(stick4)
            self.rects.append(stick_rec4)
            self.stick_rect_spis.append(stick_rec4)
            print(4)


        elif self.type == "plat5":

            # stick1
            stick1 = pygame.transform.scale(stick, (170, 170))
            stick_rec1 = stick1.get_rect(midbottom=(390, -700))
            self.images.append(stick1)
            self.rects.append(stick_rec1)
            self.stick_rect_spis.append(stick_rec1)

            # stick2
            stick2 = pygame.transform.scale(stick, (170, 170))
            stick_rec2 = stick2.get_rect(midbottom=(115, -450))
            self.images.append(stick2)
            self.rects.append(stick_rec2)
            self.stick_rect_spis.append(stick_rec2)

            # stick3
            stick3 = pygame.transform.scale(stick, (170, 170))
            stick_rec3 = stick3.get_rect(midbottom=(390, -250))
            self.images.append(stick3)
            self.rects.append(stick_rec3)
            self.stick_rect_spis.append(stick_rec3)

            # stick4
            stick4 = pygame.transform.scale(stick, (170, 170))
            stick_rec4 = stick4.get_rect(midbottom=(390, -50))
            self.images.append(stick4)
            self.rects.append(stick_rec4)
            self.stick_rect_spis.append(stick_rec4)
            print(5)


        elif self.type == "plat6":

            #stick1
            stick1 = pygame.transform.scale(stick, (170, 170))
            stick_rec1 = stick1.get_rect(midbottom=(265, -700))
            self.images.append(stick1)
            self.rects.append(stick_rec1)
            self.stick_rect_spis.append(stick_rec1)

            #stick2
            stick2 = pygame.transform.scale(stick, (170, 170))
            stick_rec2 = stick2.get_rect(midbottom=(265, -400))
            self.images.append(stick2)
            self.rects.append(stick_rec2)
            self.stick_rect_spis.append(stick_rec2)


            #stick3
            stick3 = pygame.transform.scale(stick, (170, 170))
            stick_rec3 = stick1.get_rect(midbottom=(265, -100))
            self.images.append(stick3)
            self.rects.append(stick_rec3)
            self.stick_rect_spis.append(stick_rec3)

            #other funny things:D

            # right bullet
            img3 = pygame.transform.scale(right_bullet, (170, 170))
            img3_rect = img3.get_rect(midbottom=(-30, -550))
            self.images.append(img3)
            self.rects.append(img3_rect)
            self.img3_rect = img3_rect


            self.bullet1_rect = self.img3_rect.copy()
            self.bullet1_width = 20
            self.bullet1_height = 100
            self.bullet1_y = 50
            self.bullet1_x  = 50
            self.bullet1_rect.width -=self.bullet1_width
            self.bullet1_rect.height -= self.bullet1_height
            self.bullet1_rect.y += self.bullet1_y
            self.bullet1_rect.x = self.bullet1_x
            self.bullets_list.append(self.bullet1_rect)

            # left bullet
            img4 = pygame.transform.scale(left_bullet, (170, 170))
            img4_rect = img4.get_rect(midbottom=(530, -250))
            self.img4_rect = img4_rect
            self.images.append(img4)
            self.rects.append(img4_rect)


            self.bullet2_rect = self.img4_rect.copy()
            self.bullet2_width = 20
            self.bullet2_height = 115
            self.bullet2_y = 65
            self.bullet2_x =100
            self.bullet2_rect.width -= self.bullet2_width
            self.bullet2_rect.height -= self.bullet2_height
            self.bullet2_rect.y += self.bullet2_y
            self.bullet2_rect.x = self.bullet2_x
            self.bullets_list.append(self.bullet2_rect)




            #right gun
            img1 = pygame.transform.scale(right_gun, (170, 170))
            img1_rect = img1.get_rect(midbottom=(0, -550))
            self.images.append(img1)
            self.rects.append(img1_rect)

            #left gun
            img2 = pygame.transform.scale(left_gun, (170, 170))
            img2_rect = img2.get_rect(midbottom=(500, -250))
            self.images.append(img2)
            self.rects.append(img2_rect)


            print(6)

        elif self.type == "plat7":
            stick1 = pygame.transform.scale(stick, (170, 170))
            stick_rec1 = stick1.get_rect(midbottom=(115, -650))
            self.images.append(stick1)
            self.rects.append(stick_rec1)
            self.stick_rect_spis.append(stick_rec1)

            stick2 = pygame.transform.scale(stick, (170, 170))
            stick_rec2 = stick2.get_rect(midbottom=(390, -500))
            self.images.append(stick2)
            self.rects.append(stick_rec2)
            self.stick_rect_spis.append(stick_rec2)

            stick3 = pygame.transform.scale(stick, (170, 250))
            stick_rec3 = stick3.get_rect(midbottom=(115, -250))
            self.images.append(stick3)
            self.rects.append(stick_rec3)
            self.stick_rect_spis.append(stick_rec3)

            stick4 = pygame.transform.scale(stick, (170, 230))
            stick_rec4 = stick4.get_rect(midbottom=(390, -160))
            self.images.append(stick4)
            self.rects.append(stick_rec4)
            self.stick_rect_spis.append(stick_rec4)

            #odstacles
            right_obstacle1 = pygame.transform.scale(right_obstacle,(100,100))
            obstacle_rec1 = right_obstacle1.get_rect(midbottom=(130, -270))
            self.images.append(right_obstacle1)
            self.rects.append(obstacle_rec1)
            self.obstacle_rec1 = obstacle_rec1
            self.thorn1_rect = self.obstacle_rec1.copy()

            self.thorn1_width = 70
            self.thorn1_height = 20
            self.thorn1_y = 10
            self.thorn1_x = 115
            self.thorn1_rect.width -= self.thorn1_width
            self.thorn1_rect.height -= self.thorn1_height
            self.thorn1_rect.y += self.thorn1_y
            self.thorn1_rect.x = self.thorn1_x
            self.thorns_list.append(self.thorn1_rect)

            print(7)
        elif self.type == "plat8":
            stick1 = pygame.transform.scale(stick, (170, 230))
            stick_rec1 = stick1.get_rect(midbottom=(390, -650))
            self.images.append(stick1)
            self.rects.append(stick_rec1)
            self.stick_rect_spis.append(stick_rec1)

            stick2 = pygame.transform.scale(stick, (170, 250))
            stick_rec2 = stick2.get_rect(midbottom=(115, -525))
            self.images.append(stick2)
            self.rects.append(stick_rec2)
            self.stick_rect_spis.append(stick_rec2)

            stick3 = pygame.transform.scale(stick, (170, 250))
            stick_rec3 = stick3.get_rect(midbottom=(115, -300))
            self.images.append(stick3)
            self.rects.append(stick_rec3)
            self.stick_rect_spis.append(stick_rec3)

            stick4 = pygame.transform.scale(stick, (170, 230))
            stick_rec4 = stick4.get_rect(midbottom=(390, -70))
            self.images.append(stick4)
            self.rects.append(stick_rec4)
            self.stick_rect_spis.append(stick_rec4)

            right_obstacle1 = pygame.transform.scale(right_obstacle, (100, 100))
            obstacle_rec2 = right_obstacle1.get_rect(midbottom=(130, -650))
            self.images.append(right_obstacle1)
            self.rects.append(obstacle_rec2)
            self.obstacle_rec2 = obstacle_rec2
            self.thorn2_rect = self.obstacle_rec2.copy()

            self.thorn2_width = 70
            self.thorn2_height = 20
            self.thorn2_y = 10
            self.thorn2_x = 115
            self.thorn2_rect.width -= self.thorn2_width
            self.thorn2_rect.height -= self.thorn2_height
            self.thorn2_rect.y += self.thorn2_y
            self.thorn2_rect.x = self.thorn2_x
            self.thorns_list.append(self.thorn2_rect)



            print(8)
        elif self.type == "plat9":
            stick1 = pygame.transform.scale(stick, (170, 250))
            stick_rec1 = stick1.get_rect(midbottom=(390, -650))
            self.images.append(stick1)
            self.rects.append(stick_rec1)
            self.stick_rect_spis.append(stick_rec1)

            right_obstacle3 = pygame.transform.scale(right_obstacle, (110, 130))
            obstacle_rec3 = right_obstacle3.get_rect(midbottom=(135, -450))
            self.images.append(right_obstacle3)
            self.rects.append(obstacle_rec3)
            self.obstacle_rec3 = obstacle_rec3
            self.thorn3_rect = self.obstacle_rec3.copy()

            self.thorn3_width = 85
            self.thorn3_height = 40
            self.thorn3_y = 20
            self.thorn3_x = 125
            self.thorn3_rect.width -= self.thorn3_width
            self.thorn3_rect.height -= self.thorn3_height
            self.thorn3_rect.y += self.thorn3_y
            self.thorn3_rect.x = self.thorn3_x
            self.thorns_list.append(self.thorn3_rect)


            stick3 = pygame.transform.scale(stick, (170, 270))
            stick_rec3 = stick3.get_rect(midbottom=(115, -290))
            self.images.append(stick3)
            self.rects.append(stick_rec3)
            self.stick_rect_spis.append(stick_rec3)

            stick2 = pygame.transform.scale(stick, (170, 230))
            stick_rec2 = stick2.get_rect(midbottom=(115, -485))
            self.images.append(stick2)
            self.rects.append(stick_rec2)
            self.stick_rect_spis.append(stick_rec2)

            stick4 = pygame.transform.scale(stick, (170, 230))
            stick_rec4 = stick4.get_rect(midbottom=(390, -75))
            self.images.append(stick4)
            self.rects.append(stick_rec4)
            self.stick_rect_spis.append(stick_rec4)


            print(9)
        elif self.type == "plat10":
            stick1 = pygame.transform.scale(stick, (170, 220))
            stick_rec1 = stick1.get_rect(midbottom=(115, -650))
            self.images.append(stick1)
            self.rects.append(stick_rec1)
            self.stick_rect_spis.append(stick_rec1)

            stick3 = pygame.transform.scale(stick, (170, 220))
            stick_rec3 = stick3.get_rect(midbottom=(390, -100))
            self.images.append(stick3)
            self.rects.append(stick_rec3)
            self.stick_rect_spis.append(stick_rec3)
            #obstacles_animationw

            left_obstacle = pygame.transform.scale(left_obstacle, (110, 130))
            obstacle_rec4 = left_obstacle.get_rect(midbottom=(370, -440))
            self.rects.append(obstacle_rec4)
            self.images.append(left_obstacle)

            self.obstacle_rec4 = obstacle_rec4
            self.thorn4_rect = self.obstacle_rec4.copy()

            self.thorn4_width = 90
            self.thorn4_height = 40
            self.thorn4_y = 20
            self.thorn4_x = 45
            self.thorn4_rect.width -= self.thorn4_width
            self.thorn4_rect.height -= self.thorn4_height
            self.thorn4_rect.y += self.thorn4_y
            self.thorn4_rect.x += self.thorn4_x
            self.thorns_list.append(self.thorn4_rect)

            stick2 = pygame.transform.scale(stick, (170, 310))
            stick_rec2 = stick2.get_rect(midbottom=(390, -350))
            self.images.append(stick2)
            self.rects.append(stick_rec2)
            self.stick_rect_spis.append(stick_rec2)


            print(10)
          # Копируем размеры и позицию основного rect
        self.sticks_correct_hibox = self.stick_rect_spis.copy()
        # correct size of sticks
        # for sticks_correct_rect_hitbox in self.sticks_correct_hibox:
        self.hitboks_x_position = 0# Величина, на которую нужно уменьшить хитбокс слева
        self.left_side_hitboks = 150
        self.hitboks_height =40
        self.hitboks_y_pos =0
        for sticks_correct_rect_hitbox in self.sticks_correct_hibox:
         sticks_correct_rect_hitbox.width -= self.left_side_hitboks
         sticks_correct_rect_hitbox.left += self.hitboks_x_position
         sticks_correct_rect_hitbox.height -= self.hitboks_height
         sticks_correct_rect_hitbox.bottom += self.hitboks_y_pos
         #sticks_correct_rect_hitbox.y += self.go_down



    def platforms_moving(self):
        if platforms_go:
           for rect in self.rects:
               rect.y += self.go_down
           if self.type == "plat6":
               self.bullet1_rect.y += self.go_down
               self.bullet2_rect.y += self.go_down
           if self.type == "plat7":
               self.thorn1_rect.y += self.go_down
           if self.type == "plat8":
               self.thorn2_rect.y += self.go_down
           if self.type == "plat9":
               self.thorn3_rect.y += self.go_down
           if self.type == "plat10":
               self.thorn4_rect.y += self.go_down
           #This function make a shoot
           if self.type == "plat6":
               self.img3_rect.x += self.bullets_speed
               self.img4_rect.x -= self.bullets_speed
               self.bullet1_rect.x += self.bullets_speed
               self.bullet2_rect.x -= self.bullets_speed
               if self.img3_rect.left >= 550 or self.bullet1_rect.left>= 550:
                   self.img3_rect.x = -120
                   self.bullet1_rect.x = -120
               if self.img4_rect.right <= -30 or self.bullet2_rect.right<=-30:
                   self.img4_rect.x = 550
                   self.bullet2_rect.x = 550

    def draw_platforms(self):
       for image,rect in zip(self.images,self.rects):
         screen.blit(image,(rect))
       for correct_rect in self.sticks_correct_hibox :
          pygame.draw.rect(screen, (255, 0, 0), correct_rect, 2)
       for rect in self.bullets_list:
          pygame.draw.rect(screen, (255, 0, 0), rect, 2)
       for rect in self.thorns_list:
        pygame.draw.rect(screen, (255, 0, 0), rect, 2)

    def deleting_dynamic_platforms(self):
        if self.rects: # Check if the list of rectangles is not empty
          highest_position = min(r.top for r in self.rects )
          if highest_position >= 750: # I can put if after other cycle and then I won't get an error
            self.kill()
    def return_on_top(self):
        if not self.rects: # I cant use here True/False because its a list
          return -1000 # Return a very high number if there are no rects
        return  max(r.bottom for r in self.rects)

    def update(self):
        self.draw_platforms()
        self.platforms_moving()
        self.return_on_top()
        self.deleting_dynamic_platforms()

class First_platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/Sprites/platform_wood.png").convert_alpha()
        self.platform_norm = pygame.transform.scale(self.image, (250, 400))
        self.rect = self.platform_norm.get_rect(midtop=(313, 615 ))
    def update(self):
        if platforms_go: #and game_state == True:
          self.rect.y += 2
        if self.rect.y >= 750:
             self.rect.y += 0


def player_platforms_collision():
    for platforms in dynamic_platforms:  # ВСЕГДА ПИСАТЬ ЭТУ ХЕРНЮ ИЛИ БУДЕТ БО-БО!
        for rect in platforms.stick_rect_spis:
            if player1.sprite.monkey_hitbox.colliderect(rect):
                global player_main_collision_state
                player_main_collision_state = True
                player1.sprite.player_state = "default"
                print("Collide")
            #else:
                #player_main_collision_state = False

    for platforms in null_platform:  # ВСЕГДА ПИСАТЬ ЭТУ ХЕРНЮ ИЛИ БУДЕТ ПЛОХО!
            for rect in platforms.hitboks_first :
                if player1.sprite.monkey_hitbox.colliderect(rect):
                    player_main_collision_state = True
                    player1.sprite.player_state = "default"
                    print("Collide")
            # else:
                # player_main_collision_state = False


                #print("First_Collide")
            #elif not player_collision_test :
                #player_main_collision_state = False
            #elif player_state == "jump" and keys[pygame.K_w]:
                #player_main_collision_state = "None"

def collide_with_bullets_or_thorns():
    if player1.sprite.monkey_hitbox.top >= 770 :
        dynamic_platforms.empty()

        return False
    for platforms in dynamic_platforms:
        for rect in platforms.bullets_list:
           if player1.sprite.monkey_hitbox.colliderect(rect):
              dynamic_platforms.empty()
              return False

    for platforms in dynamic_platforms:
        for rect in platforms.thorns_list:
            if player1.sprite.monkey_hitbox.colliderect(rect):
               dynamic_platforms.empty()
               return False

    else:return True
def display_score():
    #if score_displaying:
     current_time = int(pygame.time.get_ticks()//1000) - start_time
     timer_font = game_over_message_font.render(f"{current_time}", True, (255, 226, 140))
     timer_rect = timer_font.get_rect(center=(50, 50))
     screen.blit(timer_font,(timer_rect))
     return current_time


pygame.init()

screen = pygame.display.set_mode((500,750))
icon = pygame.image.load("ikon.jpg").convert_alpha()
pygame.display.set_caption("Monkey Ricochet")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
player_gravity1 = 0
player_gravity2 = 0
player_gravity3 = 0
keys = pygame.key.get_pressed()
game_state = True
platforms_go = False
timer_stage = 'None'
start_time = 0
score = 0
score_displaying = False
first_move = "None"
player_main_collision_state = False
first_platform_state = "collide"
platform_gravity =0
platform_true_rect = pygame.Rect(195,680,100,15)
pygame.draw.rect(screen, (255, 0, 0), platform_true_rect, 2)
jump_state = True
mouse_pos = pygame.mouse.get_pos()



stage = 0

#timer_state = "None"

player1= pygame.sprite.GroupSingle()
player1.add(Player())

dynamic_platforms = pygame.sprite.Group()


null_platform = pygame.sprite.GroupSingle()
null_platform.add(Null_Stick())


starting_platform = pygame.sprite.GroupSingle()
starting_platform.add(First_platform())


double =0
#test_surface = pygame.Surface((500,800))
#test_surface.fill("Brown2")
jungle_surface = pygame.image.load("graphics/Sprites/main_surface.png").convert_alpha()
norm_jungle = pygame.transform.scale(jungle_surface,(500,750))
jungle_rect = norm_jungle.get_rect(midtop = (250,0))

game_over_screen = pygame.image.load("graphics/Sprites/Game_over_screen.jpg").convert_alpha()
scaled_game_over_screen = pygame.transform.scale(game_over_screen,(500,750))
game_over_rect = scaled_game_over_screen.get_rect(midtop = (250,0))

game_over_font = pygame.font.Font("font/VT323-Regular.ttf",35)
font_surface = game_over_font.render("Press Space or Button to restart",True,(255, 226, 140))
font_rect = font_surface.get_rect(center =(250,710))

tip_surface = game_over_font.render("Press W to start",True,(255,226,140))
tip_rect = tip_surface.get_rect(center =(257,460))

messages_credits_font = pygame.font.Font("font/MotionPicture_PersonalUseOnly.ttf",35)

thanks_surface = messages_credits_font.render("Thanks for motivation and help!",True,(255, 226, 140))
thanks_rect = thanks_surface.get_rect(center =(180,120))

blog_surface = messages_credits_font.render("My blog",True,(255, 226, 140))
blog_rect = blog_surface.get_rect(center =(85,250))


#total score
game_over_message_font = pygame.font.Font("font/VT323-Regular.ttf",55)

credits_and_quit_font = pygame.font.Font("font/MotionPicture_PersonalUseOnly.ttf",60)
credits_surface = credits_and_quit_font.render("Credits",True,(255, 226, 140))
credits_rect = credits_surface.get_rect(center =(259,550))

quit_surface = credits_and_quit_font.render("Quit",True,(255, 226, 140))
quit_rect = quit_surface.get_rect(center =(259,650))

font_gravity = 0

restart_button = pygame.image.load("graphics/restart button.png").convert_alpha()
restart_scaled_button = pygame.transform.scale(restart_button,(130,130))
restart_button_rect =restart_scaled_button.get_rect(midbottom =( 250,700))

logo = pygame.image.load("graphics/menu logo.png").convert_alpha()
scaled_logo = pygame.transform.scale(logo,(300,300))
logo_rect =scaled_logo.get_rect(midbottom =(250,250))
#menu buttons
play_button = pygame.Rect(320, 415, 160, 70)
credits_button = pygame.Rect(180, 515, 160, 70)
exit_button = pygame.Rect(180, 615, 160, 70)
play_button_state = False
credits_button_state = False
exit_button_state = False

close_button = pygame.image.load("graphics/Sprites/exit button.png").convert_alpha()
close_scaled_button = pygame.transform.scale(close_button,(40,40))
close_button_rect =restart_scaled_button.get_rect(midbottom =( 496,225))

misha = pygame.image.load("graphics/Sprites/blog_icons/misha.png").convert_alpha()
scaled_misha_icon= pygame.transform.scale(misha,(95,95))
misha_icon_rect = scaled_misha_icon.get_rect(midbottom=(100,231))

shenya = pygame.image.load("graphics/Sprites/blog_icons/shenya.png").convert_alpha()
scaled_shenya_icon= pygame.transform.scale(shenya,(95,95))
shenya_icon_rect = scaled_shenya_icon.get_rect(midbottom=(250,231))

kolya = pygame.image.load("graphics/Sprites/blog_icons/kolya.png").convert_alpha()
scaled_kolya_icon= pygame.transform.scale(kolya,(95,95))
kolya_icon_rect = scaled_kolya_icon.get_rect(midbottom=(250,365))

roma_icon = pygame.image.load("graphics/Sprites/blog_icons/roma.png").convert_alpha()
scaled_icon_roma= pygame.transform.scale(roma_icon,(95,95))
roma_icon_rect = scaled_icon_roma.get_rect(midbottom=(400,231))

obstacle_timer = pygame.USEREVENT + 1 # +1 для того что бы оно не конфронтавало с встроенными мех pygame
pygame.time.set_timer(obstacle_timer,3000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w and jump_state ==True: #or play_button_state == "play":
                platform_gravity = 5
                #player_gravity1 = -20
                platforms_go = True
                score_displaying = True
                start_time = pygame.time.get_ticks() // 1000
                jump_state = False
                credits_button_state = False


        mouse_pos = pygame.mouse.get_pos()
        if game_state:
          can_spawn_dynamic_platforms = False
          if player1.sprite.monkey_hitbox.colliderect(platform_true_rect):
             first_platform_state = "collide"
          else:
             first_platform_state = "None"

          if credits_button.collidepoint(mouse_pos):
              if event.type == pygame.MOUSEBUTTONUP:
                  credits_button_state= True
          elif close_button_rect.collidepoint(mouse_pos):
              if event.type == pygame.MOUSEBUTTONUP:
                  credits_button_state = False
          elif exit_button.collidepoint(mouse_pos):
              if event.type == pygame.MOUSEBUTTONUP:
                  pygame.quit()
                  exit()
          elif misha_icon_rect.collidepoint(mouse_pos):
              if credits_button_state:
                  if event.type == pygame.MOUSEBUTTONUP:
                      webbrowser.open("https://t.me/davilkus_games_news")
          elif shenya_icon_rect.collidepoint(mouse_pos):
              if credits_button_state:
                  if event.type == pygame.MOUSEBUTTONUP:
                      webbrowser.open("https://t.me/omega_gamedev")
          elif kolya_icon_rect.collidepoint(mouse_pos):
              if credits_button_state:
                  if event.type == pygame.MOUSEBUTTONUP:
                      webbrowser.open("https://t.me/tutols_industries")
          elif roma_icon_rect.collidepoint(mouse_pos):
              if credits_button_state:
                  if event.type == pygame.MOUSEBUTTONUP:
                      webbrowser.open("https://t.me/ROMA_PLAY123")
          if platform_true_rect.bottom >= 800:
            first_platform_state ="None"
          if len(dynamic_platforms)==0:
            can_spawn_dynamic_platforms =True
          else:
            last_platform = dynamic_platforms.sprites()[-1]
            if last_platform.return_on_top() > 0:
                can_spawn_dynamic_platforms = True
          if platforms_go and timer_stage == 'start':
             if not dynamic_platforms:
              dynamic_platforms.add(Platforms(choice(["plat1","plat2","plat3","plat4","plat5","plat6","plat7","plat8","plat9","plat10"])))
             else:
                last_platform = dynamic_platforms.sprites()[-1]
                highest_point = min(r.top for r in last_platform.rects)
                Spacing = -150
                if highest_point > Spacing:
                  dynamic_platforms.add(Platforms(choice(["plat1","plat2","plat3","plat4","plat5","plat6","plat7","plat8","plat9","plat10"])))
        else:
         #print("You are dead")
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or restart_button_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP:
              #game_state = True
              player1.sprite.rect.bottom = 680
              player1.sprite.monkey_hitbox.bottom = 680
              player1.sprite.rect.x = 195
              player1.sprite.monkey_hitbox.x = 200
              player1.sprite.player_gravity1 = 0
              player1.sprite.player_gravity2 = 0
              player1.sprite.player_state = "default"
              player_main_collision_state = False


              starting_platform.sprite.rect.y = 616


              null_platform.sprite.stick_rec1_1.y =140
              null_platform.sprite.stick1_hitbox.y = 170

              null_platform.sprite.stick_rec1_2.y = 430
              null_platform.sprite.stick2_hitbox.y = 460

              null_platform.sprite.stick_rec1_3.y = -10
              null_platform.sprite.stick3_hitbox.y = 20

              null_platform.sprite.stick_rec1_4.y = -310
              null_platform.sprite.stick4_hitbox.y = -293
              platforms_go = False
              game_state = True
              #if score_displaying == True:
                #start_time = int(pygame.time.get_ticks()) // 1000


    #screen.blit(platform_norm,(platform_rec))
    #font = pygame.font.SysFont(None, 36)
    #cooldown_left = max(0, cooldown_time - (pygame.time.get_ticks() - last_jump_time))
    #text = font.render(f"Cooldown: {cooldown_left / 1000:.1f} seconds", True, "BLACK")
    #screen.blit(text, (10, 10)
    if game_state:
     platform_true_rect.y += platform_gravity
     screen.blit(norm_jungle,(jungle_rect))
     pygame.draw.rect(screen, (255, 0, 0), platform_true_rect, 2)



     player_platforms_collision()
     player1.draw(screen)
     player1.update()
     null_platform.update()
     dynamic_platforms.update()
     starting_platform.update()
     starting_platform.draw(screen)
     game_state = collide_with_bullets_or_thorns()
     if platforms_go:
       score = display_score()
     if jump_state:
         screen.blit(scaled_logo,(logo_rect))
         menu = pygame.Rect(150, 500, 220, 200)
         pygame.draw.rect(screen,"#82461E" ,menu,0,5)
         screen.blit(tip_surface,(tip_rect))

         pygame.draw.rect(screen, (156, 88, 41), credits_button, 0, 5)

         pygame.draw.rect(screen, (156, 88, 41), exit_button, 0, 5)
         screen.blit(credits_surface,(credits_rect))
         screen.blit(quit_surface,quit_rect)

         if credits_button_state == True:
             special_thanks = pygame.Rect(30, 100, 440, 280)
             pygame.draw.rect(screen, "#82461E", special_thanks, 0, 5)
             screen.blit(close_scaled_button,(close_button_rect))
             screen.blit(thanks_surface,thanks_rect)
             screen.blit(blog_surface,blog_rect)
             screen.blit(scaled_misha_icon,misha_icon_rect)
             screen.blit(scaled_shenya_icon, shenya_icon_rect)
             screen.blit(scaled_icon_roma, roma_icon_rect)
             screen.blit(scaled_kolya_icon,kolya_icon_rect)


    else:
        jump_state = True
        print("Gaben_huilo_ksta:D")

        if keys[pygame.K_SPACE]:
         player1.draw(screen)
         player1.update()
        starting_platform.draw(screen)
        starting_platform.update()
        #null_platform.draw(screen)
        #null_platform.update()
        screen.blit(scaled_game_over_screen, (game_over_rect))
        screen.blit(font_surface,(font_rect))
        screen.blit(restart_scaled_button,restart_button_rect)



    pygame.display.update()
    clock.tick(60)