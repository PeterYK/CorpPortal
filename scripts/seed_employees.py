from portal.models import Team, Employee
from datetime import date

Employee.objects.all().delete()

teams = {t.name: t for t in Team.objects.all()}

employees_data = [
    # Администрация
    {"name": "Александр Волков", "position": "Генеральный директор", "team": "Администрация", "manager": None, "city": "Москва", "birthday": date(1978, 4, 12), "email": "a.volkov@company.ru"},
    {"name": "Елена Соколова", "position": "Финансовый директор", "team": "Администрация", "manager": "Александр Волков", "city": "Москва", "birthday": date(1982, 9, 3), "email": "e.sokolova@company.ru"},
    {"name": "Дмитрий Орлов", "position": "Технический директор", "team": "Администрация", "manager": "Александр Волков", "city": "Москва", "birthday": date(1980, 11, 21), "email": "d.orlov@company.ru"},
    {"name": "Марина Кузнецова", "position": "Главный юрист", "team": "Администрация", "manager": "Александр Волков", "city": "Москва", "birthday": date(1985, 6, 15), "email": "m.kuznetsova@company.ru"},

    # Бухгалтерия
    {"name": "Ольга Новикова", "position": "Главный бухгалтер", "team": "Бухгалтерия", "manager": "Елена Соколова", "city": "Москва", "birthday": date(1988, 2, 8), "email": "o.novikova@company.ru"},
    {"name": "Анна Белова", "position": "Бухгалтер", "team": "Бухгалтерия", "manager": "Елена Соколова", "city": "Москва", "birthday": date(1992, 7, 19), "email": "a.belova@company.ru"},
    {"name": "Сергей Морозов", "position": "Бухгалтер", "team": "Бухгалтерия", "manager": "Елена Соколова", "city": "Москва", "birthday": date(1990, 10, 30), "email": "s.morozov@company.ru"},

    # Юридический отдел
    {"name": "Игорь Лебедев", "position": "Юрист", "team": "Юридический отдел", "manager": "Марина Кузнецова", "city": "Москва", "birthday": date(1991, 3, 5), "email": "i.lebedev@company.ru"},
    {"name": "Татьяна Павлова", "position": "Юрист", "team": "Юридический отдел", "manager": "Марина Кузнецова", "city": "Москва", "birthday": date(1993, 12, 14), "email": "t.pavlova@company.ru"},

    # Лиды технического отдела
    {"name": "Алексей Смирнов", "position": "Лид мобильной разработки", "team": "Технический отдел", "manager": "Дмитрий Орлов", "city": "Москва", "birthday": date(1987, 5, 22), "email": "a.smirnov@company.ru"},
    {"name": "Павел Иванов", "position": "Лид backend-разработки", "team": "Технический отдел", "manager": "Дмитрий Орлов", "city": "Москва", "birthday": date(1986, 8, 9), "email": "p.ivanov@company.ru"},
    {"name": "Наталья Козлова", "position": "Лид frontend-разработки", "team": "Технический отдел", "manager": "Дмитрий Орлов", "city": "Москва", "birthday": date(1989, 1, 17), "email": "n.kozlova@company.ru"},
    {"name": "Екатерина Васильева", "position": "Лид дизайна", "team": "Технический отдел", "manager": "Дмитрий Орлов", "city": "Москва", "birthday": date(1990, 4, 28), "email": "e.vasileva@company.ru"},

    # Мобильная разработка
    {"name": "Иван Петров", "position": "iOS-разработчик", "team": "Мобильная разработка", "manager": "Алексей Смирнов", "city": "Москва", "birthday": date(1995, 6, 11), "email": "i.petrov@company.ru"},
    {"name": "Мария Сидорова", "position": "Android-разработчик", "team": "Мобильная разработка", "manager": "Алексей Смирнов", "city": "Санкт-Петербург", "birthday": date(1996, 9, 23), "email": "m.sidorova@company.ru"},
    {"name": "Артём Кузьмин", "position": "iOS-разработчик", "team": "Мобильная разработка", "manager": "Алексей Смирнов", "city": "Москва", "birthday": date(1994, 2, 4), "email": "a.kuzmin@company.ru"},
    {"name": "Дарья Фёдорова", "position": "Android-разработчик", "team": "Мобильная разработка", "manager": "Алексей Смирнов", "city": "Казань", "birthday": date(1997, 11, 16), "email": "d.fedorova@company.ru"},
    {"name": "Никита Орлов", "position": "iOS-разработчик", "team": "Мобильная разработка", "manager": "Алексей Смирнов", "city": "Москва", "birthday": date(1993, 7, 29), "email": "n.orlov@company.ru"},
    {"name": "София Лебедева", "position": "Android-разработчик", "team": "Мобильная разработка", "manager": "Алексей Смирнов", "city": "Новосибирск", "birthday": date(1998, 1, 7), "email": "s.lebedeva@company.ru"},

    # Backend-разработка
    {"name": "Сергей Волков", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Москва", "birthday": date(1992, 3, 2), "email": "s.volkov@company.ru"},
    {"name": "Алина Морозова", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Москва", "birthday": date(1994, 8, 18), "email": "a.morozova@company.ru"},
    {"name": "Кирилл Новиков", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Санкт-Петербург", "birthday": date(1991, 5, 25), "email": "k.novikov@company.ru"},
    {"name": "Евгения Соколова", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Москва", "birthday": date(1996, 10, 13), "email": "e.sokolova2@company.ru"},
    {"name": "Максим Попов", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Казань", "birthday": date(1993, 12, 9), "email": "m.popov@company.ru"},
    {"name": "Виктория Егорова", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Москва", "birthday": date(1995, 4, 21), "email": "v.egorova@company.ru"},
    {"name": "Андрей Зайцев", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Екатеринбург", "birthday": date(1990, 7, 6), "email": "a.zaitsev@company.ru"},
    {"name": "Полина Ковалёва", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Москва", "birthday": date(1997, 9, 15), "email": "p.kovaleva@company.ru"},
    {"name": "Роман Семёнов", "position": "Backend-разработчик", "team": "Backend-разработка", "manager": "Павел Иванов", "city": "Москва", "birthday": date(1992, 2, 28), "email": "r.semenov@company.ru"},

    # Frontend-разработка
    {"name": "Анна Крылова", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Москва", "birthday": date(1994, 6, 3), "email": "a.krylova@company.ru"},
    {"name": "Дмитрий Белов", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Москва", "birthday": date(1991, 11, 19), "email": "d.belov@company.ru"},
    {"name": "Елизавета Орлова", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Санкт-Петербург", "birthday": date(1996, 3, 27), "email": "e.orlova@company.ru"},
    {"name": "Илья Макаров", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Москва", "birthday": date(1993, 8, 8), "email": "i.makarov@company.ru"},
    {"name": "Ксения Фролова", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Казань", "birthday": date(1998, 1, 14), "email": "k.frolova@company.ru"},
    {"name": "Артём Никитин", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Москва", "birthday": date(1990, 5, 22), "email": "a.nikitin@company.ru"},
    {"name": "Мария Громова", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Новосибирск", "birthday": date(1995, 9, 30), "email": "m.gromova@company.ru"},
    {"name": "Павел Соловьёв", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Москва", "birthday": date(1992, 12, 11), "email": "p.solovyov@company.ru"},
    {"name": "Алина Захарова", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Москва", "birthday": date(1997, 4, 5), "email": "a.zakharova@company.ru"},
    {"name": "Никита Воробьёв", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Екатеринбург", "birthday": date(1994, 7, 17), "email": "n.vorobyov@company.ru"},
    {"name": "Дарья Медведева", "position": "Frontend-разработчик", "team": "Frontend-разработка", "manager": "Наталья Козлова", "city": "Москва", "birthday": date(1996, 10, 26), "email": "d.medvedeva@company.ru"},

    # Дизайн
    {"name": "Софья Романова", "position": "UI/UX-дизайнер", "team": "Дизайн", "manager": "Екатерина Васильева", "city": "Москва", "birthday": date(1995, 3, 9), "email": "s.romanova@company.ru"},
    {"name": "Александр Кузнецов", "position": "Графический дизайнер", "team": "Дизайн", "manager": "Екатерина Васильева", "city": "Москва", "birthday": date(1991, 6, 18), "email": "a.kuznetsov@company.ru"},
    {"name": "Вероника Лебедева", "position": "UI/UX-дизайнер", "team": "Дизайн", "manager": "Екатерина Васильева", "city": "Санкт-Петербург", "birthday": date(1996, 11, 24), "email": "v.lebedeva@company.ru"},
    {"name": "Михаил Соколов", "position": "Дизайнер", "team": "Дизайн", "manager": "Екатерина Васильева", "city": "Москва", "birthday": date(1993, 2, 2), "email": "m.sokolov@company.ru"},
    {"name": "Анастасия Попова", "position": "UI/UX-дизайнер", "team": "Дизайн", "manager": "Екатерина Васильева", "city": "Казань", "birthday": date(1997, 8, 13), "email": "a.popova@company.ru"},
]

created = {}
for data in employees_data:
    team = teams[data["team"]]
    emp = Employee.objects.create(
        name=data["name"],
        position=data["position"],
        team=team,
        city=data["city"],
        birthday=data["birthday"],
        email=data["email"],
        telegram="@telegram"
    )
    created[data["name"]] = emp

for data in employees_data:
    if data["manager"]:
        emp = created[data["name"]]
        emp.manager = created[data["manager"]]
        emp.save()

print(f"Создано сотрудников: {Employee.objects.count()}")
