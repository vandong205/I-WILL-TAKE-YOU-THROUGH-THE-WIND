# =====================================================
# QUEST LIST SYSTEM
# =====================================================

# Đây là danh sách nhiệm vụ mẫu.
# Mỗi nhiệm vụ là 1 dict có 2 trường: name, done
default quest_list = [
    {"name": "Đến trường phỏng vấn", "done": False},
    {"name": "Gặp Lam Nguyệt ở sảnh chính", "done": True},
    {"name": "Nộp hồ sơ cho giám khảo", "done": False},
]

# =====================================================
# SCREEN HIỂN THỊ DANH SÁCH NHIỆM VỤ
# =====================================================
screen quest_screen():

    tag questlist  # đảm bảo chỉ có 1 màn hình danh sách nhiệm vụ cùng lúc

    modal False  # không khóa các hành động khác

    frame:
        align (0.5, 0.5)
        xsize 600
        ysize 400
        background Frame("gui/frame.png", 12, 12)

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5

            text "📜 Danh Sách Nhiệm Vụ" size 32 color "#ffd700" xalign 0.5

            viewport:
                draggable True
                mousewheel True
                xmaximum 560
                ymaximum 280

                vbox:
                    spacing 6
                    for i, quest in enumerate(quest_list):
                        hbox:
                            spacing 15
                            text quest["name"] size 24 color "#ffffff"
                            if quest["done"]:
                                text "✅" size 28 color "#00ff88"
                            else:
                                textbutton "Hoàn thành" action SetDict(quest_list[i], "done", True)

            textbutton "Đóng" action Hide("quest_screen") xalign 0.5
