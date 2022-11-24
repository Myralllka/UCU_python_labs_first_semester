import curses
import random
import DeMyHoriy_playing_fields
import time
import DeMyHoriy_get_and_search_numbers


def init_screen(border):
    """
    (None)-> None
    initialize first screen with borders
    """
    if border == 1:
        my_screen.border(0)


class CV:
    field = 0
    playing_field = eval("DeMyHoriy_playing_fields.field" + str(field))
    professor = [20, 10, "♔"]
    character = [9, 2, "🕴 "]
    wall = "■"
    score = [0, 0, 0]
    level = 0
    dialogs = 3
    numbers_count = 0
    difficulty = 15
    checker = True
    numbers_on_field = False


class PrintOnScreen:
    """
    Class of printing on screen functions
    make_playing_field
    print_information
    print_character
    print_professor_dialog
    professors_dialog
    print_pair_number
    print_happy_number
    print_ulam_number
    bruteforce
    clear_playing_field
    """

    @staticmethod
    def clear_playing_field():
        """
        (None) -> None

        clear your playing field
        """
        for i in range(len(CV.playing_field)):
            for j in range(len(CV.playing_field[i])):
                if str(CV.playing_field[i][j]).isdigit():
                    CV.playing_field[i][j] = "."
                    CV.playing_field[i][j + 1] = ' '

    @staticmethod
    def make_playing_field():
        """
        (None) -> None

        Print playing field on the screen
        """
        my_screen.erase()
        for i in range(len(CV.playing_field)):
            for j in range(len(CV.playing_field[0])):
                my_screen.addstr(i, j, str(CV.playing_field[i][j]))
        my_screen.refresh()

    @staticmethod
    def print_character():
        """
        (None) -> None

        Print character on the screen
        """
        my_screen.addstr(CV.character[0], CV.character[1], CV.character[2])
        my_screen.refresh()

    @staticmethod
    def print_information():
        """
        (None) -> None

        Print score and level on the screen
        """
        my_screen.addstr(2, 46, "Level:")
        my_screen.addstr(2, 53, str(CV.level))
        my_screen.addstr(3, 46, "Score:")
        my_screen.addstr(3, 53, "even |")
        my_screen.addstr(3, 60, "happy |")
        my_screen.addstr(3, 68, "Ulam")
        my_screen.addstr(4, 54, str(CV.score[0]))
        my_screen.addstr(4, 62, str(CV.score[1]))
        my_screen.addstr(4, 70, str(CV.score[2]))

    def print_professor_dialog(self, x=3, y=2):
        """
        (string, int, int) -> void

        Print dialog windows with professor
        """
        dialogs = {
            "1": "press 'e' to speak with Professor...",
            "2": "                                    ",
            "3":
            "PROFESSOR:*Sitting in his chair reading The Histories of Herodotous*\n\
             Uhh, another stranger... What is your name kid ? \n\
        NUB: My name is Nub \n"
            "  PROFESSOR: Noob ? Hahahahaa, such an irony...\n\
        NUB: It's nUb...\n\
  PROFESSOR: Isn't it the same? Haha, anyway, my name is Professor.\n\
             But you'd better call me 'Your Grace' or 'Sir' or 'Sensei'...\n\
        NUB: OK, Professor !\n\
  PROFESSOR: *sighed* *facepalm* I guess that you should have been named \
nOOb \n\
        NUB: But I'm \n\
  PROFESSOR: *pokerface*  Welcome to the NumberField. To complete the game \n\
             have to collect specific numbers. I will support you through\n\
             the game, unwillingly, and give you the needed information. \n\
             There are 4 levels, on each you have different tasks. \n\
             First level is about even numbers. Good luck... \n\
        NUB: But what numbers are even?\n\
  PROFESSOR: Are you from Lviv Polytechnic or what? \n\
        NUB: Yes, so, explain me, Your Grace. \n\
  PROFESSOR: EVEN NUMBERS ARE INTEGERS THAT CAN BE DIVIDED EXACTLY BY 2.\n\
             Now go and bring some evens, son! Haha, joking.\n\
             Hope you will not come back.",
            "4": "PROFESSOR:You made it! I'm impressed. \n\
             I thought you would stuck on the first level... \n\
             Anyway you are here. Congratulations. \n\
             Next level is about happy numbers.\n\
             Go and make happy numbers unhappy!...\n\
        NUB: What numbers ?  \n\
  PROFESSOR: Sorry, I forgot that you are from Polytechnic.\n\
             A HAPPY NUMBER is defined by the following process:\n\
             Starting with any positive integer, replace the number\n\
             by the sum of the squares of its digits in base-ten,\n\
             and repeat the process until the number either equals 1\n\
             or it loops endlessly in a cycle that does not include 1.\n\
             Those numbers for which this process ends in 1 are happy numbers\n\
             Understood?\n\
        NUB: Not really.\n\
  PROFESSOR: I am not surprised due to your alma mater... GO!",
            "5": "PROFESSOR:Can't believe you are here... Ulam numbers, good luck.\n\
        NUB: Excuse me, Sensei, but what is...\n\
  PROFESSOR: Let me guess: you don't know what number is and Ulam number? \n\
        NUB: No, I don't...\n\
  PROFESSOR: *facepalm* Ok, Ulam number is a member of Ulam sequence.*smiling* \n\
        NUB: What is Ul...\n\
  PROFESSOR: The standard Ulam sequence (the (1, 2)–Ulam sequence)\n\
             starts with U1 = 1 and U2 = 2. Then for n > 2, Un is defined\n\
             to be the smallest integer that is the sum of two distinct\n\
             earlier terms in exactly one way. Good luck, my dear Noob.",
            "6": "      NUB: Ulam numbers are now Nub numbers, Sir!\n\
  PROFESSOR: *facepalm* Are you idiot kid?\n\
        NUB: Excuse me, Your Grace...\n\
  PROFESSOR: *sigh*...\n\
        NUB: Thank you a lot, Sensei. I really do appreciate your taught.\n\
             I will never forget you,Lord of the numbers.Hope we'll meet again!\n\
  PROFESSOR: Are you really so stupid or you just pretending?\n\
             You haven't won yet...\n\
             Oh oh, sorry, I forgot that you are from Polytechnic, again...\n\
             NULP - 4 letters, but such a deep meaning...\n\
             Anyway, to win this game, the points of each section\n\
             must match their meaning.It means: Points of Ulam\n\
             numbers must be an Ulam number, points of pair numbers \n\
             must be a pair number and points of happy numbers must be\n\
             a happy number. Go and win, or go and lose, loser, HA HA HA."
        }
        my_screen.addstr(y, x, dialogs[self])

    @staticmethod
    def professors_dialog():
        """
        (None) -> None

        Run and control dialogs with professor
        """
        while 1:
            try:
                my_screen.refresh()
                my_screen.clear()
                PrintOnScreen.print_professor_dialog(str(CV.dialogs))
                CheckConditions.analise_keypress(CheckConditions.get_key())
            finally:
                curses.endwin()
                break

    def print_pair_number(self):
        """
        (None) -> None

        add pair numbers on the field
        """
        counter = 0
        while counter < self:
            x = random.randint(2, 19)
            y = random.randint(2, 19) * 2
            n = DeMyHoriy_get_and_search_numbers.pair_number_generator(99)
            if not CheckConditions.is_on_element(x, y) and not \
                    CheckConditions.is_near_number(x, y):
                CV.playing_field[x][y] = str(n)
                CV.playing_field[x][y + 1] = str(n % 10)
                counter += 1

    def print_happy_number(self):
        """
        (None) -> None

        add happy numbers on the field
        """
        counter = 0
        while counter < self:
            x = random.randint(2, 19)
            y = random.randint(2, 19) * 2
            n = DeMyHoriy_get_and_search_numbers.happy_number_generator(99)
            if not CheckConditions.is_on_element(x, y) and not \
                    CheckConditions.is_near_number(x, y):
                CV.playing_field[x][y] = str(n)
                CV.playing_field[x][y + 1] = str(n % 10)
                counter += 1

    def print_ulam_number(self):
        """
        (None) -> None

        add ulam numbers on the field
        """
        counter = 0
        while counter < self:
            x = random.randint(2, 19)
            y = random.randint(2, 19) * 2
            n = DeMyHoriy_get_and_search_numbers.ulam_number_generator(99)
            if (not CheckConditions.is_on_element(x, y)) and not \
                    CheckConditions.is_near_number(x, y):
                CV.playing_field[x][y] = str(n)
                CV.playing_field[x][y + 1] = str(n % 10)
                counter += 1

    @staticmethod
    def bruteforce(x, y, string, brute_time=.01):
        """
        (int, int, str) -> void

        print on the screen bruteforce text (string) in coordinates (x;y)
        """
        x_init, y_init = x, y
        my_screen.clear()
        target_array = []
        string_array = ["", ""]
        for each in string:
            target_array.append(each)
            string_array.append('')
        i = 0
        while i < len(target_array):
            if string_array[i] != target_array[i]:
                string_array[i] = chr(random.randint(32, 126))
            if string_array[i] == target_array[i]:
                i += 1
            pos, x, y = 0, x_init, y_init
            my_screen.clear()
            while pos < len(string_array):
                my_screen.addstr(y, x, string_array[pos])
                pos += 1
                x += 1
                my_screen.refresh()
            time.sleep(brute_time)
        time.sleep(1)

    @staticmethod
    def bruteforce_creators(x, y, string, brute_time=.01):
        """
        (int, int, str) -> void

        print on the screen bruteforce text (string) in coordinates (x;y)
        """
        x_init, y_init = x, y
        target_array = []
        string_array = ["", ""]
        for each in string:
            target_array.append(each)
            string_array.append('')
        i = 0
        while i < len(target_array):
            if string_array[i] != target_array[i]:
                string_array[i] = chr(random.randint(32, 126))
            if string_array[i] == target_array[i]:
                i += 1
            pos, x, y = 0, x_init, y_init
            while pos < len(string_array):
                my_screen.addstr(y, x, string_array[pos])
                pos += 1
                x += 1
                my_screen.refresh()
            time.sleep(brute_time)


