### JavaScript (день 23)

### Используйте JavaScript для управления поведением

#### Базовый синтаксис JavaScript

- Заявления и комментарии
- Переменные и типы данных
  * Декларация и уступка
  * Простые типы данных и сложные типы данных
  * Правила именования переменных
- Выражения и операторы
  * Оператор присваивания
  * Арифметический оператор
  * Оператор сравнения
  * Логические &&операторы: ||,,!
- Структура филиала
  * if...else...
  * switch...cas...default...
- Циклическая структура
  * for цикл
  * while цикл
  * do...while цикл
- Множество
  * Создать массив
  * Манипулировать элементами в массиве
- функция
  * Объявить функцию
  * функция вызова
  * Параметры и возвращаемые значения
  * Анонимная функция
  * Вызов функции немедленно

#### Объектно-ориентированный

 - Концепция объекта
 - Литеральный синтаксис для создания объектов
 - Доступ к оператору-члену
 - Синтаксис конструктора для создания объектов
  * this Ключевое слово
 - Добавить и удалить атрибуты
  * delete Ключевое слово
 - Стандартный объект
  * Number/ String/ Boolean/ Symbol/ Array/Function
  * Date/ Error/ Math/ RegExp/ Object/ Map/Set
  * JSON/ Promise/ Generator/ Reflect/Proxy

#### Спецификация BOM

 - `window` Свойства и методы объекта
 - `history`Объект
    - `forward()` / `back()` / `go()`
 - `location`Объект
 - `navigator`Объект
 - `screen`Объект

#### DOM

  - DOM-дерево
  - Элемент доступа
    - getElementById() / querySelector()
    - getElementsByClassName()/ getElementsByTagName()/querySelectorAll()
    - parentNode/ previousSibling/ nextSibling/ children/ firstChild/lastChild
  - Элемент операции
    - nodeValue
    - innerHTML/ textContent/ createElement()/ createTextNode()/ appendChild()/ insertBefore()/removeChild()
    - className/ id/ hasAttribute()/ getAttribute()/ setAttribute()/removeAttribute()
  - Обработка событий
    - Тип события
    - События пользовательского интерфейса: load/ unload/ error/ resize/scroll
    - События клавиатуры: keydown/ keyup/keypress
    - События мыши: click/ dbclick/ mousedown/ mouseup/ mousemove/ mouseover/mouseout
    - Фокусное событие: focus/blur
    - Событие формы: input/ change/ submit/ reset/ cut/ copy/ paste/select
  - Связывание событий
    - Обработчик событий HTML (не рекомендуется, потому что метка должна быть отделена от кода)
    - Традиционный обработчик событий DOM (можно подключить только одну функцию обратного вызова)
    - Слушатель событий (не поддерживается в старых браузерах)
  - Поток событий: захват событий / всплытие событий
  - Объект события (window.event в более ранней версии IE)
    - target(Некоторые браузеры используют srcElement)
    - type
    - cancelable
    - preventDefault()
    - stopPropagation()(CancelBubble в более ранней версии IE)
  - Событие мыши - место, где произошло событие
    - Положение экрана: screenXиscreenY
    - Позиция страницы: pageXиpageY
    - Расположение клиента: clientXиclientY
    - Событие клавиатуры - какая клавиша была нажата
    - keyCodeСвойства (используются некоторыми браузерами which)
    - String.fromCharCode(event.keyCode)
  - HTML5 события
    - `DOMContentLoaded`
    - `hashchange`
    - `beforeunload`

#### JavaScript API

- Клиентское хранилище - `localStorage` и `sessionStorage`

  ```JavaScript
  localStorage.colorSetting = '#a4509b';
  localStorage['colorSetting'] = '#a4509b';
  localStorage.setItem('colorSetting', '#a4509b');
  ```

- Получить информацию о местоположении - `geolocation`

  ```JavaScript
  navigator.geolocation.getCurrentPosition(function(pos) { 		  
      console.log(pos.coords.latitude)
      console.log(pos.coords.longitude)
  })
  ```

- Получение данных из server-Fetch API

- Draw Graphics- <canvas>API

- Аудио и видео- <audio>и <video>API



[Вернуться на главную](https://github.com/BEPb/Python-100-days)

[К следующему занятию](https://github.com/BEPb/Python-100-days/blob/master/%D0%94%D0%B5%D0%BD%D1%8C%2021-30/%D0%94%D0%B5%D0%BD%D1%8C%2024/README.md)
