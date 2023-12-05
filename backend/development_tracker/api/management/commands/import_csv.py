import csv

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from courses.models import Course, CourseDefaultSkill
from skills.models import Skill
from selections.models import Selection, SelectionSkill
from development_tracker.settings import BASE_DIR


class Command(BaseCommand):
    help = "Импорт данных в таблицы из csv файлов"

    def handle(self, *args, **kwargs):
        self.courses_upload()
        self.skills_upload()
        self.selections_upload()
        self.course_skill_upload()
        self.selection_skill_upload()

    def courses_upload(self):
        with open(
            str(BASE_DIR) + "/data/" + "courses.csv", encoding="utf-8"
        ) as r_file:
            reader = csv.DictReader(r_file)
            csv_data = []
            for row in reader:
                course = Course(
                    id=row.get("id"),
                    name=row.get("name"),
                    image=row.get("image"),
                    url=row.get("url"),
                )
                csv_data.append(course)
            try:
                Course.objects.bulk_create(csv_data)
                print(f"Добавлены записи в таблицу {Course.__name__}")
            except IntegrityError:
                print(f"Данные модели {Course.__name__} уже импортированы")

    def skills_upload(self):
        with open(
            str(BASE_DIR) + "/data/" + "skills.csv", encoding="utf-8"
        ) as r_file:
            reader = csv.DictReader(r_file)
            csv_data = []
            for row in reader:
                skill = Skill(
                    id=row.get("id"), name=row.get("name"), editable=False
                )
                csv_data.append(skill)
            try:
                Skill.objects.bulk_create(csv_data)
                print(f"Добавлены записи в таблицу {Skill.__name__}")
            except IntegrityError:
                print(f"Данные модели {Skill.__name__} уже импортированы")

    def selections_upload(self):
        with open(
            str(BASE_DIR) + "/data/" + "selections.csv", encoding="utf-8"
        ) as r_file:
            reader = csv.DictReader(r_file)
            csv_data = []
            for row in reader:
                selection = Selection(id=row.get("id"), name=row.get("name"))
                csv_data.append(selection)
            try:
                Selection.objects.bulk_create(csv_data)
                print(f"Добавлены записи в таблицу {Selection.__name__}")
            except IntegrityError:
                print(f"Данные модели {Selection.__name__} уже импортированы")

    def course_skill_upload(self):
        with open(
            str(BASE_DIR) + "/data/" + "course_skill.csv", encoding="utf-8"
        ) as r_file:
            reader = csv.DictReader(r_file)
            csv_data = []
            for row in reader:
                course_skill = CourseDefaultSkill(
                    id=row.get("id"),
                    course=Course(id=row.get("course")),
                    skill=Skill(id=row.get("skill")),
                )
                csv_data.append(course_skill)
            try:
                CourseDefaultSkill.objects.bulk_create(csv_data)
                print(
                    f"Добавлены записи в таблицу {CourseDefaultSkill.__name__}"
                )
            except IntegrityError:
                print(
                    f"Данные модели {CourseDefaultSkill.__name__} уже импортированы"
                )

    def selection_skill_upload(self):
        with open(
            str(BASE_DIR) + "/data/" + "selection_skill.csv", encoding="utf-8"
        ) as r_file:
            reader = csv.DictReader(r_file)
            csv_data = []
            for row in reader:
                selection_skill = SelectionSkill(
                    id=row.get("id"),
                    selection=Selection(id=row.get("selection")),
                    skill=Skill(id=row.get("skill")),
                )
                csv_data.append(selection_skill)
            try:
                SelectionSkill.objects.bulk_create(csv_data)
                print(f"Добавлены записи в таблицу {SelectionSkill.__name__}")
            except IntegrityError:
                print(
                    f"Данные модели {SelectionSkill.__name__} уже импортированы"
                )
