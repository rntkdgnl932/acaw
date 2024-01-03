import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dungeon_start(cla, where):
    import numpy as np
    import cv2
    import os
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2
    from action import clean_screen, juljun_off, juljun_on, auto_on
    from potion import my_potion_check

    try:

        # where = "던전_마다나_6", "던전_얼음잔_6", "던전_얼음잔_6", "던전_신전_6", "던전_폐광_6", "던전_도서관_2"
        # where = "바다_길잃은바다_5"
        # where = "렐름_전장_5", "렐름_틈_5"

        print("dungeon_start", where)


        # 먼저 절전모드인지 파악하고

        # 절전모드일 경우 사냥터가 맞는지, 자동 사냥 중인지 파악하고, 물약체크하기...

        # 절전모드가 아닐경우 현재 위치 파악하고, 현재 위치가 지정한 자동사냥터라면 절전모드 후 사냥하기
        # 절전모드가 아닐경우 현재 위치 파악하고, 현재 위치가 지정한 자동사냥터가 아니라면 이동하기(던전일 경우는 빠져나오기)

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\juljun\\juljun_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 400, 600, 600, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\juljun\\juljun_jadong.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 350, 550, 450, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("어디에선가 자동사냥중", imgs_)
                # 사냥터가 맞는지 체크하기
                result_dungeon_check = dungeon_in_spot_check(cla, where)

                if result_dungeon_check == True:
                    print("지정한 던전에서 사냥중")
                    my_potion_check(cla)
                else:
                    juljun_off(cla)

                    # 사냥터로 이동
                    dungeon_in_spot_go(cla, where)

            else:
                juljun_off(cla)

                auto_on(cla)

                juljun_on(cla)


        else:


            result_dungeon_check = dungeon_in_spot_check(cla, where)

            if result_dungeon_check == True:
                # 절전모드로 전환

                auto_on(cla)

                juljun_on(cla)


            else:
                # 사냥터로 이동
                dungeon_in_spot_go(cla, where)



        # 자동 사냥터 맞는지...

        # 맞다면 오토사냥 중인지...

        # 지정한 자동 사냥터 아니라면 이동하기



    except Exception as e:
        print(e)
        return 0


