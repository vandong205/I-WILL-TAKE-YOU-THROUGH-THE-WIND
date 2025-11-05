transform fade_out:
    linear 0.4 alpha 0.0
# --- Màn hình tìm đồ trong phòng ---
screen bedroom_find_objects():
    default quests = [q for q in QUESTS["bedroom"]]

    add "bg bedroom" xpos -50 ypos -23

    # --- 1. Đồng hồ ---
    if not is_quest_done(1, "bedroom"):
        imagebutton:
            idle "clock"
            xpos 300
            ypos 200
            focus_mask True
            action Function(set_quest_done, 1, "bedroom")
    else:
        add "clock" xpos 300 ypos 200 at fade_out

    # --- 2. Chăn gối ---
    if not is_quest_done(2, "bedroom"):
        imagebutton:
            idle "blanket"
            xpos 0.24
            ypos 0.47
            focus_mask True
            action Function(set_quest_done, 2, "bedroom")
    else:
        add "blanket" xpos 0.24 ypos 0.47 at fade_out

    # --- 3. Áo ---
    if not is_quest_done(3, "bedroom"):
        imagebutton:
            idle "shirt"
            xpos 0.36
            ypos 0.016
            focus_mask True
            action Function(set_quest_done, 3, "bedroom")
    else:
        add "shirt" xpos 0.36 ypos 0.016 at fade_out
    if all_quests_done("bedroom"):
        timer 1.0 action Return(True)

label chapter1:
    "Reng reng rengggg ... "
    LamNguyet "Cái gì vậy ~~"
    LamNguyet "Để người ta còn ngủ chứ .. "
    LamNguyet "Mà khoan đã..."

    show screen custom_bbspeech("serius", "Hôm nay mình phải đi phỏng vấn mà !",
        textsize=30, textcolor="#202020", posx=0.5, posy=0.4, padx=200, pady=200)
    pause 2.0
    hide screen custom_bbspeech
    # 1. CẢNH PHÒNG NGỦ RỘNG
    scene bg bedroom_full with dissolve
    window hide
    LamNguyet "Mình sẽ muộn mất! Nhanh nhanh dọn đồ đạc thôi"

    # 2. CHUYỂN SANG MÀN ĐEN (tránh flash)
    scene black with dissolve

    # 3. HIỆN MÀN TÌM ĐỒ (nền + đồ cùng lúc, mượt mà!)
    call screen bedroom_find_objects
    # 4. QUAY LẠI CẢNH PHÒNG NGỦ RỘNG
    scene bg bedroom with dissolve
    window show
    LamNguyet "Xong!Mau đi đến địa điểm phỏng vấn!!"
    show screen quest_screen
    "pause"
    return