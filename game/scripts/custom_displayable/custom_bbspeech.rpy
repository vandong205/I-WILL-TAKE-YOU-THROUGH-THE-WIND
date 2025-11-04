screen custom_bbspeech(type, context,textsize=28,textcolor="#000000", posx=0.5, posy=0.5,padx=100,pady=100):
    # chọn hình theo type
    $ bubble_image = "gui/bubble.png"
    if type == "serius":
        $ bubble_image = "gui/bubble_background/serius_speech.png"
    frame:
        background Frame(bubble_image, 12, 12)
        xanchor 0.5
        yanchor 0.5
        xpos posx
        ypos posy
        padding (padx,pady)
        text context:
            color textcolor
            size textsize
            xalign 0.5
            yalign 0.5
            layout "subtitle"  # cho phép text tự xuống dòng mềm
            line_spacing 3
