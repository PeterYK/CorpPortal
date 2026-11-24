from portal.models import Team, Employee

leaders_map = {
    "Администрация": ["Александр Волков"],
    "Бухгалтерия": ["Елена Соколова"],
    "Юридический отдел": ["Марина Кузнецова"],
    "Технический отдел": ["Дмитрий Орлов"],
    "Мобильная разработка": ["Алексей Смирнов"],
    "Backend-разработка": ["Павел Иванов"],
    "Frontend-разработка": ["Наталья Козлова"],
    "Дизайн": ["Екатерина Васильева"],
}

for team_name, leader_names in leaders_map.items():
    try:
        team = Team.objects.get(name=team_name)
        for name in leader_names:
            leader = Employee.objects.get(name=name)
            team.leaders.add(leader)
    except (Team.DoesNotExist, Employee.DoesNotExist) as e:
        print(f"Ошибка для {team_name}: {e}")

print("Руководители добавлены")
