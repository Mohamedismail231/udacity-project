def script():
    # imports that are real important

    import time as tm
    import datetime as dtm
    import random as rnd
    import sys

    # vars for the start of game
    pressed1 = False

    pressed2 = False

    pressed3 = False

    pressed4 = False

    pressed5 = False

    s = tm.time()

    score = 0
    hp = 100
    joehp = 400
    hunger = 100
    enemyhp = 50  # it will be modified for every enemy
    elaptime = 0
    inventory = {"sandwich": 1}
    weapon = {}
    broomdict = {"broom": 1}
    bowdict = {"bow": 1}
    sworddict = {"sword": 1}
    broomdamage = [5, 10, 15, 20]
    bowdamage = [10, 13, 18, 25]
    sworddamage = [90, 100, 200, 300]
    joedamage = [50, 60, 65, 100]
    joeturn_choose = ["attack", "defend"]
    mothdamage = [10, 13, 14, 18]

    achoodamage = [20, 24, 26, 35]

    theblugoprodamage = [90, 150, 200, 250]

    enemyattackchoose = ["you", "joe"]

    # defs to make the coding much easier

    def print_l(script):
        for letter in script:
            print(letter, end='', flush=True)
            tm.sleep(0.04)

        tm.sleep(1)

    def retryask(tm):
        print_l(
            f"you lose your score is {score} and you finished"
            + f"this ending in {tm}\n")

        m = input("do you want to retry? Y/N\n")
        while not pressed1:
            if m == "Y" or m == "y":
                script()

            elif m == "N" or m == "n":
                sys.exit(1)

    def retrytime_record():
        et = tm.time()

        el = et - s

        d = dtm.timedelta(seconds=el)

        dstr = str(d)

        retryask(dstr)

    yourturn = 1

    joeturn = 0

    enemyturn = 0

    def FIGHTMODE(hitthing, enemy):
        global yourturn

        global joeturn

        global enemyturn

        global hp

        global joehp

        global enemyhp

        while (hp > 0 or joehp > 0) and enemyhp > 0:
            broom_crit_chance = rnd.choices(
                population=broomdamage, weights=[40, 30, 20, 6])

            bow_crit_chance = rnd.choices(
                population=bowdamage, weights=[40, 30, 20, 6])[0]

            sword_crit_chance = rnd.choices(
                population=sworddamage, weights=[40, 40, 50, 30]
            )[0]

            moth_crit_chance = rnd.choices(population=mothdamage, weights=[40,
                                                                           30,
                                                                           20,
                                                                           6])
            [0]

            achoo_crit_damage = rnd.choices(
                population=achoodamage, weights=[40, 30, 20, 6]
            )[0]

            gopro_crit_damage = rnd.choices(
                population=theblugoprodamage, weights=[40, 30, 20, 6]
            )[0]

            joes_crit_chance = rnd.choices(population=joedamage, weights=[50,
                                                                          40,
                                                                          40,
                                                                          10])
            [0]

            joes_choose_chance = rnd.choices(
                population=joeturn_choose, weights=[40, 60])[0]

            enemychoose_chance = rnd.choices(
                population=enemyattackchoose, weights=[50, 50]
            )[0]

            print(f"{hp}= {joehp}= {enemyhp}=")

            if yourturn == 1:
                decide = input(
                    "ITS YOUR TURN YOU CAN EITHER A)ATTACK OR"
                    + f"B)DEFEND(increases hp)"
                )

                if decide == "A" or decide == "a":
                    if hitthing == "broom":
                        print(f"YOU ATTACK ENEMY -{broom_crit_chance}")

                        enemyhp -= broom_crit_chance[0]

                        print(f"ENEMY HP:{enemyhp}")

                        yourturn -= 1

                        joeturn += 1

                    elif hitthing == "bow":
                        print(f"YOU ATTACK ENEMY -{bow_crit_chance}")

                        enemyhp -= bow_crit_chance

                        print(f"ENEMY HP:{enemyhp}")

                        yourturn -= 1

                        joeturn += 1

                    elif hitthing == "sword":
                        print(f"YOU ATTACK ENEMY -{sword_crit_chance}")

                        enemyhp -= sword_crit_chance

                        print(f"ENEMY HP:{enemyhp}")

                        yourturn -= 1

                        joeturn += 1

                if decide == "b" or decide == "B":
                    hp += 10

                    yourturn -= 1

                    joeturn += 1

            elif joeturn == 1:
                print("ITS JOE'S TURN")

                print(f"JOE CHOOSES to{joes_choose_chance}")

                if joes_choose_chance == "attack":
                    print(f"JOE ATTACKS -{joes_crit_chance}")

                    enemyhp -= joes_crit_chance

                    joeturn -= 1

                    enemyturn += 1

                elif joes_choose_chance == "defend":
                    print(f"JOE DEFENDS")

                    joehp += 10

                    joeturn -= 1

                    enemyturn += 1

            elif enemyturn == 1:
                if enemy == "moth" and enemychoose_chance == "you":
                    print(f"THE ENEMY ATTACKS YOU -{moth_crit_chance} ")

                    hp -= moth_crit_chance

                    print(f"YOUR HP NOW IS {hp}")

                elif enemy == "moth" and enemychoose_chance == "joe":
                    print(f"THE ENEMY ATTACKS JOE -{moth_crit_chance}")

                    joehp -= moth_crit_chance

                    print(f"JOES HP NOW IS {joehp}")

                elif enemy == "achoo" and enemychoose_chance == "you":
                    print(f"THE ENEMY ATTACKS YOU -{achoo_crit_damage}")

                    hp -= achoo_crit_damage

                    print(f"YOUR HP NOW IS {hp}")

                elif enemy == "achoo" and enemychoose_chance == "joe":
                    print(f"THE ENEMY ATTACKS JOE -{achoo_crit_damage}")

                    joehp -= achoo_crit_damage

                    print(f"JOES HP IS NOW {joehp}")

                elif enemy == "gopro" and enemychoose_chance == "you":
                    print(f"THE ENEMY ATTACKS YOU -{gopro_crit_damage}")

                    print(f"YOUR HP NOW IS {hp}")

                    hp -= gopro_crit_damage

                elif enemy == "gopro" and enemychoose_chance == "joe":
                    print(f"THE ENEMY ATTACKS JOE -{gopro_crit_damage}")

                    joehp -= gopro_crit_damage

                    print(f"JOES HP IS NOW {joehp}")

                enemyturn -= 1

                yourturn += 1

        if hp <= 0 and joehp <= 0:
            retrytime_record()

        elif enemyhp <= 0:
            print("YOU WIN")

    # now to the start of the game

    print_l("you are in the middle of a forest with some friends(paid actors)"
            + "\n")

    print_l("you make a camp and then you play a game of truth or dare\n")

    print_l("you get dared to sleep in the cave 2 miles away from the camp\n")

    print_l(
        "if you didnt accept the dare, you'll pay for whatever they want for" +
        " the next month\n"
    )

    print_l("so you go with 2 sandwiches\n")

    print_l("you enter the cave\n")

    print_l("you trip into a hole....")

    print_l("a big one\n")

    print_l("long ago two races ruled the world: monsters and humans-")

    print_l("oh sorry wrong game\n")

    hunger -= 40

    hp -= 30

    score += 5

    print_l("you wake up and you're hurt and hungry\n")

    while not pressed2:
        q = input("So, would you eat a sandwich? (Y/N)\n")

        if q.lower() == "y":
            pressed2 = True
            print_l("You eat the sandwich\n")
            hp = 100
            hunger = 100
            score += 10
            inventory["sandwich"] -= 1
            print_l("Refreshing...")
            print_l("You continue your way\n")
            print_l("You feel a strange aura\n")
            print_l("You see a shadow of something human-like\n")

            while not pressed3:
                w = input("Would you A) scream or B) look for a weapon\n")

                if w.lower() == "a":
                    pressed3 = True
                    print_l("You scream\n")
                    score += 5
                    print_l("The monster gets afraid and instantly kills you\n"
                            )
                    retrytime_record()

                elif w.lower() == "b":
                    pressed3 = True
                    print_l("You look for a weapon\n")
                    print_l("You find a broom\n")
                    score += 10
                    weapon.update(broomdict)
                    print_l("You grab the broom and ready yourself for a fight"
                            + "\n")
                    print_l("The monster sees you and understands your fear\n")
                    print_l(
                        "The monster gets out of the shadow and reveals itself"
                        + " as Joe\n")
                    print_l("Joe tells you not to say that stupid joke\n")
                    e = input("So, would you say it or not? (Y/N)\n")

                    while not pressed4:
                        if e.lower() == "y":
                            pressed4 = True
                            print_l(
                                "Joe gets angry and he will not leave you till"
                                + " you die\n")
                            print_l("FIGHTMODE ENGAGED\n")
                            print_l("Joe attacks your HP - 400\n")
                            retrytime_record()

                        elif e.lower() == "n":
                            pressed4 = True
                            print_l(
                                "Joe is happy to meet you and now he joins the"
                                + " party\n")
                            print_l("You continue your way to find the exit\n")
                            print_l("A bodybuilder-sized moth approaches\n")
                            FIGHTMODE("broom", "moth")
                            score += 20
                            hp = 100
                            enemyhp = 400
                            joehp = 400
                            print_l("That was easy\n")
                            print_l("You continue your way\n")

                            while not pressed5:
                                r = input(
                                    "You find a bow. Would you take it? (Y/N)"
                                    + "\n")

                                if r.lower() == "y":
                                    pressed5 = True
                                    del weapon[broomdict]
                                    weapon.update(bowdict)
                                    print_l("You get the bow")
                                    score += 30
                                    print_l(
                                        "Your attack increases and your "
                                        + "defense increases by the magic of "
                                        + "'take this you lucky guy'\n")
                                    hp = 200
                                    print_l(
                                        "You continue and find a yellow rat "
                                        + "called Achoo from Pokeyman\n")
                                    FIGHTMODE("bow", "achoo")
                                    enemyhp = 1000
                                    score += 30
                                    print_l(
                                        "Ah, finally we finished this long"
                                        + " battle. Also, why did Joe defend"
                                        + "so much?\n")
                                    print_l(
                                        "You continue and find a glowing cave"
                                        + "\n")
                                    print_l("You and Joe get inside\n")
                                    print_l(
                                        "OH MY GOD, IT'S THE SWORD FROM DOOM."
                                        + "IT'S SO OP, BRO\n")
                                    del weapon[bowdict]
                                    weapon.update(sworddict)
                                    print_l(
                                        "Joe is very happy and he tells you to"
                                        + " take it\n")
                                    print_l(
                                        "Attack increases and defense "
                                        + "increases\n")
                                    hp = 500
                                    score += 50
                                    print_l(
                                        "You and Joe continue till you find "
                                        + "the final exit from this creepy"
                                        + " cave\n")
                                    print_l("You approach it...")
                                    print("Slow...\n")
                                    tm.sleep(4)
                                    print_l(
                                        "And steady while making yourself "
                                        + "ready for an upcoming fight\n")
                                    print_l("You feel it in your guts\n")
                                    print_l("You're 4ft away from the door\n")
                                    print_l(
                                        "THE BLUE GOPRO FROM ULTRAKILL LANDS"
                                        + " IN FRONT OF YOU\n")
                                    FIGHTMODE("sword", "gopro")
                                    score += 100
                                    print_l("YEEEES LES GOOOOO\n")
                                    print_l("You and Joe get out\n")
                                    print_l(
                                        "Joe disguises as a human and you "
                                        + "become friends with him till "
                                        + "eternity\n")
                                    et = tm.time()
                                    el = et - s
                                    d = tm.timedelta(seconds=el)
                                    dstr = str(d)
                                    print(
                                        F"YOU WIN! YOUR SCORE IS {score} AND"
                                        + f"YOU FINISHED IN {dstr}")
                                    sys.exit(1)

                                elif r.lower() == "n":
                                    print_l("You don't take the bow")
                                    print_l(
                                        "G-man: Prepare for unforeseen "
                                        + "consequences")
                                    print_l(
                                        "Gordon Freeman jumps out of a portal "
                                        + "and yeets you with his portal gun")
                                    retrytime_record()

                                else:
                                    pressed5 = False

                        else:
                            pressed4 = False

                else:
                    pressed3 = False

        elif q.lower() == "n":
            pressed2 = True
            print_l("You don't eat the sandwich")
            print_l("You feel so hurt that you can't even move")
            print_l("A big rock falls on you and crushes you")
            print_l("You're now her crush, lol")
            retrytime_record()

        else:
            pressed2 = False


script()