class CheckConditions:
    """
    Class of checking conditions functions
    get_key
    is_clear_field
    is_near_professor
    is_near_number
    is_near_wall
    analise_keypress
    is_on_element
    is_on_number
    score_counter
    """

    @staticmethod
    def get_key():
        """
        (None) -> str

        Return pressed key
        """
        return my_screen.getkey()

    @staticmethod
    def is_clear_field():
        """
        (None) -> bool

        Return True if field is empty and False if it isn`t
        """
        for i in CV.playing_field:
            for j in i:
                if not (str(j) in ". ♔■🕴"):
                    return False
        CV.numbers_on_field = False
        return True

    def is_near_professor(self=""):
        """
        (str) -> bool

        Check if character is near the professor
        """
        placement = {
            "up": CV.playing_field[CV.character[0] - 1]
            [CV.character[1]] == CV.professor[2],
            "down": CV.playing_field[CV.character[0] + 1]
            [CV.character[1]] == CV.professor[2],
            "left": CV.playing_field[CV.character[0]]
            [CV.character[1] - 2] == CV.professor[2],
            "right": CV.playing_field[CV.character[0]]
            [CV.character[1] + 2] == CV.professor[2]
        }

        if self == "":
            for each in placement:
                if placement[each]:
                    return placement[each]
            return False

        if not (CV.field == 0):
            return placement[self]
        elif placement[self]:
            PrintOnScreen.print_professor_dialog("1")
        else:
            PrintOnScreen.print_professor_dialog("2")
        return placement[self]

    @staticmethod
    def is_near_number(x, y):
        """
        (None) -> bool

        Check if character is near the number
        """

        if ((CV.playing_field[x - 1][y].isdigit()) or
                (CV.playing_field[x + 1][y]).isdigit() or
                (CV.playing_field[x][y + 2]).isdigit() or
                (CV.playing_field[x][y - 2]).isdigit()):
            return True
        return False

    @staticmethod
    def is_on_element(x, y):
        """
        (int, int) -> bool

        Check if element of playing field is
        filled with something except dot
        """
        return str(CV.playing_field[x][y]) in " ♔■🕴"

    @staticmethod
    def is_on_number():
        """
        (None) -> bool

        Return whether character is on cell with number
        """
        if str(CV.playing_field[CV.character[0]][CV.character[1]]).isdigit():
            return True
        return False

    def is_near_wall(self):
        """
        (str) -> bool

        Check if character is near the wall
        """
        placement = {
            "up": CV.playing_field[CV.character[0] - 1]
            [CV.character[1]] == CV.wall,
            "down": CV.playing_field[CV.character[0] + 1]
            [CV.character[1]] == CV.wall,
            "left": CV.playing_field[CV.character[0]]
            [CV.character[1] - 2] == CV.wall,
            "right": CV.playing_field[CV.character[0]]
            [CV.character[1] + 2] == CV.wall
        }
        return placement[self]

    def analise_keypress(self=" "):
        """
        (str) -> None

        Analise pressed keys
        """
        if self == 'w':
            Movement.move_up()
            PrintOnScreen.print_character()
        elif self == 'd':
            Movement.move_right()
            PrintOnScreen.print_character()
        elif self == 'a':
            Movement.move_left()
            PrintOnScreen.print_character()
        elif self == 's':
            Movement.move_down()
            PrintOnScreen.print_character()
        elif self == 'e' and CheckConditions.is_near_professor(""):
            PrintOnScreen.professors_dialog()
            CV.field = random.randint(1, 9)
            CV.character = [9, 2, "🕴 "]
            CV.dialogs += 1
            CV.level += 1
            CV.playing_field = eval("DeMyHoriy_playing_fields.field" + str(CV.field))
            PrintOnScreen.make_playing_field()
            PrintOnScreen.print_character()
        elif self == 'c' and CV.level > 3:
            my_screen.clear()
            PrintOnScreen.clear_playing_field()
            CV.numbers_on_field = False
            CV.character = [9, 2, "🕴 "]
            CV.field = random.randint(1, 9)
            CV.playing_field = eval("DeMyHoriy_playing_fields.field" + str(CV.field))
        elif self == "q" and CV.level > 3:
            PrintOnScreen.bruteforce(int(my_screen.getmaxyx()[1] / 2) - 13,
                                     int(my_screen.getmaxyx()[0] / 2),
                                     "YOU LOSE. HAVE A NICE DAY!", 0.001)
            CV.checker = False
        elif self == "m" and CV.field != 0 and CV.level > 3:
            menu()
        my_screen.refresh()

    @staticmethod
    def score_counter():
        """
        (None) -> None

                counter of scores
        """
        if CheckConditions.is_on_number():
            if DeMyHoriy_get_and_search_numbers.is_pair_number(int
                                                  (CV.playing_field
                                                   [CV.character[0]]
                                                   [CV.character[1]])):
                CV.score[0] += 1
            if DeMyHoriy_get_and_search_numbers.is_ulam_number(int
                                                  (CV.playing_field
                                                   [CV.character[0]]
                                                   [CV.character[1]])):
                CV.score[2] += 1
            if DeMyHoriy_get_and_search_numbers.is_happy_number(int
                                                   (CV.playing_field
                                                    [CV.character[0]]
                                                    [CV.character[1]])):
                CV.score[1] += 1
            pass


