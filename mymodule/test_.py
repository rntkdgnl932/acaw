import time

import requests
import json
# import os
import sys
sys.path.append('C:/nightcrow/mymodule')

import variable as v_


def go_test():
    from function import imgs_set_, click_pos_reg, imgs_set, text_check_get, int_put_, text_check_get_3, click_pos_2, drag_pos
    from schedule import myQuest_play_check
    from potion import my_potion_check, buy_potion, grow_jangbi_check
    from dead_die import dead_die_start, boohwal
    from get_item import get_item_start
    from action import bag_open

    import numpy as np
    import pyautogui
    import cv2

    cla = "one"

    if cla == 'one':
        plus = 0
    if cla == 'two':
        plus = 960

    print("여긴 테스트")

    # grow_jangbi_check(cla)

    full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\boonhae_title.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(690, 310, 760, 360, cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("boonhae_title", imgs_)

        full_path = "c:\\acaw\\my_acaw\\imgs\\get_item\\daily_confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 600, 660, 660, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("daily_confirm_1", imgs_)


    # potion_ = text_check_get(750, 482, 785, 495, cla)
    # print("앞4자리 potion_?", potion_)
    #
    # for i in range(5):
    #     potion_ = text_check_get(750, 482, 777 + i, 495, cla)
    #     print("<< " + str(777+i) + " >>")
    #     print("앞4자리 potion_?", potion_)

    # full_path = "c:\\acaw\\my_acaw\\imgs\\jadong\\auto_on.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(850, 900, 940, 940, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("auto_on", imgs_)
    # else:
    #     print("auto_on이 아니다.")
    #
    # full_path = "c:\\acaw\\my_acaw\\imgs\\jadong\\auto_off.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(850, 900, 940, 940, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("auto_off", imgs_)
    # else:
    #     print("auto_off 아니다.")
    #
    # full_path = "c:\\acaw\\my_acaw\\imgs\\dead_die\\no_chance_boohwal.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(120, 600, 180, 640, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print(cla, "이제 그만 죽도록 안전한곳에 자사 보내자")
    # else:
    #     print("아직아직아직아직아직아직아직아직")
    #
    # full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(150, 80, 680, 110, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("컬렉션 포인트 있다.", imgs_)

    # get_item_start(cla)

    # # 컬렉션 포인트
    # full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(850, 80, 880, 110, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("컬렉션 포인트 있다.", imgs_)
    # else:
    #     print("컬렉션 포인트 없다.")
    #
    # # 거래소 포인트
    # full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(765, 130, 795, 155, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("거래소 포인트 있다.", imgs_)
    # else:
    #     print("거래소 포인트 없다.")
    #
    # # 출석 포인트
    # full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(725, 180, 750, 210, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("출석 포인트 있다.", imgs_)
    # else:
    #     print("출석 포인트 없다.")
    #
    # # 길드 포인트
    # full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(765, 180, 795, 210, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("길드 포인트 있다.", imgs_)
    # else:
    #     print("길드 포인트 없다.")
    #
    # # 우편 포인트
    # full_path = "c:\\acaw\\my_acaw\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(895, 180, 925, 210, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("우편 포인트 있다.", imgs_)
    # else:
    #     print("우편 포인트 없다.")




    # potion_ = text_check_get(733, 1004, 758, 1016, cla)
    # print("전체4자리 potion_?", potion_)
    # potion_bool = potion_.isdigit()
    # if potion_bool == True:
    #     print("potion_[0]", potion_[0])
    #     if potion_[0] == "0":
    #         potion_ = "1" + potion_
    #         print("potion_ = '1' + potion_", potion_)
    #
    # potion_ = text_check_get(730, 1004, 759, 1016, cla)
    # print("전체4자리 potion_2?", potion_)
    #
    # potion_ = text_check_get(730, 1004, 752, 1016, cla)
    # print("앞3자리 potion_?", potion_)
    #
    # potion_ = text_check_get(738, 1004, 759, 1016, cla)
    # print("뒷3자리 potion_??", potion_)





    # full_path = "c:\\nightcrow\\imgs\\potion\\random_move.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("already_in___1", imgs_)
    #
    #     if cla == "one":
    #         potion_ = text_check_get(imgs_.x - 10, imgs_.y + 10, imgs_.x + 30, imgs_.y + 30, cla)
    #     if cla == "two":
    #         potion_ = text_check_get(imgs_.x - 10 - 960, imgs_.y + 10, imgs_.x + 30 - 960, imgs_.y + 30, cla)
    #     print("how many 1?", potion_)
    #     print("int_put_(potion_) 1?", int(int_put_(potion_)))
    #
    # full_path = "c:\\nightcrow\\imgs\\potion\\maul_move_.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(680, 110, 920, 1000, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("already_in___2", imgs_)
    #
    #     if cla == "one":
    #         potion_ = text_check_get(imgs_.x - 10, imgs_.y + 10, imgs_.x + 30, imgs_.y + 30, cla)
    #     if cla == "two":
    #         potion_ = text_check_get(imgs_.x - 10 - 960, imgs_.y + 10, imgs_.x + 30 - 960, imgs_.y + 30, cla)
    #     print("how many 2?", potion_)
    #     print("int_put_(potion_) 2?", int(int_put_(potion_)))


    # for z in range(3):
    #     last_x = 0
    #     last_y = 0
    #     print("z ? ", z)
    #     if z != 0:
    #         pic_ = "talgut_" + str(z)
    #         full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\" + pic_ + ".PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         for i in pyautogui.locateAllOnScreen(img, region=(680 + plus, 90, 40, 170), confidence=0.7):
    #             last_x = i.left
    #             last_y = i.top
    #             print("last_x", last_x)
    #             print("last_y", last_y)
    #         if last_x != 0:
    #             print("얏호")

    # click_pos_2(700, 110, cla)
    #
    # time.sleep(0.5)
    #
    # full_path = "c:\\nightcrow\\imgs\\grow\\grow_1\\no_talgut_1.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(365, 85, 450, 115, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("no_talgut_1", imgs_)
####################################################################
    # full_path = "c:\\nightcrow\\imgs\\potion\\out_potion.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(700, 950, 760, 1030, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("화면에 물약 존재한다", imgs_)
    # 
    #     potion_ = text_check_get(730, 1004, 752, 1016, cla)
    #     print("처음3자리 potion_?", potion_)
    #     if len(potion_) != 0:
    # 
    #         if " " in potion_:
    #             potion_ = potion_.replace(' ', '')
    # 
    #             print("!!!!!! ['   '] !!!!!!!", potion_)
    # 
    #         if "|" in potion_:
    #             potion_ = potion_.replace('|', '1')
    # 
    #             print("!!!!!!![   |   ]!!!!!!!!!!!", potion_)
    # 
    #         if "B" in potion_:
    #             potion_ = potion_.replace('B', '8')
    # 
    #             print("!!!!!!!!![  B  ]!!!!!!!!!!!!!", potion_)
    # 
    #         potion = int_put_(potion_)
    #         potion_bloon = potion.isdigit()
    #         if potion_bloon == True:
    #             potion = int(potion)
    #             print("potion?", potion)
    #         else:
    #             print("potion => 숫자 아님")
    #     # else:
    # 
    #     potion_ = text_check_get(738, 1004, 759, 1016, cla)
    #     print("뒷3자리 potion_?", potion_)
    #     if len(potion_) != 0:
    # 
    #         if " " in potion_:
    #             potion_ = potion_.replace(' ', '')
    # 
    #             print("!!!!!! ['   '] !!!!!!!", potion_)
    # 
    #         if "|" in potion_:
    #             potion_ = potion_.replace('|', '1')
    # 
    #             print("!!!!!!![   |   ]!!!!!!!!!!!", potion_)
    # 
    #         if "B" in potion_:
    #             potion_ = potion_.replace('B', '8')
    # 
    #             print("!!!!!!!!![  B  ]!!!!!!!!!!!!!", potion_)
    #         potion = int_put_(potion_)
    #         potion_bloon = potion.isdigit()
    #         if potion_bloon == True:
    #             potion = int(potion)
    #             print("potion?", potion)
    #         else:
    #             print("potion => 숫자 아님")
    # 
    #     potion_ = text_check_get(730, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_?", potion_)
    #     if len(potion_) != 0:
    # 
    #         if " " in potion_:
    #             potion_ = potion_.replace(' ', '')
    # 
    #             print("!!!!!! ['   '] !!!!!!!", potion_)
    # 
    #         if "|" in potion_:
    #             potion_ = potion_.replace('|', '1')
    # 
    #             print("!!!!!!![   |   ]!!!!!!!!!!!", potion_)
    # 
    #         if "B" in potion_:
    #             potion_ = potion_.replace('B', '8')
    # 
    #             print("!!!!!!!!![  B  ]!!!!!!!!!!!!!", potion_)
    #         potion = int_put_(potion_)
    #         potion_bloon = potion.isdigit()
    #         if potion_bloon == True:
    #             potion = int(potion)
    #             print("potion?", potion)
    #         else:
    #             print("potion => 숫자 아님")
    #     potion_ = text_check_get(731, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_2?", potion_)
    #     potion_ = text_check_get(732, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_3?", potion_)
    #     potion_ = text_check_get(733, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_4?", potion_)
    #     potion_ = text_check_get(734, 1004, 758, 1016, cla)
    #     print("전체4자리 potion_5?", potion_)
    ###########################################################################
    # print("<< point 파악 >>")
    #
    # if cla == 'one':
    #     plus = 0
    # if cla == 'two':
    #     plus = 960
    # count_ = 0
    # full_path = "c:\\nightcrow\\imgs\\check\\point.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for i in pyautogui.locateAllOnScreen(img, region=(0 + plus, 0, 960, 1030), confidence=0.75):
    #     count_ += 1
    #
    #     last_x = i.left
    #     last_y = i.top
    #     print("point 넘버 : ", count_)
    #     print("last_x", last_x)
    #     print("last_y", last_y)




