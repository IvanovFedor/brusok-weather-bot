# BrusokWeatherBot (MVP)
Чат-бот на платформе telegram для удобного получения прогноза погоды.
# Вступление:
Цель всего нашего дела — написать чат-бота для удобного получения прогноза погоды через платформу telegram. Первая наша задача — сделать MVP-версию бота, а лишь затем дополнять его различным функционалом.
# Возможности MVP-версии: 
- Команды /start и /help
- Текущая погода
- Прогноз на 5 дней*
# Термины:
1. *Информативное сообщение* — это сообщение, которое будет максимально понятно пользователю. В тексте должны присутствовать:
- Структура
- Разные виды начертания (Bold, Italic, SystemFixed),
- Emoji для лучшего ориентирования пользователей
2. *Главная клавиатура* — это клавиатура, содержащая в себе основные команды бота (Погода, Прогноз).
3. *Указать место* — действие пользователя, помогающее боту определить местность, по которому осуществляется запрос. Сделать это можно несколькими способами:
- Указание места (текстом)
- Отправка своего местоположения
- Отправка координат в формате lat, lon.
# Описание возможностей:
- Команды */start* и */help* — эквивалентные по-своей сути команды. В ответ на них бот отправляет пользователю информативное сообщение с описанием возможностей и главную клавиатуру для их использования.
- Текущая погода — команда *«Погода»* на главной клавиатура. Содержит в себе несколько последовательных шагов: 1. — После вызова команды, бот, в ответ на нее, отправляет пользователю информативное сообщение, где просит его указать место, по которому стоит определить погоду. 2. — Если бот успешно получил информацию о местности, по которой осуществлялся запрос погоды, он отправляет его результат в виде информативного сообщения, иначе — информативное сообщение об ошибке. 3. — завершает команду отправкой пользователю главной клавиатуры.
- Прогноз погоды — команда *«Прогноз»* на главной клавиатуре. Содержит в себе несколько последовательных шагов: 1. — После вызова команды, бот, в ответ на нее, отправляет пользователю информативное сообщение, где просит его указать место, по которому стоит определить погоду. 2. — Если бот успешно получил информацию о местности, по которой осуществлялся запрос прогноза, он отправляет его результат в виде информативного сообщения, иначе — сообщение об ошибке. 3. — завершает команду отправкой пользователю главной клавиатуры.
# Инструменты для разработки:
- Github и Git
- Trello — для лучшей организации работы
- Miro — для рисования схем
- UML — тоже для рисования схем
- PyCharm — я уже хз зачем я это пишу но ладно
- Windows — похоже я увлекся, заканчиваю.
# Используемые технологии, сервисы и API:
- Python — петухон — ванлав язык forever
- openweathermap.org — API погоды (Current weather data, 5 day / 3 hour forecast)
- https://geocode-maps.yandex.ru — API Яндекс.Карты для определения координат по имени местности (Города, улицы и т.д.)
- pyTelegramBotApi — библиотека telebot.