class Movement:
    """
    Class of movement functions
    move_up
    move_down
    move_left
    move_right
    """

    @staticmethod
    def move_up():
        """
        (None) -> None

        Move character up
        """
        my_screen.addstr(CV.character[0], CV.character[1], ".")
        my_screen.addstr(CV.character[0], CV.character[1] + 1, " ")
        if not (CheckConditions.is_near_wall("up") or
                CheckConditions.is_near_professor("up")):
            CV.character[0] -= 1

    @staticmethod
    def move_down():
        """
        (None) -> None

        Move character down
        """
        my_screen.addstr(CV.character[0], CV.character[1], ".")
        my_screen.addstr(CV.character[0], CV.character[1] + 1, " ")
        if not (CheckConditions.is_near_wall("down") or
                CheckConditions.is_near_professor("down")):
            CV.character[0] += 1

    @staticmethod
    def move_left():
        """
        (None) -> None

        Move character left
        """
        my_screen.addstr(CV.character[0], CV.character[1], ".")
        my_screen.addstr(CV.character[0], CV.character[1] + 1, " ")
        if not (CheckConditions.is_near_wall("left") or
                CheckConditions.is_near_professor("left")):
            CV.character[1] -= 2

    @staticmethod
    def move_right():
        """
        (None) -> None

        Move character right
        """
        my_screen.addstr(CV.character[0], CV.character[1], ".")
        my_screen.addstr(CV.character[0], CV.character[1] + 1, " ")
        if not (CheckConditions.is_near_wall("right") or
                CheckConditions.is_near_professor("right")):
            CV.character[1] += 2


