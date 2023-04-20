class ClusterJewel:
    def __init__(self, jewel_data):
        self.max_skills = jewel_data.get("max_skills")
        self.min_skills = jewel_data.get("min_skills")
        self.name = jewel_data.get("name")
        self.notable_indices = jewel_data.get("notable_indices")
        self.passive_skills = [
            PassiveSkill(skill_data) for skill_data in jewel_data.get("passive_skills", [])
        ]


class PassiveSkill:
    def __init__(self, skill_data):
        self.id = skill_data.get("id")
        self.name = skill_data.get("name")
        self.stats = skill_data.get("stats")
        self.tag = skill_data.get("tag")
