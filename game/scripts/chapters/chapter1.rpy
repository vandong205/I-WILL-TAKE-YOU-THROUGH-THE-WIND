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
    linear speed xpos startxpos - 1.0
    repeat

transform normal_run:
    xpos 0.2 ypos 0.71
    zoom 0.3

transform jump_up_down:
    xpos 0.2 ypos 0.71
    zoom 0.3
    easeout 0.2 ypos 0.60
    linear 0.1 ypos 0.57
    linear 0.1 ypos 0.55
    linear 0.1 ypos 0.55
    linear 0.1 ypos 0.552
    linear 0.1 ypos 0.556
    linear 0.1 ypos 0.560
    linear 0.1 ypos 0.57
    easein 0.2 ypos 0.71

transform run_to_right:
    xpos 0.2 ypos 0.71
    zoom 0.3
    linear 5 xpos 1.0

style timebar:
    xalign 0.5
    yalign 0.05
    xmaximum 600
    ymaximum 20
init python:
    import random

    TARGET_BREAD_COUNT = 20  # số lượng cần nhặt để thắng

    def move_bread(bread_items):
        """Bread di chuyển từ phải sang trái."""
        for item in bread_items:
            item["x"] -= 0.01
            if item["x"] < -0.2:
                item["visible"] = False

    def spawn_bread(bread_items):
        """Sinh bread ngẫu nhiên."""
        if random.random() < 0.5:
            y = 0.75
            if random.random() <0.5:
                y = 0.63
            bread_items.append({
                "x": 1.2,
                "y": y,
                "width": 0.032,
                "height": 0.06,
                "visible": True
            })  

    def delete_bread(bread_items):
        """Xóa các bread không còn hiển thị."""
        bread_items[:] = [i for i in bread_items if i["visible"] and i["x"] > -0.2]
    def check_collect_bread(hero, bread_items, collected_ref):
        """Kiểm tra va chạm giữa hero và bread."""
        hero_left   = hero["x"]
        hero_right  = hero["x"] + hero["width"]
        hero_top    = hero["y"]
        hero_bottom = hero["y"] + hero["height"]

        for item in bread_items:
            if not item["visible"]:
                continue
            item_left   = item["x"]
            item_right  = item["x"] + item["width"]
            item_top    = item["y"]
            item_bottom = item["y"] + item["height"]

            # Kiểm tra giao nhau (AABB collision)
            overlap_x = hero_left < item_right and hero_right > item_left
            overlap_y = hero_top < item_bottom and hero_bottom > item_top

            if overlap_x and overlap_y:
                item["visible"] = False
                renpy.run(SetScreenVariable("collected", renpy.get_screen("street_jumping_minigame").scope["collected"] + 1))

screen street_jumping_minigame():
    default jumping = False
    default game_over = False
    default bread_items = []
    default collected = 0 

    default player = {"x": 0.2, "y": 0.71, "width": 0.072, "height": 0.231}

    # --- NỀN ---
    add "street_side_view" at scroll_bg(speed=8.0, startxpos=0.0)
    add "street_side_view" at scroll_bg(speed=8.0, startxpos=1.0)

    # --- NHÂN VẬT ---
    if not game_over:
        if jumping:
            add "ln_jump" at jump_up_down
            timer 1.1 action SetScreenVariable("jumping", False)
            $ player["y"] = 0.55
        else:
            add "ln_run" at normal_run
            $ player["y"] = 0.71
    else:
        add "ln_run" at run_to_right
        text "🎉 Thu thập đủ bánh mì!" xpos 0.5 ypos 0.1 size 40 color "#0f0" xanchor 0.5
        timer 5.0 action Return()
    # --- Điều khiển ---
    key "mousedown_1" action SetScreenVariable("jumping", True)

    # --- Logic game ---
    if not game_over:
        timer 0.35 repeat True action Function(spawn_bread, bread_items)
        timer 0.03 repeat True action Function(move_bread, bread_items)
        timer 0.03 repeat True action Function(check_collect_bread, player, bread_items, collected)
        timer 0.05 repeat True action Function(delete_bread, bread_items)

        if collected >= TARGET_BREAD_COUNT:
            $ game_over = True
    # --- Hiển thị số lượng ---
    text f"Bánh mì: {collected}/{TARGET_BREAD_COUNT}" xpos 0.05 ypos 0.05 size 30 color "#fff"
    text "Ăn sáng !" xalign 0.5 ypos 0.05 size 30
    # --- Vẽ Bread ---
    if not game_over:
        for item in bread_items:
            if item["visible"]:
                add "bread" xpos item["x"] ypos item["y"] zoom 0.4

    # # --- Debug Collider ---
    # # Vẽ khung nhân vật
    # frame:
    #     background Solid("#00ff0033")  # xanh trong suốt
    #     xpos player["x"] ypos player["y"]
    #     xsize player["width"]
    #     ysize player["height"]

    # # Vẽ collider từng bread
    # for item in bread_items:
    #     if item["visible"]:
    #         frame:
    #             background Solid("#ff000033")  # đỏ trong suốt
    #             xpos item["x"] ypos item["y"]
    #             xsize item["width"]
    #             ysize item["height"]

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
    scene black
    show bg company_entry
    "Tập đoàn Tần Thị"
    hide bg company_entry with dissolve
    show bg interview_table with dissolve
    "pause"
    return