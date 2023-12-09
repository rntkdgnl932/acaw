import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla, where):
    import numpy as np
    import cv2
    import os
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2
    from action import clean_screen, juljun_off, juljun_on, auto_on
    from potion import my_potion_check

    try:

        # where = "자동_송별의뜰"

        print("jadong_start", where)


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
                result_jadong_check = jadong_in_spot_check(cla, where)

                if result_jadong_check == True:
                    print("지정한 사냥터에서 사냥중")
                    my_potion_check(cla)
                else:
                    juljun_off(cla)

                    # 사냥터로 이동
                    jadong_in_spot_go(cla, where)

            else:
                juljun_off(cla)

                auto_on(cla)

                juljun_on(cla)


        else:


            result_jadong_check = jadong_in_spot_check(cla, where)

            if result_jadong_check == True:
                # 절전모드로 전환

                auto_on(cla)

                juljun_on(cla)


            else:
                # 사냥터로 이동
                jadong_in_spot_go(cla, where)



        # 자동 사냥터 맞는지...

        # 맞다면 오토사냥 중인지...

        # 지정한 자동 사냥터 아니라면 이동하기



    except Exception as e:
        print(e)
        return 0


def jadong_in_spot_check(cla, where):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check

    try:

        # where = "자동_송별의뜰"

        print("jadong_in_spot_check", where)

        if "_" in where:
            spot_ = where.split("_")
        print("spot_", spot_)

        same_ = False
        title_ = "none"

        file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_nooia.txt"

        with open(file_path, "r", encoding='UTF8') as file:
            read_list = file.read().splitlines()
            # print("read_list", read_list)

        for i in range(len(read_list)):
            result_spot = read_list[i].split("_")
            # print("result_spot", result_spot)
            if spot_[1] == result_spot[0]:
                spot_name = result_spot[1]
                same_ = True
                title_ = "nooia"

        if same_ == False:
            file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_sea.txt"

            with open(file_path, "r", encoding='UTF8') as file:
                read_list = file.read().splitlines()
                # print("read_list", read_list)

            for i in range(len(read_list)):
                result_spot = read_list[i].split("_")
                # print("result_spot", result_spot)
                if spot_[1] == result_spot[0]:
                    spot_name = result_spot[1]
                    title_ = "sea"

        spot_true = False


        # 절전일때
        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\juljun\\juljun_ing.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 400, 600, 600, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_juljun_list\\" + str(spot_name) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(100, 920, 200, 980, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("juljun_jadong_spot", spot_name)
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

                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_out_list\\" + str(spot_name) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 90, 200, 130, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("out_jadong_spot", spot_name)
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
                                # 바로 사냥터 진입하기
                                in_spot = True
                                click_pos_2(45, 105, cla)
                                time.sleep(1)
                                for i in range(10):
                                    result_out = out_check(cla)
                                    if result_out == True:
                                        break
                                    time.sleep(1)


        # 자동 사냥터 맞는지...

        # 맞다면 오토사냥 중인지...

        # 지정한 자동 사냥터 아니라면 이동하기

        return spot_true

    except Exception as e:
        print(e)
        return 0

def jadong_in_spot_go(cla, where):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2
    from action import out_check, clean_screen

    try:

        # where = "자동_송별의뜰"

        print("jadong_in_spot_go", where)

        if "_" in where:
            spot_ = where.split("_")
        print("spot_", spot_)

        same_ = False
        title_ = "none"

        file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_nooia.txt"

        with open(file_path, "r", encoding='UTF8') as file:
            read_list = file.read().splitlines()
            # print("read_list", read_list)

        for i in range(len(read_list)):
            result_spot = read_list[i].split("_")
            # print("result_spot", result_spot)
            if spot_[1] == result_spot[0]:
                spot_name = result_spot[1]
                spot_second_list = result_spot[2]
                same_ = True
                title_ = "nooia"

        if same_ == False:
            file_path = "C:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_list_sea.txt"

            with open(file_path, "r", encoding='UTF8') as file:
                read_list = file.read().splitlines()
                # print("read_list", read_list)

            for i in range(len(read_list)):
                result_spot = read_list[i].split("_")
                # print("result_spot", result_spot)
                if spot_[1] == result_spot[0]:
                    spot_name = result_spot[1]
                    spot_second_list = result_spot[2]
                    title_ = "sea"

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

        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_out_list\\" + str(spot_name) + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 90, 200, 130, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_jadong_spot", spot_name)

        else:

            in_spot = False
            in_spot_count = 0
            while in_spot is False:
                in_spot_count += 1
                if in_spot_count > 6:
                    in_spot = True

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_worldmap.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(780, 30, 900, 90, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("worldmap")

                    # 큰 타이틀 맵 클릭
                    if title_ == "nooia":
                        for i in range(10):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\nooia.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 60, 170, 105, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\sea.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 60, 170, 105, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    for c in range(10):
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\nooia_click.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(50, 95, 170, 160, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                        time.sleep(0.5)
                            time.sleep(0.5)
                    elif title_ == "sea":
                        for i in range(10):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\sea.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 60, 170, 105, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\nooia.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 60, 170, 105, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    for c in range(10):
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\sea_click.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(50, 95, 170, 160, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                        time.sleep(0.5)
                            time.sleep(0.5)
                    # 두번째 타이틀 맵 클릭하기 전 정리
                    for i in range(15):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\worldmap_up.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 100, 280, 1040, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("worldmap_up", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                        time.sleep(0.5)
                    # 두번째 타이틀 맵 및 지정한 사냥터 클릭
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\confirm_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(480, 620, 640, 670, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break

                        else:

                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\worldmap_list\\" + str(spot_name) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 90, 260, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                time.sleep(0.5)
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\worldmap_list_clicked\\" + str(spot_name) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(720, 90, 900, 145, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("jadong_spot_clicked", spot_name)
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\jadong_soongan_move2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(795, 980, 945, 1025, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jadong_soongan_move2", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\worldmap_list\\" + str(
                                        spot_name) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 90, 260, 1040, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jadong_spot", spot_name)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\jadong\\worldmap_second_list\\" + str(spot_second_list) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(60, 90, 260, 1040, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("second_jadong_spot", spot_name)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                    # 현장 도착하는지 파악
                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            in_spot = True
                            break
                        time.sleep(1)
                else:
                    clean_screen(cla)
                    click_pos_2(140, 140, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_worldmap.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 30, 900, 90, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0
