HH and SJ parser
Курсовая работа №4 Максимов Д.А

Парсер для работы с HH.ru и Super Job.

Программа ищет вакансии под заданным параметрам:
- Ключевое слово
- Город
- Количество вакансий

**Сначала предлагается сайт HH.ru.** Для поиска нужно ввести ключевые слова
и город (можно латиницей), а так же количество вакансий.
~~Изначально, если не был введен хотя-бы один параметр для поиска, 
программа предлагала продолжить поиск на другом сайте~~, 
но после, я ввел бесконечный цикл для заполнения всех параметров.
Если нет необходимости искать на HH, нажмите (н/n)

**После, сайт SuperJob.** Тут, важно ввести название города кириллицей(для городов РФ),
в противном случае ничего не найдет.

Вакансии сохраняются в файл .json
На экран вакансии выводятся отфильтрованные по минимальной ЗП!
Я не стал отсекать ЗП по валюте или стране, чтобы не потерять 
интересные предложения. Просто сортируется по минимальной цифре.

