import time
# import os
import sys


import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


def sub_quest_start(cla):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("sub_quest_start")
        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("18_1")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)
        #     time.sleep(1)
        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\18\\18_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(70, 670, 300, 770, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("18_1")
        #     click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)
        return 0

def request_start(cla):
    import random
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import bag_open, menu_open, auto_on, out_check
    from potion import my_potion_check, buy_potion
    from dead_die import dead_die_start
    from schedule import myQuest_play_add

    try:
        print("request_start")

        dead_die_start(cla, "의뢰퀘스트")

        if v_.request_go == False:

            request_start = False
            request_start_count = 0
            while request_start is False:
                request_start_count += 1
                if request_start_count > 7:
                    request_start = True

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_quest.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 30, 940, 670, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("quest")

                    click_pos_2(220, 105, cla)
                    time.sleep(0.1)
                    click_pos_2(220, 105, cla)
                    time.sleep(0.1)

                    not_have_request = False

                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\not_have_request.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(370, 530, 580, 600, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            not_have_request = True
                            break
                        else:
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\soongan_move.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(780, 960, 940, 1015, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\get_bosang.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 960, 940, 1015, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    request_complete_check(cla)
                                    break

                        time.sleep(0.4)

                    if not_have_request == True:
                        print("가방 확인해서 의뢰 퀘스트 있는지 확인 후 있다면 의뢰 받기")

                        result_request = have_request(cla)

                        if result_request == True:

                            for i in range(10):
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\request.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(690, 355, 940, 670, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    for h in range(10):
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\request_have_confirm.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(780, 940, 940, 1000, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            break
                                        else:
                                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\request.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(690, 355, 940, 670, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.1)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.1)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                time.sleep(0.1)
                                        time.sleep(0.3)
                                else:
                                    break
                                time.sleep(0.5)
                        else:
                            request_start = True
                            # add 완료
                            myQuest_play_add(cla, "의뢰퀘스트")
                    else:
                        for i in range(10):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\soongan_move_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 620, 640, 670, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                for o in range(10):
                                    result_out = out_check(cla)
                                    if result_out == True:
                                        request_start = True
                                        v_.request_go = True
                                        break
                                    time.sleep(0.5)


                                break
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\soongan_move.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(780, 960, 940, 1015, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)

                                    # 여기에 티켓 부족 넣기
                                    ticket_enough = True
                                    support_ = True
                                    for t in range(10):
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\ticket_not_enough.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(360, 120, 600, 200, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("티켓 부족...")
                                            ticket_enough = False
                                            break
                                        else:
                                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\do_not_support.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(360, 120, 600, 200, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                print("지원하지 않음...")
                                                support_ = False
                                                break
                                        time.sleep(0.1)
                                    if ticket_enough == False or support_ == False:

                                        if ticket_enough == False:
                                            for t in range(10):
                                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\ticket_not_enough.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(360, 120, 600, 200, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("의뢰 대기 1")
                                                else:
                                                    break
                                                time.sleep(0.5)
                                        elif support_ == False:
                                            for t in range(10):
                                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\do_not_support.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(360, 120, 600, 200, cla, img, 0.8)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("의뢰 대기 2")
                                                else:
                                                    break
                                                time.sleep(0.5)


                                        for t in range(10):
                                            # 확인 넣기
                                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\soongan_move_confirm.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(480, 620, 640, 670, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                                break
                                            else:
                                                click_pos_2(530, 990, cla)
                                            time.sleep(0.5)



                            time.sleep(0.5)

                else:
                    ran_result = random.randint(1, 5)

                    x_reg = 330 + (int(ran_result) * 50)

                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\random_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 590, 620, 660, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(x_reg, 625, cla)

                    else:
                        menu_open(cla)
                        click_pos_2(860, 60, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 30, 940, 670, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.2)
        else:
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\tuto\\quest_clear_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(640, 70, 690, 300, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("go_quest", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                # 380, 430, 480, 530, 580
                ran_result = random.randint(1, 5)

                x_reg = 330 + (int(ran_result) * 50)



                for i in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\random_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 590, 410, 660, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)

                for i in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\random_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 590, 620, 660, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:

                        click_pos_2(x_reg, 625, cla)

                        time.sleep(0.2)

                        slot_enough = True


                        for e in range(10):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\slot_not_enough.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(360, 120, 580, 200, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("슬롯 부족...")
                                slot_enough = False
                                break
                            else:
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\slot_not_enough2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(360, 120, 580, 200, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("무게 부족...")
                                    slot_enough = False
                                    break
                            time.sleep(0.1)

                        if slot_enough == False:
                            # 물약 사러 가기
                            buy_potion(cla)
                            break
                        else:
                            time.sleep(0.3)
                            click_pos_2(x_reg, 625 + 100, cla)
                            v_.request_go = False


                    else:
                        break
                    time.sleep(0.5)
            else:

                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\potion\\maul_.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 70, 150, 150, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    v_.request_go_count = 0
                    v_.request_go = False
                else:

                    v_.request_go_count += 1

                    if v_.request_go_count > 300:
                        v_.request_go_count = 0
                        v_.request_go = False

                    else:
                        my_potion_check(cla)
                        auto_on(cla)


    except Exception as e:
        print(e)
        return 0

def have_request(cla):
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import bag_open

    try:
        print("request_start")

        to_heve = False

        bag_open(cla)

        click_pos_2(875, 345, cla)

        for i in range(10):
            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\request.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(690, 355, 940, 670, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("request", imgs_)
                to_heve = True
                break
            else:
                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\drag_stop.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 355, 940, 670, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("drag_stop", imgs_)
                    break
                else:
                    drag_pos(820, 620, 820, 520, cla)
            time.sleep(0.5)

        return to_heve
    except Exception as e:
        print(e)
        return 0

def request_complete_check(cla):
    import random
    import numpy as np
    import cv2
    from function_acaw import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    from action import bag_open, menu_open
    from potion import buy_potion
    from schedule import myQuest_play_add

    try:
        print("request_complete_check")

        request_start = False
        request_start_count = 0
        while request_start is False:
            request_start_count += 1
            if request_start_count > 7:
                request_start = True

            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(690, 30, 940, 670, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest")

                click_pos_2(220, 105, cla)
                time.sleep(0.1)
                click_pos_2(220, 105, cla)
                time.sleep(0.1)

                not_have_request = False

                for i in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\not_have_request.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 530, 580, 600, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        not_have_request = True
                        break
                    else:
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\get_bosang.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 960, 940, 1015, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            break

                    time.sleep(0.4)

                if not_have_request == True:
                    print("가방 확인해서 의뢰 퀘스트 있는지 확인 후 있다면 의뢰 받기")

                    result_request = have_request(cla)

                    if result_request == True:

                        for i in range(10):
                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\request.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 355, 940, 670, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                for h in range(10):
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\request_have_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(780, 940, 940, 1000, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                    else:
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\request.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(690, 355, 940, 670, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(0.1)
                                    time.sleep(0.3)
                            else:
                                break
                            time.sleep(0.5)
                    else:
                        request_start = True
                        # add 완료
                        myQuest_play_add(cla, "의뢰퀘스트")
                else:
                    # 보상받기
                    for i in range(10):
                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\get_bosang.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(780, 960, 940, 1015, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            # 380, 430, 480, 530, 580
                            ran_result = random.randint(1, 5)

                            x_reg = 330 + (int(ran_result) * 50)


                            for r in range(10):
                                full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\random_click.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(340, 590, 410, 660, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    break
                                time.sleep(0.3)

                            full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\random_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(340, 590, 620, 660, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(x_reg, 625, cla)
                                time.sleep(0.1)

                                slot_enough = True

                                for e in range(10):
                                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\slot_not_enough.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(360, 120, 580, 200, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("슬롯 부족...")
                                        slot_enough = False
                                        break
                                    else:
                                        full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\sub_quest\\request\\slot_not_enough2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(360, 120, 580, 200, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("무게 부족...")
                                            slot_enough = False
                                            break
                                    time.sleep(0.1)

                                if slot_enough == False:
                                    # 물약 사러 가기
                                    buy_potion(cla)
                                    request_start = True
                                    break
                                else:
                                    click_pos_2(x_reg, 625 + 100, cla)


                            time.sleep(0.5)
                        else:
                            request_start = True
                            v_.request_go = False
                            break
                        time.sleep(0.3)

            else:
                menu_open(cla)
                click_pos_2(860, 60, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\acaw\\data_acaw\\imgs\\title\\title_quest.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(690, 30, 940, 670, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)




    except Exception as e:
        print(e)
        return 0

