# Currency_Converter
Мобильное приложение на фреймворке kivy


## Описание:
- Обзор программы: В этом мобильном приложении можно конвертировать различные типы валют в рубли (RUB). Предусматривается экран входа в систему. Учетные данные пользователя сохраняются в формате .json. Если у пользователя отсутствует учетная запись, он может создать ее при помощи кнопки регистрации. Если пользователь забыл пароль, он может воспользоваться функцией “Забыли пароль”.

- Структурно приложение состоит из файла main.py, файла design.kv, файла user_details.json, и папки image, внутри которой находится изображение логотипа для приложения. В main.py контролируется логика работы (бэкенд) приложения, в design.kv контролируется внешний вид приложения (фронтенд), в user_details.json хранятся учетные данные пользователя в формате ключ:значение с помощью формата json.


## Как использовать:`

- Перейти в репозиторий<br>
`cd Currency_Converter`
- Создать виртуальное окружение<br>
`python3 -m venv venv`
- Активировать ви ртуальное окружение<br>
`source venv/bin/activate`
- Проинсталлировать библиотеки для функционирования приложения<br>
`pip install kivy`
- Запустить python файл<br>
`python main.py`