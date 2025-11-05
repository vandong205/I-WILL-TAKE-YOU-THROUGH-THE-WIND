init -10 python: 
    class QuestStack:
        def __init__(self, quests=None):
            self.quests = quests or []
        def add(self, quest):
            if isinstance(quest, list):
                for q in quest:
                    if not any(existing.id == q.id for existing in self.quests):
                                self.quests.append(q)
            else:
                if not any(q.id == quest.id for q in self.quests):
                    self.quests.append(quest)

        def clear(self, qid=None):
            if qid is None:
                self.quests.clear()
            else:
                self.quests = [q for q in self.quests if q.id != qid]
        def all_done(self):
            return all(q.isDone for q in self.quests)
default queststack = QuestStack()
style quest_frame:
    background Frame("#0008", 15, 15)  # màu đen trong suốt, bo tròn
    padding (15, 15)
    xalign 0.02
    yalign 0.1
    xmaximum 400
screen quest_list_ui():
    tag quest_ui  
    frame:
        style "quest_frame"
        vbox:
            spacing 10
            text "📜 Danh sách nhiệm vụ" size 28 color "#ffffff" xalign 0.5

            null height 10

            # Duyệt toàn bộ quest trong queststack
            for q in queststack.quests:
                hbox:
                    spacing 10
                    xmaximum 380
                    text "[q.text]" size 22 color "#ffffff" xalign 0.0
                    if q.isDone:
                        text "✅" size 22 color "#00ff00" xalign 1.0
                    else:
                        text "⬜" size 22 color "#aaaaaa" xalign 1.0




