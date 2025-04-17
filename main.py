from parkour_functies import *
from common import *
import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
WIDTH, HEIGHT = pygame.display.get_window_size()
running = True
state = "Menu"
logo = pygame.image.load('resources/textures/logo.png')
pygame.display.set_caption("Titanic escape")
pygame.display.set_icon(logo)
mainFont = 'resources/MinecraftTen-VGORe.ttf'
punch = move("punch", "Hits the opponent \n for 10 damage", pygame.image.load('resources/textures/move_punch.png'))
comboPunch = move("combo punch", "Hits the opponent a \n random number of times", pygame.image.load('resources/textures/move_comboPunch.png'))
enrage = move("enrage", "Increases your damage on \n the next 3 turns", pygame.image.load('resources/textures/move_enrage.png'))
poison = move("poison", "Poisons your opponent to \n take damage over time", pygame.image.load('resources/textures/move_poison.png'))
lifeSteal = move("life steal", "Damages your opponent \n and gives a percentage \n back as health", pygame.image.load('resources/textures/move_lifeSteal.png'))
block = move("block", "Can block your opponents' \n next few attacks", pygame.image.load('resources/textures/move_block.png'))
devTestInstakill = move("devtest instakill", "for developer purposes only", '')
playerName = "bob"

while running:
    if state == "Menu":
        screen.fill('black')
        game_manager.Reset()
        if playerName != "bob":
            playerName = player.name
        player = character(playerName, 5,
                           pygame.transform.scale(pygame.image.load('resources/textures/rat_idle.png'), (200, 80)), 100,
                           100, [punch, comboPunch], [
                               item("Full Restore", 2),
                               item("Bomb", 3),
                               item("Poison bottle", 2),
                               item("Immunizing elixir", 2),
                               item("Giantkiller", 2),
                               item("Orb of absorption", 1)
                           ], 3, True, False)
        for i in range(len(enemyList)):
            if not(enemyList[i] in platforms):
                enemyList[i].Type.alive = True
                platforms.append(enemyList[i])
        state, player.name = menu(player.name)
        playerName = player.name

    # Hoofd code:
    elif state == "Playing":
        state = parkour(player, game_manager)
        if type(state) == character:
            encounter = state
            result, player.hitpoints, player.items = fight(encounter, player, screen)
            if result == "loss":
                player.lives, state, dead = game_over(player.lives)
                player.hitpoints = player.maxHitpoints
                if state is None:
                    state = "Playing"
                if dead:
                    state = "dead"
            elif result == "win":
                encounter.alive = False
                allMovesList = [punch, comboPunch, enrage, poison, lifeSteal, block]
                if encounter.NewMove == True:
                    newMove = chooseNewAttack(allMovesList, player)
                    if newMove is not None:
                        if newMove != "Menu":
                            player.moveset.append(newMove)
                            state = "Playing"
                        else:
                            state = newMove
                    else:
                        state = "Playing"
                else:
                    state = "Playing"
            else:
                state = result
            playerObject.xpos += 120

    elif state == "quit":
        running = False

    elif state == "dead":
        state = "Playing"
        game_manager.Reset()
        player.moveset = [punch, comboPunch]
        player.items = [
            item("Full Restore", 2),
            item("Bomb", 5),
            item("Poison bottle", 2),
            item("Immunizing elixir", 3),
            item("Giantkiller", 4),
            item("Orb of absorption", 2)
        ]
        for i in range(len(enemyList)):
            if not (enemyList[i] in platforms):
                enemyList[i].Type.alive = True
                platforms.append(enemyList[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()