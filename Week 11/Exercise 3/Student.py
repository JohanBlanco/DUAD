class Student:
    def __init__(self, full_name, section, grade_in_spanish, grade_in_english, grade_in_science, grade_in_social_studies):
        self.full_name = full_name
        self.section = section
        self.grade_in_spanish = grade_in_spanish
        self.grade_in_english = grade_in_english
        self.grade_in_science = grade_in_science
        self.grade_in_social_studies = grade_in_social_studies

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def get_average(self):
        total = (
            self.grade_in_spanish
            + self.grade_in_english
            + self.grade_in_science
            + self.grade_in_social_studies
        )
        return total / 4