def dungeon_in_spot_check(cla, where):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check

    try:

        # where = "자동_송별의뜰"

        print("dungeon_in_spot_check", where)

        if "_" in where:
            spot_ = where.split("_")
        print("spot_", spot_)

        # where = "던전_마다나_6", "던전_얼음잔_6", "던전_신전_6", "던전_폐광_6", "던전_도서관_2"
        # where = "바다_길잃은바다_5"
        # where = "렐름_전장_5", "렐름_틈_5"

        # spot_[0] => 던전 // 바다 // 렐름
        # spot[1] => 마다나, 얼음잔, 신전, 폐광, 도서관 // 길잃은바다 // 전장, 틈
        # spot[2] => 스텝...1~6


        if spot_[0] == "던전":
            file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_list_dun.txt"
        elif spot_[0] == "바다":
            file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_list_sea.txt"
        elif spot_[0] == "렐름":
            file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_list_lelm.txt"

        with open(file_path, "r", encoding='UTF8') as file:
            read_list = file.read().splitlines()
            # print("read_list", read_list)

        for i in range(len(read_list)):
            result_spot = read_list[i].split("_")
            # print("result_spot", result_spot)
            if spot_[1] == result_spot[0]:
                spot_name = result_spot[1]



        spot_true = False


        # 절전일때
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\juljun\\juljun_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 400, 600, 600, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_juljun_list\\" + str(spot_name) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(100, 920, 220, 980, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dungeon_jadong_spot", spot_name)
                spot_true = True


        # 절전 아닐때
        else:
            in_spot = False
            in_spot_count = 0
            while in_spot is False:
                in_spot_count += 1
                if in_spot_count > 6:
                    in_spot = True

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_out.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 70, 300, 150, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    in_spot = True

                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_out_list\\" + str(spot_name) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 90, 200, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("out_dungeon_spot", spot_name)
                        spot_true = True

                    else:
                        # 던전일 경우 나가기 클릭하도록...
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dun_list.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(20, 80, 55, 125, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            for i in range(10):
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_out.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 70, 300, 150, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\common_.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(40, 70, 120, 120, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(45, 105, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\boho_.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(40, 70, 120, 120, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(45, 105, cla)
                                            break
                                time.sleep(0.5)
                            time.sleep(1)
                            for i in range(10):
                                result_out = out_check(cla)
                                if result_out == True:
                                    break
                                time.sleep(1)
                else:
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\common_.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 70, 120, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("common_", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_out.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 70, 300, 150, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.3)
                    else:
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\maul_.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 70, 120, 120, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("maul_", imgs_)
                            # 바로 사냥터 진입하기
                            in_spot = True
                        else:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\boho_.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 70, 120, 120, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("boho_", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for i in range(10):
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_out.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(200, 70, 300, 150, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.3)


        # 자동 사냥터 맞는지...

        # 맞다면 오토사냥 중인지...

        # 지정한 자동 사냥터 아니라면 이동하기

        return spot_true

    except Exception as e:
        print(e)
        return 0

def dungeon_in_spot_go(cla, where):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import out_check, clean_screen, menu_open, auto_on
    from potion import soongan_move_check
    from schedule import myQuest_play_add

    try:

        dun_clear = False

        print("dungeon_in_spot_go", where)

        if "_" in where:
            spot_ = where.split("_")
        print("spot_", spot_)

        # where = "던전_마다나_6", "던전_얼음잔_6", "던전_신전_6", "던전_폐광_6", "던전_도서관_2"
        # where = "바다_길잃은바다_5"
        # where = "렐름_전장_5", "렐름_틈_5"

        # spot_[0] => 던전 // 바다 // 렐름
        # spot[1] => 마다나, 얼음잔, 신전, 폐광, 도서관 // 길잃은바다 // 전장, 틈
        # spot[2] => 스텝...1~6

        if spot_[0] == "던전":
            file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_list_dun.txt"
        elif spot_[0] == "바다":
            file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_list_sea.txt"
        elif spot_[0] == "렐름":
            file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_list_lelm.txt"

        with open(file_path, "r", encoding='UTF8') as file:
            read_list = file.read().splitlines()
            # print("read_list", read_list)

        for i in range(len(read_list)):
            result_spot = read_list[i].split("_")
            # print("result_spot", result_spot)
            if spot_[1] == result_spot[0]:
                spot_name = result_spot[1]


        in_spot = False
        in_spot_count = 0
        while in_spot is False:
            in_spot_count += 1
            if in_spot_count > 6:
                in_spot = True

            full_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_step_title\\" + str(spot_name) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 80, 240, 140, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("step 클릭해서 진입하자", spot_name)
                # spot_[2] => 스텝...1~6
                y_reg = 110 + (50 * int(spot_[2]))
                if spot_[1] == "도서관":
                    if int(spot_[2]) >= 2:
                        y_reg = 110 + (50 * 2)

                click_pos_2(100, y_reg, cla)
                time.sleep(0.5)

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dun_move_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 980, 900, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dun_in_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 620, 670, 670, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(0.3)
                time.sleep(0.5)
                # 아직 그대로라면...던전 끝...예상함...
                print("아직 그대로라면...던전 끝...예상함...")
                full_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_step_title\\" + str(
                    spot_name) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(5, 80, 240, 140, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:

                    click_pos_2(915, 60, cla)

                else:
                    # 현장 도착하는지 파악
                    print("현장 도착하는지 파악")
                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            break
                        time.sleep(1)

                    # 도착했으면 랜덤(순간) 이동서 클릭하기
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\soongan_move_check.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 940, 350, 1010, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)

                    result_soongan = soongan_move_check(cla)

                    if result_soongan == True:
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\common_grow\\soongan_move_check.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 940, 350, 1010, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)
                            # 다시 현장 도착하는지 파악
                            for i in range(10):
                                result_out = out_check(cla)
                                if result_out == True:
                                    in_spot = True
                                    # 사냥하기
                                    auto_on(cla)
                                    break
                                time.sleep(1)


            else:

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(780, 30, 900, 90, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("title_dungeon")



                    # spot_[0] => 던전 // 바다 // 렐름
                    # spot[1] => 마다나, 얼음잔, 신전, 폐광, 도서관 // 길잃은바다 // 전장, 틈
                    # spot[2] => 스텝...1~6

                    # 해당 던전 클릭하자
                    if spot_[0] == "던전":
                        click_pos_2(90, 105, cla)
                        time.sleep(0.2)
                        click_pos_2(90, 105, cla)
                        drag_pos(100, 530, 700, 530, cla)
                    elif spot_[0] == "바다":
                        click_pos_2(220, 105, cla)
                        time.sleep(0.2)
                        click_pos_2(220, 105, cla)
                    elif spot_[0] == "렐름":
                        click_pos_2(350, 105, cla)
                        time.sleep(0.2)
                        click_pos_2(350, 105, cla)

                    time.sleep(0.5)

                    event_x = 240

                    # 해당 던전 스텝 활성화 하기전에 시간 남아있는지 확인하자
                    if spot_[1] == "이벤트":
                        drag_pos(100, 530, 700, 530, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(165, 630, 240, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True
                    elif spot_[1] == "마다나":
                        drag_pos(100, 530, 700, 530, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(415 + event_x, 630, 490 + event_x, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True
                    elif spot_[1] == "얼음잔":
                        drag_pos(800, 530, 200, 530, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(375, 630, 445, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True
                    elif spot_[1] == "신전":
                        drag_pos(800, 530, 200, 530, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(620, 630, 700, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True
                    elif spot_[1] == "폐광":
                        drag_pos(100, 530, 700, 530, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(165 + event_x, 630, 240 + event_x, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True
                    elif spot_[1] == "도서관":
                        drag_pos(800, 530, 200, 530, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(875, 630, 950, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True
                    elif spot_[1] == "길잃은바다":
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(165, 630, 240, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True
                    elif spot_[1] == "전장":
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(165, 630, 240, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True
                    elif spot_[1] == "틈":
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\time_out.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(415, 630, 490, 690, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            dun_clear = True

                    if dun_clear == True:
                        print("던전 클리어")
                        in_spot = True

                        myQuest_play_add(cla, where)
                        time.sleep(0.2)


                    else:
                        # 해당 던전 스텝 활성화 하자

                        full_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_step_in_click\\" + str(spot_name) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 560, 960, 620, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("dungeon_step_in_click", spot_name)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for i in range(10):
                                full_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_step_title\\" + str(
                                    spot_name) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(5, 80, 240, 140, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.5)
                        else:
                            if spot_[0] == "던전":
                                drag_pos(800, 530, 200, 530, cla)
                            time.sleep(0.5)
                            full_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_step_in_click\\" + str(
                                spot_name) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(5, 560, 960, 620, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("dungeon_step_in_click", spot_name)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                for i in range(10):
                                    full_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\dungeon\\dungeon_step_title\\" + str(
                                        spot_name) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(5, 80, 240, 140, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    time.sleep(0.5)

                else:
                    menu_open(cla)
                    click_pos_2(905, 115, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_dungeon.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 30, 900, 90, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
            time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0
