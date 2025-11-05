init -10 python:
    class Quest:
        def __init__(self,id,content,isdone):
            self.id = id
            self.text = content
            self.isDone = isdone
    QUESTS = {
    "bedroom": [
        Quest(1, "Tắt đồng hồ", False),
        Quest(2, "Dọn chăn gối", False),
        Quest(3, "Mặc áo", False)
    ]
    }
    # --- Lấy quest theo ID ---
    def get_quest_by_id(qid, area="bedroom"):
        for q in QUESTS.get(area, []):
            if q.id == qid:
                return q
        return None

    # --- Đánh dấu hoàn thành ---
    def set_quest_done(qid, area="bedroom"):
        q = get_quest_by_id(qid, area)
        if q:
            q.isDone = True

    # --- Kiểm tra trạng thái ---
    def is_quest_done(qid, area="bedroom"):
        q = get_quest_by_id(qid, area)
        return q.isDone if q else True
    def all_quests_done(area="bedroom"):
        for q in QUESTS.get(area, []):
            if not q.isDone:
                return False
        return True
