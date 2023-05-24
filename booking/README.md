# Проект 2. Анализ вакансий из HeadHunter

## Оглавление  

[1. Описание проекта](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_sql/README.md#Описание-проекта)

[2. Этапы работы над проектом](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_sql/README.md#Этапы-работы-над-проектом)

[3. Метрики качества](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_sql/README.md#Метрики-качества)  

[4. Краткая информация о данных](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_sql/README.md#Краткая-информация-о-данных) 

[5. Результаты](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_sql/README.md#Результаты)    

### Описание проекта    
Компания HeadHunter хочет построить модель, которая рекомендует вакансии клиентам кадрового агентства, претендующим на позицию Data Scientist. Однако сначала нужно понять, что из себя представляют данные и насколько они соответствуют целям проекта.

:arrow_up: [к оглавлению](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_sql/README.md#Оглавление)

### Этапы работы над проектом  
1. Знакомство с данными
2. Предварительный анализ данных
3. Детальный анализ вакансий
4. Анализ работодателей
5. Предметный анализ

:arrow_up: [к оглавлению](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_sql/README.md#Оглавление)

**Метрики качества**     
- Решение оформлено в Jupyter Notebook.
- Решение оформлено в соответствии с ноутбуком-шаблоном.
- Каждое задание выполнено в отдельных ячейках, выделенных под задание.
- Текст SQL-запросов и код на Python должны быть читаемыми.
- Выводы по каждому этапу оформлены в формате Markdown в отдельной ячейке.

:arrow_up: [к оглавлению](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_sql/README.md#Оглавление)

### Краткая информация о данных 
<image src="https://lms.skillfactory.ru/assets/courseware/v1/efd63819603e7d4f4433ed2fedec717c/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_1.png" width="448" height="492"/>

База данных состоит из 5 таблиц. Рассмотрим их структуру.

**VACANCIES**

Таблица хранит в себе данные по вакансиям и содержит следующие столбцы:

<image src="https://lms.skillfactory.ru/assets/courseware/v1/837cf6ff79f483e387a16c993634f3e4/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_2.png" width="585" height="288"/>


Зарплатная вилка — это верхняя и нижняя граница оплаты труда в рублях (зарплаты в других валютах уже переведены в рубли). Соискателям она показывает, в каком диапазоне компания готова платить сотруднику на этой должности.


**AREAS**

Таблица-справочник, которая хранит код города и его название.

<image src="https://lms.skillfactory.ru/assets/courseware/v1/682c2306f3d46a25915a89d4ec7e16ed/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_3.png" width="585" height="108"/>

**EMPLOYERS**

Таблица-справочник со списком работодателей.

<image src="https://lms.skillfactory.ru/assets/courseware/v1/d2a26db623c75572c71923b57241e038/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_4.png" width="585" height="148"/>

**INDUSTRIES**

Таблица-справочник вариантов сфер деятельности работодателей.

<image src="https://lms.skillfactory.ru/assets/courseware/v1/2c76bca09937a1a05a9e66d51008e298/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_5.png" width="595" height="108"/>

**EMPLOYERS_INDUSTRIES**

Дополнительная таблица, которая существует для организации связи между работодателями и сферами их деятельности.

Эта таблица нужна нам, поскольку у одного работодателя может быть несколько сфер деятельности (или работодатели могут вовсе не указать их). Для удобства анализа необходимо хранить запись по каждой сфере каждого работодателя в отдельной строке таблицы.

<image src="https://lms.skillfactory.ru/assets/courseware/v1/16ff3df0bb0ddecd922562f3c4bdd32c/asset-v1:SkillFactory+DST-3.0+28FEB2021+type@asset+block/SQL_pj2_2_6.png" width="595" height="108"/>

### Результаты  
- Выявлены города - лидеры и компании по количеству открытых вакансий.
- Представлен средний диапазон зарплат, которые работодатели готовы платить своим сотрудникам.
- Проанализированы требования работодателей к опыту работы сотрудников, а также типу трудоустройства и рабочего графика.
- Детально рассмотрены вакансии для специалистов в области Data Science, а также текущие требования к ним и оплата труда.

:arrow_up: [к оглавлению](https://github.com/vanpakpro/Data_Science_Hub/tree/main/hh_vacancies/README.md#Оглавление)