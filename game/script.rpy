
define LamNguyet = Character("Lâm nguyệt")
define config.default_text_cps = 10
# The game starts here.
label start:
    "Reng reng rengggg ... " 
    LamNguyet"Cái gì vậy ~~ " 
    LamNguyet"Để người ta còn ngủ chứ .. "
    LamNguyet"Mà khoan đã..."
    show screen custom_bbspeech("serius", "Dậy đi, muộn rồi!", textsize=30, textcolor="#202020", posx=0.5, posy=0.5)
    pause 2
    hide screen custom_bbspeechw with fade
    return