def menu():

    def menu_points():
        """
        (None) -> None

        Print Main menu on screen
        """
        my_screen.addstr(1, int(max_yx[1] / 2) - 6, "▀ ▀ ▀ ▀ ▀ ▀ ▀")
        my_screen.addstr(2, int(max_yx[1] / 2) - 8, "↣  NumberFIELD  ↢")
        my_screen.addstr(3, int(max_yx[1] / 2) - 6, "▄ ▄ ▄ ▄ ▄ ▄ ▄")
        my_screen.addstr(4, int(max_yx[1] / 2) - 6, "▌ Main menu ▐")
        my_screen.addstr(5, int(max_yx[1] / 2) -
                         16, "▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄")
        my_screen.addstr(7, int(max_yx[1] / 2) - 5, "Start game")
        my_screen.addstr(9, int(max_yx[1] / 2) - 4, "Settings")
        my_screen.addstr(11, int(max_yx[1] / 2) - 8, "Story of the game")
        my_screen.addstr(13, int(max_yx[1] / 2) - 4, "Creators")
        my_screen.addstr(15, int(max_yx[1] / 2) - 6, "Quit the game")
        for each in range(6, 17):
            my_screen.addstr(each, int(max_yx[1] / 2) - 16, "▌")
            my_screen.addstr(each, int(max_yx[1] / 2) + 16, "▐")
        my_screen.addstr(17,
                         int(max_yx[1] / 2) - 16,
                         "▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀ ▀")
        my_screen.addstr(18,
                         int(max_yx[1] / 2) - 16,
                         "▌ press 'space' to chose a point▐")
        my_screen.addstr(19,
                         int(max_yx[1] / 2) - 16,
                         "▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄")

    def point1():
        """
        (None) -> None

        behavior of point1
        """
        my_screen.addstr(7, int(max_yx[1] / 2) - 7, "〉")
        my_screen.addstr(9, int(max_yx[1] / 2) - 6, " ")

    def point2():
        """
        (None) -> None

        behavior of point2
        """
        my_screen.addstr(7, int(max_yx[1] / 2) - 7, " ")
        my_screen.addstr(9, int(max_yx[1] / 2) - 6, "۞")
        my_screen.addstr(11, int(max_yx[1] / 2) - 10, " ")

    def point3():
        """
        (None) -> None

        behavior of point3
        """
        my_screen.addstr(9, int(max_yx[1] / 2) - 6, " ")
        my_screen.addstr(11, int(max_yx[1] / 2) - 10, "📚")
        my_screen.addstr(13, int(max_yx[1] / 2) - 6, " ")

    def point4():
        """
        (None) -> None

        behavior of point4
        """
        my_screen.addstr(11, int(max_yx[1] / 2) - 10, " ")
        my_screen.addstr(13, int(max_yx[1] / 2) - 6, "©")
        my_screen.addstr(15, int(max_yx[1] / 2) - 8, "  ")

    def point5():
        """
        (None) -> None

        behavior of point5
        """
        my_screen.addstr(13, int(max_yx[1] / 2) - 6, " ")
        my_screen.addstr(15, int(max_yx[1] / 2) - 8, "⎆")

    def settings():
        """
        (None) -> None

        Print on screen settings menu
        """

        def menu_set_points():
            """
            (None) -> None

            Print on screen points of settings menu
            """
            my_screen.addstr(3, int(max_yx[1] / 2) - 6, "■ ■ ■ ■ ■ ■ ■")
            my_screen.addstr(4, int(max_yx[1] / 2) - 6, "■ Settings  ■")
            my_screen.addstr(5, int(max_yx[1] / 2) -
                             16, "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
            my_screen.addstr(7, int(max_yx[1] / 2) - 5, "Difficulty")
            my_screen.addstr(9, int(max_yx[1] / 2) - 2, "Easy")
            my_screen.addstr(11, int(max_yx[1] / 2) - 3, "Normal")
            my_screen.addstr(13, int(max_yx[1] / 2) - 2, "Hard")
            for each in range(6, 17):
                my_screen.addstr(each, int(max_yx[1] / 2) - 16, "■")
                my_screen.addstr(each, int(max_yx[1] / 2) + 16, "■")
            my_screen.addstr(17,
                             int(max_yx[1] / 2) - 16,
                             "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")
            my_screen.addstr(18,
                             int(max_yx[1] / 2) - 16,
                             "■ press 'space' to chose a point■")
            my_screen.addstr(19,
                             int(max_yx[1] / 2) - 16,
                             "■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■")

        def point_set2():
            """
            (None) -> None

            behavior of point settings 2
            """
            my_screen.addstr(9, int(max_yx[1] / 2) - 4, "〉")
            my_screen.addstr(11, int(max_yx[1] / 2) - 5, " ")

        def point_set3():
            """
            (None) -> None

            behavior of point settings 3
            """
            my_screen.addstr(9, int(max_yx[1] / 2) - 4, " ")
            my_screen.addstr(11, int(max_yx[1] / 2) - 5, "〉")
            my_screen.addstr(13, int(max_yx[1] / 2) - 4, " ")

        def point_set4():
            """
            (None) -> None

            behavior of point settings 4
            """
            my_screen.addstr(11, int(max_yx[1] / 2) - 5, " ")
            my_screen.addstr(13, int(max_yx[1] / 2) - 4, "〉")

        point_set = 2
        my_screen.clear()
        my_screen.refresh()
        menu_set_points()
        init_screen(1)

        try:
            my_screen.addstr(9, int(max_yx[1] / 2) - 4, "〉")
            menu_set_points()
            while 1:
                movement_key = my_screen.getkey()
                if movement_key == "w" and point_set > 2:
                    point_set -= 1
                if movement_key == "s" and point_set < 4:
                    point_set += 1
                if movement_key == " ":
                    if point_set == 2:
                        CV.difficulty = 15
                        point_set2()
                        break
                    if point_set == 3:
                        CV.difficulty = 21
                        point_set3()
                        break
                    if point_set == 4:
                        CV.difficulty = 30
                        point_set4()
                        break
                eval("point_set" + str(point_set) + "()")
            my_screen.refresh()
        finally:
            my_screen.clear()
            curses.endwin()

    def creators():
        """
        (None) -> None

        Print on screen creators and license
        """
        try:
            my_screen.clear()
            my_screen.refresh()
            init_screen(1)
            PrintOnScreen.bruteforce_creators(
                int(max_yx[1] / 2) - 7,
                4,
                "APPS UCU 2018",
                brute_time=0.001)
            PrintOnScreen.bruteforce_creators(
                int(max_yx[1] / 2) - 15,
                5,
                "our game is licensed under the",
                brute_time=0.0005)
            PrintOnScreen.bruteforce_creators(
                int(max_yx[1] / 2) - 16,
                6,
                "GNU General Public License v 3.0",
                brute_time=0.0005)
            PrintOnScreen.bruteforce_creators(
                int(max_yx[1] / 2) - 9,
                8,
                "Our creators team:",
                brute_time=0.0005)
            PrintOnScreen.bruteforce_creators(
                int(max_yx[1] / 2) - 6,
                9,
                "Datsko Denys",
                brute_time=0.0005)
            PrintOnScreen.bruteforce_creators(
                int(max_yx[1] / 2) - 10,
                10,
                "Ovsiannikov Hryhoriy",
                brute_time=0.0005)
            PrintOnScreen.bruteforce_creators(
                int(max_yx[1] / 2) - 9,
                11,
                "Morgunenko Mykola",
                brute_time=0.0005)
        finally:
            time.sleep(1)
            my_screen.addstr(
                13,
                int(max_yx[1] / 2) - 17,
                "Press any movement_key to continue")
            my_screen.getkey()
            my_screen.clear()
            curses.endwin()

    def quit_game():
        """
        (None) -> None

        quit_game the game
        """
        my_screen.clear()
        PrintOnScreen.bruteforce(
            int(max_yx[1] / 2) - 13,
            int(max_yx[0] / 2),
            "GOOD BYE! HAVE A NICE DAY!", 0.001)
        exit()

    def story():
        """
        (None) -> None

        Print on screen story of the game
        """
        try:
            my_screen.clear()
            my_screen.addstr(2, 0,
                             '''
    Student of NULP - NUB visits KMA. He is a very veeeerrry curious person\n\
    so he finds his way into restricted area of KMA's library\n\
    one of the oldest in Ukraine. Nub tries to find any information to become\n\
    more intelligent so he could become a student of UCU. He finds nothing but\n\
    a mysterious CD with a 'NumberField' name on it and numbers that make
    absolutely no sense. A librarian catches noob and gets him out of KMA,\n\
    but he doesn't notice a CD in Nub's pocket. Nub returns to his\n\
    hometown - Lviv, where he tries to get some information about\n\
    the game. So he is convinced that the only way to find out something\n\
    about this CD is to visit Sheptytsky's Center and search for\n\
    any information in books. As a result of 3 hours of searching\n\
    he does find a mention about existing of such CD by Ulam,\n\
    however it makes things more mysterious and Nub has a way \n\
    more questions now. After spending a whole day in UCU's library\n\
    he finds nothing useful, so he decides to run that CD on a local\n\
    computer. In a moment NULP's student understands that the\n\
    world that surrounds him is no longer real. It turns to be\n\
    a completely another virtual Universe that is called NumberField... 
                           ''' )

            init_screen(1)
            my_screen.refresh()
        finally:
            time.sleep(3)
            my_screen.addstr(
                1,
                int(max_yx[1] / 2) - 14,
                "Press any key to continue...")
            my_screen.getkey()
            my_screen.clear()
            curses.endwin()

    point = 1
    max_yx = my_screen.getmaxyx()
    try:
        my_screen.clear()
        my_screen.refresh()
        init_screen(1)
        my_screen.addstr(7, int(max_yx[1] / 2) - 7, "〉")
        menu_points()
        while 1:
            key = my_screen.getkey()
            if key == "w" and point > 1:
                point -= 1
            if key == "s" and point < 5:
                point += 1
            if key == " ":
                if point == 1:
                    break
                if point == 2:
                    settings()
                    menu_points()
                if point == 3:
                    story()
                    menu_points()
                if point == 4:
                    creators()
                    menu_points()
                if point == 5:
                    quit_game()
            my_screen.clear()
            my_screen.refresh()
            init_screen(1)
            menu_points()
            eval("point" + str(point) + "()")
        my_screen.refresh()
    finally:
        my_screen.clear()
        curses.endwin()


my_screen = curses.initscr()
init_screen(1)
curses.noecho()
curses.curs_set(False)
menu()
try:
    '''
    instruction for the game, first init
    '''
    my_screen.refresh()
    my_screen.addstr(6, 10, "Movement:\n          W - move up \n\
          S - move down \n          D - move right \n\
          A - move left\n\
          ENGLISH LAYOUT ONLY!\n\
          NO CAPS LOCK! (This one doesn't count)\n\
          Press any key to continue")
    my_screen.getch()
    my_screen.refresh()
    PrintOnScreen.make_playing_field()
    PrintOnScreen.print_character()
    PrintOnScreen.print_information()
    CV.numbers_on_field = False
    '''
    main loop
    '''
    while CV.checker:
        CheckConditions.analise_keypress(CheckConditions.get_key())
        '''
        generate numbers on field on level 1-4
        '''
        if CV.field != 0:
            if not CV.numbers_on_field:
                if CV.level == 1:
                    PrintOnScreen.print_pair_number(CV.difficulty)
                elif CV.level == 2:
                    PrintOnScreen.print_happy_number(CV.difficulty)
                elif CV.level == 3:
                    PrintOnScreen.print_ulam_number(CV.difficulty)
                else:
                    PrintOnScreen.print_ulam_number(CV.difficulty // 3)
                    PrintOnScreen.print_happy_number(CV.difficulty // 3)
                    PrintOnScreen.print_pair_number(CV.difficulty // 3)
                CV.numbers_on_field = True
            PrintOnScreen.make_playing_field()
        CheckConditions.score_counter()
        PrintOnScreen.print_information()
        PrintOnScreen.print_character()
        if CheckConditions.is_on_number():
            CV.playing_field[CV.character[0]][CV.character[1]] = "."
            CV.playing_field[CV.character[0]][CV.character[1] + 1] = " "
        '''
        if you get all numbers on field and
        not on the 0th field (with professor)
        then you teleport on professor's field
        else (if your field 4 and more) generate numbers on the random field
        and refresh field
        '''
        if CheckConditions.is_clear_field() and CV.field != 0:
            CV.numbers_on_field = False
            if CV.level < 4:
                CV.field = 0
                CV.playing_field = DeMyHoriy_playing_fields.field0
            else:
                CV.field = random.randint(1, 9)
                CV.playing_field = eval(
                    "DeMyHoriy_playing_fields.field" + str(CV.field))
                PrintOnScreen.print_ulam_number(CV.difficulty // 3)
                PrintOnScreen.print_happy_number(CV.difficulty // 3)
                PrintOnScreen.print_pair_number(CV.difficulty // 3)
                CV.numbers_on_field = True
            my_screen.clear()
            CV.character = [9, 2, "🕴 "]
            PrintOnScreen.make_playing_field()
            PrintOnScreen.print_information()
            PrintOnScreen.print_character()
        '''
        if you are on 4th level then you can leave game (then you are loser)
        or skip level (if you have "bad" numbers on field)
        and if
        score of your even numbers - even number
        score of your happy numbers - happy number
        score of your Ulam numbers - Ulam number
        then you win!

        '''
        if CV.level > 3:
            my_screen.addstr(6, 46, "to quit the game press 'q' ...")
            my_screen.addstr(8, 46, "to skip the level press 'c' ...")
            my_screen.addstr(10, 46, "to go to the menu press 'm' ...")
            if (DeMyHoriy_get_and_search_numbers.is_pair_number(CV.score[0]) and
                    DeMyHoriy_get_and_search_numbers.is_happy_number(CV.score[1]) and
                    DeMyHoriy_get_and_search_numbers.is_ulam_number(CV.score[2])):
                PrintOnScreen.bruteforce(
                    int(my_screen.getmaxyx()[1] / 2) - 5,
                    int(my_screen.getmaxyx()[0] / 2),
                    "YOU WIN!")
                CV.checker = False
finally:
    curses.endwin()
