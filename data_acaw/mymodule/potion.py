import sys
import time

import pyautogui

sys.path.append('C:/acaw/my_acaw/mymodule')

import variable as v_


def potion_start(cla):
    try:

        print("potion_start")



    except Exception as e:
        print(e)
        return 0


def my_potion_check_ex(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, text_check_get, click_pos_2, drag_pos, in_number_check, int_put_, change_number
        from action import clean_screen, out_check

        potion_read_ready = False
        #v_.potion_search_count = 0
        potion_tuto_count = 0
        while potion_read_ready is False:
            potion_tuto_count += 1
            if potion_tuto_count > 10:
                potion_read_ready = True
                print("튜토 진행중이라 물약 갯수 읽기 불가능")
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\potion_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 385, 760, 420, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                maul_move_check(cla)

                potion_read_ready = True
                potion_ = text_check_get(750, 482, 785, 495, cla)
                print("앞4자리 potion_?", potion_)
                potion_many = change_number(potion_)

                if potion_many != v_.potion_result:

                    v_.potion_result = potion_many
                    potion_bool = in_number_check(cla, potion_)

                    if potion_bool == True:


                        print("포션 있음 :", v_.potion_result)
                        if int(v_.potion_result) < 100:
                            v_.potion_search_count += 1
                            print("v_.potion_search_count_1 (+)", "[ " + str(v_.potion_search_count) + " ]")
                        else:
                            if v_.potion_search_count > 1:
                                v_.potion_search_count -= 1
                                print("v_.potion_search_count_1 (-)", "[ " + str(v_.potion_search_count) + " ]")
                        if v_.potion_search_count > 10:
                            v_.potion_search_count = 0
                            print("포션사러 가주앗")
                            buy_potion(cla)
                    else:
                        v_.potion_search_count += 1
                        print("v_.potion_search_count_2 (+)", "[ " + str(v_.potion_search_count) + " ]")
                        if v_.potion_search_count > 10:
                            v_.potion_search_count = 0
                            print("포션사러 가주앗")
                            buy_potion(cla)
                            #click_pos_2(255, 980, cla)
                        print("포션 못 읽음")
                else:
                    print("이전과 포션 숫자가 같다", v_.potion_result)
            else:
                result_out = out_check(cla)
                if result_out == True:
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\clean_screen\\bag_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 660, 750, 705, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("bag_1", imgs_)
                        click_pos_2(875, 340, cla)
                        time.sleep(0.1)
                        click_pos_2(820, 685, cla)
                        look_potion = False
                        look_ok = False
                        look_potion_count = 0
                        while look_potion is False:
                            look_potion_count += 1
                            if look_potion_count > 20:
                                look_potion = True

                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\small_potion_11.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(680, 300, 960, 670, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                look_potion = True
                                look_ok = True
                                x_reg = imgs_.x
                                y_reg = imgs_.y
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\small_potion_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(695, 355, 940, 670, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    look_potion = True
                                    look_ok = True
                                    x_reg = imgs_.x
                                    y_reg = imgs_.y
                                else:
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\small_potion_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(695, 355, 940, 670, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        look_potion = True
                                        look_ok = True
                                        x_reg = imgs_.x
                                        y_reg = imgs_.y
                        if look_ok == True:
                            click_pos_reg(x_reg, y_reg, cla)
                            time.sleep(0.1)
                            click_pos_2(865, 680, cla)
                        else:

                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\zero.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 980, 500, 1010, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("숫자 '0'이다. 포션 사러 가자", imgs_)
                                potion_read_ready = True
                                buy_potion(cla)
                            else:
                                print("숫자 '0'이 아니다.")

                                potion_tuto_count += 1
                                if potion_tuto_count > 3:
                                    drag_pos(820, 640, 820, 460, cla)
                                    time.sleep(1.5)
                                    if potion_tuto_count > 6:
                                        potion_tuto_count = 0
                                        print("포션 수량 계속 알아보자")
                                        # buy_potion(cla)
                                        # drag_pos(820, 460, 820, 640, cla)
                                        click_pos_2(875, 340, cla)
                                        time.sleep(2)




                    else:
                        click_pos_2(770, 60, cla)

                        # 여기에 무기 체크
                        if v_.grow_jangbi == True:
                            grow_jangbi_check(cla)



                else:
                    clean_screen(cla)



        #
        #for i in range(1):
        #    potion_ = text_check_get(725 + i, 360, 750, 370, cla)
        #    print("<<" + str(725 + i) + ">>")
        #    print(potion_)


    except Exception as e:
        print(e)
        return 0

def my_potion_check(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, text_check_get, click_pos_2, drag_pos, in_number_check, int_put_, change_number
        from action import clean_screen, out_check

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\out_small_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(460, 950, 500, 1005, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            v_.my_potion_check = 0
            print("out_small_potion", imgs_)
        else:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\out_small_potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(460, 950, 500, 1005, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                v_.my_potion_check = 0
                print("out_small_potion", imgs_)
            else:
                v_.my_potion_check += 1
                print("포션 없다", v_.my_potion_check)
                if v_.my_potion_check > 3:
                    buy_potion(cla)




    except Exception as e:
        print(e)
        return 0


def maul_move_check(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import bag_open

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\maul_move_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(220, 940, 290, 1010, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("마을 이동서 있다.")
        else:
            print("마을 이동서 없어서 빠른 실행칸에 넣기")
            bag_open(cla)
            search_maul_move = False
            search_maul_move_count = 0
            while search_maul_move is False:
                search_maul_move_count += 1
                if search_maul_move_count > 3:

                    # 이때는 지도로 마을 가기
                    go_worldmap_maul(cla)
                    search_maul_move = True
                click_pos_2(875, 340, cla)
                time.sleep(0.5)
                click_pos_2(815, 680, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\maul_move_check2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 350, 940, 670, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("마을 이동서 있다.")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(250, 975, cla)
                    search_maul_move = True
                else:
                    drag_pos(820, 640, 820, 460, cla)
                    time.sleep(1)


    except Exception as e:
        print(e)
        return 0

def soongan_move_check(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import bag_open


        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\soongan_move_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 940, 350, 1010, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("랜덤 이동서 있다.")
        else:
            print("랜덤 이동서 없어서 빠른 실행칸에 넣기")
            bag_open(cla)
            search_maul_move = False
            search_maul_move_count = 0
            while search_maul_move is False:
                search_maul_move_count += 1
                if search_maul_move_count > 3:
                    search_maul_move = True
                click_pos_2(875, 340, cla)
                time.sleep(0.5)
                click_pos_2(815, 680, cla)
                time.sleep(0.5)
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\soongan_move_check2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(680, 350, 940, 670, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("순간 이동서 있다.")
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(310, 975, cla)
                    search_maul_move = True
                else:
                    drag_pos(820, 640, 820, 460, cla)
                    time.sleep(1)


    except Exception as e:
        print(e)
        return 0

def go_worldmap_maul(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import bag_open, clean_screen

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\maul_.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 70, 150, 150, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            in_maul = True
        else:
            in_maul = False

        if in_maul == False:
            in_maul_count = 0
            while in_maul is False:
                in_maul_count += 1
                if in_maul_count > 5:
                    in_maul = True

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_worldmap.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(780, 30, 960, 100, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("title_worldmap", imgs_)
                    click_pos_2(35, 85, cla)
                    time.sleep(0.5)

                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\worldmap_maul_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(50, 100, 110, 960, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        click_pos_2(870, 1005, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\in_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 610, 640, 670, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(0.5)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\maul_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 70, 150, 150, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            in_maul = True
                            break
                        time.sleep(1)
                else:
                    clean_screen(cla)
                    click_pos_2(150, 150, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 940, 350, 1010, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("title_worldmap")
                            break
                        time.sleep(0.2)


    except Exception as e:
        print(e)
        return 0


def buy_potion(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2, in_number_check, int_put_, text_check_get, change_number, drag_pos
        from massenger import line_to_me
        from action import clean_screen
        from get_item import set_collection, boonhae

        close_to_potion = False
        close_to_potion_count = 0
        while close_to_potion is False:
            close_to_potion_count += 1
            if close_to_potion_count > 10:
                close_to_potion = True
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\close_to_potion.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 300, 940, 360, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                close_to_potion = True

        # 마을 도착 여부
        in_maul = False
        again = False
        in_maul_count = 0
        dangerous = 0
        while in_maul is False:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\maul_.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 70, 150, 150, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("maul______", imgs_)

                drag_pos(240, 100, 600, 100, cla)
                time.sleep(0.3)
                click_pos_2(425, 105, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 30, 840, 80, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)
                # full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_1.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(20, 80, 300, 200, cla, img, 0.8)
                # if imgs_ is not None and imgs_ != False:
                #     print("jabhwa_111111", imgs_)
                #     click_pos_reg(imgs_.x, imgs_.y, cla)
                # else:
                #     full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_2.PNG"
                #     img_array = np.fromfile(full_path, np.uint8)
                #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                #     imgs_ = imgs_set_(20, 80, 300, 200, cla, img, 0.8)
                #     if imgs_ is not None and imgs_ != False:
                #         print("jabhwa_222222", imgs_)
                #         click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 840, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jabhwa_title!!!!!!!!!!", imgs_)
                    in_maul = True
                else:
                    clean_screen(cla)
                    in_maul_count += 1
                    if 2 < in_maul_count < 4:

                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\maul_move_check.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(220, 940, 290, 1010, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(255, 980, cla)
                        else:
                            maul_move_check(cla)

                    if in_maul_count > 10:
                        in_maul_count = 0
                        dangerous += 1
                        if dangerous > 1:
                            print("stop!!!")
                            in_maul = True
                            again = True
                            line_to_me(cla, "아키 마을 못 가고 있다")
            time.sleep(0.5)

        # 마을 진입 후
        if again == False:
            isJabhwa = False
            while isJabhwa is False:
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 30, 840, 80, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jabhwa_title", imgs_)
                    # 포션 구매
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\40level.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 140, 240, 970, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("40level", imgs_)
                        print("작은 포션 사자")
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_small_potion.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 140, 240, 970, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jabhwa_small_potion", imgs_)
                            click_pos_reg(imgs_.x + 100, imgs_.y, cla)
                            time.sleep(0.5)

                            if v_.now_ing_schedule != "튜토육성":

                                per_count = 0
                                click_count = 0
                                per_ready = False
                                while per_ready is False:
                                    for i in range(3):
                                        potion_per = text_check_get(331 - i, 975, 390, 990, cla)
                                        print("potion_per?", potion_per)
                                        buy_ready = in_number_check(potion_per)
                                        if buy_ready == True:
                                            break
                                    if buy_ready == True:
                                        buy_per_ready = change_number(potion_per)
                                        print("buy_per_ready", buy_per_ready)
                                        print("buy_per_ready[0]", buy_per_ready[0])
                                        if int(buy_per_ready[0]) >= 7:
                                            click_count = per_count - 1
                                            print("click_count", click_count)
                                            # per_ready = True
                                            click_pos_2(300, 880, cla)
                                            time.sleep(0.2)

                                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jabhwa_small_potion.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(0, 140, 240, 970, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("jabhwa_small_potion.......", imgs_)
                                                x_reg = imgs_.x + 100
                                                y_reg = imgs_.y
                                                # click_pos_reg(imgs_.x + 100, imgs_.y, cla)
                                                time.sleep(0.5)
                                                isJabhwa = True
                                                per_ready = True
                                                if click_count > 0:

                                                    last_buy = False
                                                    last_buy_count = 0
                                                    while last_buy is False:
                                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jab_confirm.PNG"
                                                        img_array = np.fromfile(full_path, np.uint8)
                                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                        imgs_ = imgs_set_(480, 600, 650, 650, cla, img, 0.8)
                                                        if imgs_ is not None and imgs_ != False:
                                                            print("jab_confirm", imgs_)
                                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                                            last_buy = True
                                                        else:
                                                            last_buy_count += 1
                                                            if last_buy_count > 3:
                                                                last_buy = True
                                                                line_to_me(cla, "물약 사는데 문제 있다ㅠ")
                                                                clean_screen(cla)
                                                            click_pos_2(x_reg, y_reg, cla)
                                                            time.sleep(0.3)
                                                            for i in range(click_count):
                                                                click_pos_2(415, 945, cla)
                                                                time.sleep(0.2)
                                                            click_pos_2(865, 995, cla)
                                                            time.sleep(0.5)
                                                        time.sleep(0.5)
                                        else:
                                            per_count += 1
                                            click_pos_2(415, 945, cla)
                                            time.sleep(0.5)
                                        time.sleep(0.5)
                            else:
                                last_buy = False
                                last_buy_count = 0
                                while last_buy is False:
                                    last_buy_count += 1
                                    if last_buy_count > 3:
                                        last_buy = True
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jab_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(480, 600, 650, 650, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jab_confirm", imgs_)
                                        isJabhwa = True
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        last_buy = True
                                        time.sleep(2)
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jab_confirm.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(810, 30, 900, 90, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            line_to_me(cla, "돈 없어서 보석 상점 와있다")

                                    else:
                                        for i in range(3):
                                            click_pos_2(415, 945, cla)
                                            time.sleep(0.3)
                                        click_pos_2(865, 995, cla)
                                    time.sleep(1)

                    else:
                        print("40레벨 포션 구매하기")

                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jab_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 600, 650, 650, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("jab_confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    # 마을 이동 구매
                    move_ = False
                    move_count = 0
                    while move_ is False:
                        move_count += 1
                        if move_count > 5:
                            move_ = True
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jab_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 600, 650, 650, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jab_confirm", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            move_ = True
                        else:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\guihwan_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 140, 240, 970, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("guihwan.......", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                click_pos_2(320, 945, cla)
                                time.sleep(0.5)
                                click_pos_2(865, 995, cla)
                                time.sleep(0.5)
                            time.sleep(0.3)

                    # 순간 이동 구매
                    move_ = False
                    move_count = 0
                    while move_ is False:
                        move_count += 1
                        if move_count > 5:
                            move_ = True
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\jab_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 600, 650, 650, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jab_confirm", imgs_)
                            move_ = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\soongan_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 140, 240, 970, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("soongan.......", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                click_pos_2(320, 945, cla)
                                time.sleep(0.5)
                                click_pos_2(865, 995, cla)
                                time.sleep(0.5)
                            time.sleep(0.3)



                time.sleep(0.3)
        v_.jadong_on = False

        set_collection(cla)
        boonhae(cla)

        soongan_move_check(cla)

        clean_screen(cla)

    except Exception as e:
        print(e)
        return 0


def grow_jangbi_check(cla):
    try:
        import cv2
        import numpy as np
        from function_acaw import click_pos_reg, imgs_set_, click_pos_2, drag_pos
        from action import bag_open

        click_pos_2(815, 680, cla)

        time.sleep(0.5)

        jb_list = ["toogoo", "hwal_1", "gabot", "baji", "pal", "sinbal", "mangto"]

        for i in range(len(jb_list)):

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\" + jb_list[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(680, 300, 960, 670, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print(jb_list[i], imgs_)
                x_reg = imgs_.x
                y_reg = imgs_.y
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\jangchag.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_reg - 50, y_reg - 50, x_reg, y_reg, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("jangchag", imgs_)
                else:
                    print("없")
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\" + jb_list[i] + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 300, 960, 670, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.1)
                        click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0
