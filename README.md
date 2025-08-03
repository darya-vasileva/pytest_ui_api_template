# pytest_ui_api_template

## Шаблон для автоматизации тестирования на python

### Шаги:
1. Склонировать проект 'git clone https://github.com/darya-vasileva/pytest_ui_api_template.git'
2. Установить все зависимости
3. Запустить тесты 'pytest' # python -m pytest
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД(?)
- test_config.ini - настройки для тестов

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests
