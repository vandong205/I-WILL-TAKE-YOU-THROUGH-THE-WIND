transform fade_black(time=0.5):
    alpha 0.0
    linear time alpha 1.0
    pause time
    linear time alpha 0.0

screen black_transition(time=0.5):
    zorder 999
    add Solid("#000") at fade_black(time)
