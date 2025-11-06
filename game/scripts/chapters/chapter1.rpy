transform fade_out:
    linear 0.4 alpha 0.0
# --- Màn hình tìm đồ trong phòng ---
screen bedroom_find_objects():
    on "show" action Show("quest_list_ui")
    python:
        queststack.add(QUESTS["bedroom"])
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
        on "hide" action Hide("quest_list_ui")
        timer 1.0 action [Return(True), Function(lambda: queststack.clear())]
transform scroll_bg(speed=5.0, startxpos=0):
    xpos startxpos
    ypos 0.2
    linear speed xpos startxpos-1
    repeat
transform normal_run:
    xpos 0.2 ypos 0.71
    zoom 0.3
transform jump_up_down:
    xpos 0.2 ypos 0.71
    zoom 0.3
    # 1. Nhảy lên (từ đất)
    easeout 0.2 ypos 0.60

    # 2. Lên gần đỉnh
    linear 0.1 ypos 0.57
    linear 0.1 ypos 0.55

    # 3. Giữ phần đỉnh (vẫn di chuyển nhẹ để vòng cung tự nhiên)
    linear 0.05 ypos 0.55
    linear 0.05 ypos 0.555

    # 4. Rơi xuống (tăng tốc dần)
    linear 0.1 ypos 0.57
    easein 0.2 ypos 0.71
screen street_jumping_minigame():
    default jumping = False
    add "street_side_view" at scroll_bg(speed=8.0, startxpos=0.0) 
    add "street_side_view" at scroll_bg(speed=8.0, startxpos=1.0)
    if jumping :
        add "ln_jump" at jump_up_down     
    else:
        add "ln_run" at normal_run
    key "K_SPACE" action [
        SetScreenVariable("jumping", True), 
    ]
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
    with dissolve
    window show
    show bg street_run
    LamNguyet "Hy vọng hôm nay không tắc đường…"
    scene lightblue
    window hide
    call screen street_jumping_minigame
    window show
    "pause"
    return