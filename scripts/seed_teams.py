from portal.models import Team

Team.objects.all().delete()

teams = [
    {"name": "Администрация", "description": "Высшее руководство компании", "mascot_icon": "building.2"},
    {"name": "Бухгалтерия", "description": "Финансовый учёт и отчётность", "mascot_icon": "chart.bar"},
    {"name": "Юридический отдел", "description": "Правовое сопровождение деятельности компании", "mascot_icon": "scale.3d"},
    {"name": "Технический отдел", "description": "Техническое руководство разработкой", "mascot_icon": "gearshape.2"},
    {"name": "Мобильная разработка", "description": "Разработка iOS и Android приложений", "mascot_icon": "iphone"},
    {"name": "Backend-разработка", "description": "Серверная разработка и API", "mascot_icon": "server.rack"},
    {"name": "Frontend-разработка", "description": "Разработка веб-интерфейсов", "mascot_icon": "safari"},
    {"name": "Дизайн", "description": "UI/UX и визуальный стиль продуктов", "mascot_icon": "paintbrush"},
]

for data in teams:
    Team.objects.create(**data)

print(f"Создано команд: {Team.objects.count()}")
