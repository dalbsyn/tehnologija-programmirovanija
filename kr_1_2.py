class Course:
    def __init__(self, title, credits):
        self.__title = title
        self.__credits = credits

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_credits(self):
        return self.__credits

    def set_credits(self, credits):
        self.__credits = credits


class OnlineCourse(Course):
    def start_video_lecture(self):
        print("Видео лекция началась")

    def get_course_info(self):
        print(f"Информация по онлайн курсу: {self.get_title()}, Кредиты: {self.get_credits()}")


class OfflineCourse(Course):
    def schedule_classroom(self):
        print("Расписание готово")

    def get_course_info(self):
        print(f"Информация по оффлайн курсу: {self.get_title()}, Кредиты: {self.get_credits()}")




