## Обзор веб-интерфейса

> Примечание. Некоторые из иллюстраций, использованных в этой статье, взяты из книги Джона Дакетта * HTML и CSS: 
> разработка и создание веб-сайтов *. Это отличная вводная книга. Заинтересованные читатели могут найти книгу на 
> Amazon или других веб-сайтах. Ссылка на покупку.

### Краткая история HTML

1. Октябрь 1991 г .: Европейский центр ядерных исследований изначально публикует 18 тегов HTML, автор этого 
   документа - физик Тим Бернерс-Ли, так что он изобретатель Всемирной паутины
2. Ноябрь 1995 г .: опубликован стандарт HTML 2.0 (RFC 1866).
3. Январь 1997: HTML 3.2 был выпущен как рекомендация W3C .
4. Декабрь 1997: HTML 4.0 был выпущен как рекомендация W3C.
5. Декабрь 1999: HTML4.01 был выпущен как рекомендация W3C.
6. Январь 2008: HTML5 был выпущен W3C в качестве рабочего проекта.
7. Май 2011: W3C переводит HTML5 на стадию «Последний звонок».
8. Декабрь 2012: W3C обозначил HTML5 как этап «рекомендации кандидата».
9. Октябрь 2014: HTML5 был выпущен как стабильная рекомендация W3C, что означает, что стандартизация HTML5 завершена.

#### Новые возможности HTML5

1. Ввести встроенную поддержку мультимедиа (аудио и видео теги)
2. Ввести программируемый контент (тег холста)
3. Знакомство с семантической сетью (теги article, aside, details, figure, footer, header, nav, section, summary и т.
   д.)
4. Представьте новые элементы управления формой (календарь, почтовый ящик, поиск, слайдер и т. д.)
5. Улучшить поддержку автономного хранилища (localStorage и sessionStorage)
6. Внедрить поддержку позиционирования, перетаскивания, WebSocket, фоновых задач и т. д.

### Используйте теги для размещения контента

####  Состав стандартной страницы HTML

- html
  - head
    - title
    - meta
  - body

#### текст

- Заголовок и абзац
  - h1 ~ h6
  - p
- Надстрочный （superscript） и подстрочный （subscript）индекс
  - sup
  - sub
- Пустой (пробел сложен)
- Разрыв （break）и горизонтальная линейка和水平标尺（horizontal ruler）
  - br
  - hr
- Семантические теги
  - Смелый и подчеркнутый-сильный - strong
  - Цитата - blockquote
  - Сокращения и акронимы - abbr / acronym
  - цитировать - cite
  - Контактная информация Владельца - address
  - Изменения содержимого - ins / del

#### Список（list）

 - Упорядоченный список（ordered list）- ol / li
 - Неупорядоченный список（unordered list）- ul / li
 - Список определений（definition list）- dl / dt / dd

#### Ссылка (привязка)

- Ссылка на страницу
- Якорная ссылка
- Ссылка на функцию

#### Изображение image）

- Место хранения изображений  

- Изображение, его ширина и высота

- Выберите правильный формат изображения
  - JPEG
  - GIF
  - PNG

- Векторная иллюстрация

- Семантическая разметка- figure / figcaption

#### Таблица（table）

- Базовая структура таблицы - table / tr / td / th
- Заголовок таблицы-подпись - caption
- Атрибут  - rowspan / colspan
- Длинная форма - thead / tbody / tfoot

#### Форма（form）

- Важные атрибуты - action / method / enctype
- Атрибут типа элемента управления (ввода)
  - Текстовое поле - text / поле пароля- password / числовое поле- number
  - Email- email/ телефон - tel/ Дата - date/ Slider- range/ url- url/ Search-search
  - Радиокнопка- radio/ Проверить кнопку-checkbox
  - Загрузка файла file/ скрытый домен-hidden
  - Кнопка отправки- submit/ кнопка изображения- image / кнопка сброса-reset
- Раскрывающийся список - select / option
- текстовая область (многострочный текст) - textarea
- Объединить элементы формы - fieldset / legend

#### Аудио и видео（audio / video）

- Формат видео и плеер
- Услуги видеохостинга
- Подготовка к добавлению видео
- теги видео и атрибуты- autoplay / controls / loop / muted / preload / src
- аудио теги и атрибуты- autoplay / controls / loop / muted / preload / src / width / height / poster

#### Оконная рама（frame）

- Набор фреймов (устаревший, не рекомендуется) - frameset / frame

- Встроенное окно - iframe

#### Другие

- Тип документа

  ```HTML
  <!doctype html>
  ```

  ```HTML
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
  ```

  ```HTML
  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
  ```

- Аннотации

  ```HTML
  <!-- Это комментарий, комментарии не могут быть вложенными -->
  ```

- Атрибуты
  - id: уникальный идентификатор
  - class: класс, к которому принадлежит элемент, используемый для различения различных элементов.
  - title: дополнительная информация об элементе (текст всплывающей подсказки будет отображаться при наведении курсора мыши)
  - tabindex: порядок переключения клавиш табуляции
  - contenteditable: доступен ли элемент для редактирования
  - draggable: можно ли перетащить элемент

- Элемент уровня блока / элемент уровня строки

- Сущность персонажа (замена сущности)


### Визуализируйте страницу с помощью CSS

#### Вступление

- Роль CSS

- Как работает CSS

- Правила, атрибуты и ценности

- Общие селекторы

 
#### Цвет
- Как указать цвета
- Цветовая гамма и цветовой контраст
- Фоновый цвет

#### текст / шрифт（text / font）

- Размер и шрифт текста (font-size / font-family)

- Толщина, стиль, растяжка и оформление (font-weight / font-style / font-stretch / text-decoration)

- Высота строки, межбуквенный интервал и межсловный интервал

- Выравнивание (выравнивание текста) и отступ (идентификатор текста)

- Стиль ссылки (: ссылка /: посетил /: актив /: наведен)

- CSS3 новые свойства

   - Эффект тени-текст-тень
   - Первая буква и первая строка текста (: first-letter /: first-line)
   - Отвечайте пользователям

#### Коробка （box model）

- Контроль размера коробки（width / height）

- Граница, внешнее поле и внутреннее поле поля (граница/поле/отступ)（border/margin/padding）

- Показать и скрыть поле (отображение / видимость)（display / visibility）

- CSS3 новые свойства
  - Граница-изображение（border-image）
  - Проекция (граница-тень)（border-shadow）
  - Закругленные углы （border-radius）

#### Списки, таблицы и формы

- Список маркеров (в виде списка)
- Граница и фон таблицы (border-collapse)
- Внешний вид элементов управления формой
- Выравнивание элементов управления формой
- Инструменты разработчика для браузера

#### изображение
- Управление размером изображения (отображение: встроенный блок)
- Выровнять изображение
- Фоновое изображение (background / background-image / background-repeat / background-position)
（background / background-image / background-repeat / background-position）

#### макет
- Положение элемента управления (позиция / z-индекс)

- Нормальный поток
- Относительное позиционирование
- Абсолютное позиционирование
- Фиксированное позиционирование
- Плавающий элемент (float / clear)


Макет HTML5

- По размеру экрана
  - Макет фиксированной ширины
  - Плавный макет
  - Сетка макета

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

### Используйте jQuery

#### обзор jQuery

1. Пишите меньше, делайте больше (используйте меньше кода, чтобы выполнять больше работы)
2. Используйте селекторы CSS для поиска элементов (проще и удобнее)
3. Используйте методы jQuery для управления элементами (решите проблемы совместимости браузера, примените ко всем элементам и примените несколько методов) 


#### Представляем jQuery
- Загрузите версию для разработки и сжатую версию jQuery
- Загрузить jQuery из CDN

```HTML
<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
<script>
    window.jQuery || 
        document.write('<script src="js/jquery-3.3.1.min.js"></script>')
</script>
```

#### Найти элемент
Селектор
* / element / #id / .class / selector1, selector2
  - предок потомок / родитель> потомок / предыдущий + следующий / предыдущие братья и сестры
* Фильтр
  - Основные фильтры:: not (селектор) /: first /: last /: even /: odd /: eq (index) /: gt (index) /: lt (index) /: animated /: focus
  - Фильтр содержимого:: содержит ('...') /: пустой /: родительский /: имеет (селектор)
  - Фильтр видимости:: скрытый /: видимый
  - Фильтр дочерних узлов:: nth-child (expr) /: first-child /: last-child /: only-child
  - Фильтр атрибутов: [атрибут] / [атрибут = 'значение'] / [атрибут! = 'Значение'] / [атрибут ^ = 'значение'] / [атрибут $ = 'значение'] / [атрибут | = 'значение'] / [атрибут ~ = 'значение']
* Форма:: input /: text /: password /: radio /: checkbox /: submit /: image /: reset /: button /: file /: selected /: enabled /: disabled /: checked
#### Выполнить операцию
* Манипуляции с контентом
  - Получить / изменить содержимое: html()/ text()/ replaceWith()/remove()
  - Получить / установить элемент: before()/ after()/ prepend()/ append()/ remove()/ clone()/ unwrap()/ detach()/ empty()/add()
  - Получить / изменить атрибуты: attr()/ removeAttr()/ addClass()/ removeClass()/css()
  - Получить / установить значение формы:val()
* Найти операцию
  - Метод поиска: find()/ parent()/ children()/ siblings()/ next()/ nextAll()/ prev()/prevAll()
  - Фильтр: filter()/ not()/ has()/ is()/contains()
  - Индекс:eq()
* Размер и положение
  - В зависимости от размера: height()/ width()/ innerHeight()/ innerWidth()/ outerWidth()/outerHeight()
  - Связано с местоположением: offset()/ position()/ scrollLeft()/scrollTop()
* Спецэффекты и анимация
  - Базовая анимация: show()/ hide()/toggle()
  - Исчезли: fadeIn()/ fadeOut()/ fadeTo()/fadeToggle()
  - Эффект скольжения: slideDown()/ slideUp()/slideToggle()
  - Пользовательский: delay()/ stop()/animate()
* мероприятие
  - Загрузка документа: ready()/load()
  - Взаимодействие с пользователем: on()/off()

#### Цепная операция

#### Проверить, доступна ли страница

```HTML
<script>
    $(document).ready(function() {
        
    });
</script>
```

```HTML
<script>
    $(function() {
        
    });
</script>
```

#### jQuery плагин

- jQuery Validation
- jQuery Treeview
- jQuery Autocomplete
- jQuery UI

#### Избегайте конфликтов с другими библиотеками
Ситуация с введением сначала других библиотек, а затем jQuery.

```HTML
<script src="other.js"></script>
<script src="jquery.js"></script>
<script>
	jQuery.noConflict();
    jQuery(function() {
        jQuery('div').hide();
    });
</script>
```

Ситуация, когда сначала вводится jQuery, а затем вводятся другие библиотеки.

```HTML

<script src="jquery.js"></script>
<script src="other.js"></script>
<script>
    jQuery(function() {
        jQuery('div').hide();
    });
</script>
```

#### Используйте Ajax
Ajax - это технология, которая может обновлять часть веб-страницы без перезагрузки всей веб-страницы.

- Родной Ajax
- Ajax на основе jQuery
   - Загрузить контент
   - представить форму

### Интерфейсный фреймворк

#### Прогрессивный фреймворк - [Vue.js](<https://cn.vuejs.org/>)

Требуемый фреймворк для интерфейсной и внутренней разработки (внешний рендеринг).

##### Начни быстро

1. Представляя файл Vue JavaScript, мы по-прежнему рекомендуем загружать его с сервера CDN.

   ```HTML
   <script src="https://cdn.jsdelivr.net/npm/vue"></script>
   ```

2. Связывание данных (декларативный рендеринг).

   ```HTML
   <div id="app">
   	<h1>{{ product }}Информация об инвентаре</h1>
   </div>
   
   <script src="https://cdn.jsdelivr.net/npm/vue"></script>
   <script>
   	const app = new Vue({
   		el: '#app',
   		data: {
   			product: 'iPhone X'
   		}
   	});
   </script>
   ```

3. Условия и петли.

   ```HTML
   <div id="app">
   	<h1>Информация об инвентаре</h1>
       <hr>
   	<ul>
   		<li v-for="product in products">
   			{{ product.name }} - {{ product.quantity }}
   			<span v-if="product.quantity === 0">
   				Уже продано
   			</span>
   		</li>
   	</ul>
   </div>
   
   <script src="https://cdn.jsdelivr.net/npm/vue"></script>
   <script>
   	const app = new Vue({
   		el: '#app',
   		data: {
   			products: [
   				{"id": 1, "name": "iPhone X", "quantity": 20},
   				{"id": 2, "name": "Mate20", "quantity": 0},
   				{"id": 3, "name": "Mix3", "quantity": 50}
   			]
   		}
   	});
   </script>
   ```

4. Вычислить атрибуты.

   ```HTML
   <div id="app">
   	<h1>Информация об инвентаре</h1>
   	<hr>
   	<ul>
   		<li v-for="product in products">
   			{{ product.name }} - {{ product.quantity }}
   			<span v-if="product.quantity === 0">
   				Уже продано
   			</span>
   		</li>
   	</ul>
   	<h2>вычислено：{{ totalQuantity }}台</h2>
   </div>
   
   <script src="https://cdn.jsdelivr.net/npm/vue"></script>
   <script>
   	const app = new Vue({
   		el: '#app',
   		data: {
   			products: [
   				{"id": 1, "name": "iPhone X", "quantity": 20},
   				{"id": 2, "name": "Mate20", "quantity": 0},
   				{"id": 3, "name": "Mix3", "quantity": 50}
   			]
   		},
   		computed: {
   			totalQuantity() {
   				return this.products.reduce((sum, product) => {
   					return sum + product.quantity
   				}, 0);
   			}
   		}
   	});
   </script>
   ```

5. Обработка событий.

   ```HTML
   <div id="app">
   	<h1>Информация об инвентаре</h1>
   	<hr>
   	<ul>
   		<li v-for="product in products">
   			{{ product.name }} - {{ product.quantity }}
   			<span v-if="product.quantity === 0">
   				Уже продано
   			</span>
   			<button @click="product.quantity += 1">
   				Увеличить инвентарь
   			</button>
   		</li>
   	</ul>
   	<h2>Общий запас: {{totalQuantity}} единиц</h2>
   </div>
   
   <script src="https://cdn.jsdelivr.net/npm/vue"></script>
   <script>
   	const app = new Vue({
   		el: '#app',
   		data: {
   			products: [
   				{"id": 1, "name": "iPhone X", "quantity": 20},
   				{"id": 2, "name": "Mate20", "quantity": 0},
   				{"id": 3, "name": "ix3", "quantity": 50}
   			]
   		},
   		computed: {
   			totalQuantity() {
   				return this.products.reduce((sum, product) => {
   					return sum + product.quantity
   				}, 0);
   			}
   		}
   	});
   </script>
   ```

6. Пользовательский ввод.

   ```HTML
   <div id="app">
   	<h1>Информация об инвентаре</h1>
   	<hr>
   	<ul>
   		<li v-for="product in products">
   			{{ product.name }} - 
   			<input type="number" v-model.number="product.quantity" min="0">
   			<span v-if="product.quantity === 0">
   				Уже продано
   			</span>
   			<button @click="product.quantity += 1">
   				Увеличить инвентарь
   			</button>
   		</li>
   	</ul>
   	<h2>Общий запас: {{totalQuantity}} единиц </h2>
   </div>
   
   <script src="https://cdn.jsdelivr.net/npm/vue"></script>
   <script>
   	const app = new Vue({
   		el: '#app',
   		data: {
   			products: [
   				{"id": 1, "name": "iPhone X", "quantity": 20},
   				{"id": 2, "name": "Mate20", "quantity": 0},
   				{"id": 3, "name": "Mix3", "quantity": 50}
   			]
   		},
   		computed: {
   			totalQuantity() {
   				return this.products.reduce((sum, product) => {
   					return sum + product.quantity
   				}, 0);
   			}
   		}
   	});
   </script>
   ```

7. Загрузите данные JSON по сети.

   ```HTML
   <div id="app">
   	<h2>Информация об инвентаре</h2>
   	<ul>
   		<li v-for="product in products">
   			{{ product.name }} - {{ product.quantity }}
   			<span v-if="product.quantity === 0">
   				Уже продано
   			</span>
   		</li>
   	</ul>
   </div>
   
   <script src="https://cdn.jsdelivr.net/npm/vue"></script>
   <script>
   	const app = new Vue({
   		el: '#app',
   		data: {
   			products: []
   		}，
   		created() {
   			fetch('https://jackfrued.top/api/products')
   				.then(response => response.json())
   				.then(json => {
   					this.products = json
   				});
   		}
   	});
   </script>
   ```

##### Используйте scaffolding-vue-cli
Vue предоставляет очень удобный инструмент для создания шаблонов vue-cli для разработки коммерческих проектов.С помощью этого инструмента вы можете сохранить шаги ручной настройки среды разработки, среды тестирования и операционной среды, позволяя разработчикам уделять внимание только проблеме, которую нужно решить. .

1. Установить строительные леса.
2. Создайте проект.
3. Установите зависимые пакеты.
4. Запускаем проект.

#### Платформа пользовательского интерфейса
Библиотека компонентов рабочего стола, основанная на Vue 2.0, используется для создания пользовательского интерфейса и поддерживает адаптивный макет.

1. Представьте файлы Element CSS и JavaScript.

   ```HTML
   <!-- Знакомство со стилем -->
   <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
   <!-- Знакомство с библиотекой компонентов -->
   <script src="https://unpkg.com/element-ui/lib/index.js"></script>
   ```

2. Простой пример.

   ```HTML
   <!DOCTYPE html>
   <html>
       <head>
           <meta charset="UTF-8">
           <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
       </head>
       <body>
           <div id="app">
               <el-button @click="visible = true">Нажми меня</el-button>
               <el-dialog :visible.sync="visible" title="Hello world">
                   <p>Начать использовать элемент</p>
               </el-dialog>
               </div>
       </body>
       <script src="https://unpkg.com/vue/dist/vue.js"></script>
       <script src="https://unpkg.com/element-ui/lib/index.js"></script>
       <script>
           new Vue({
               el: '#app',
               data: {
                   visible: false,
               }
           })
       </script>
   </html>
   ```

3. Используйте компоненты.

   ```HTML
   <!DOCTYPE html>
   <html>
       <head>
           <meta charset="UTF-8">
           <link rel="stylesheet" href="https://unpkg.com/element-ui/lib/theme-chalk/index.css">
       </head>
       <body>
           <div id="app">
               <el-table :data="tableData" stripe style="width: 100%">
                   <el-table-column prop="date" label="date" width="180">
                   </el-table-column>
                   <el-table-column prop="name" label="name" width="180">
                   </el-table-column>
                   <el-table-column prop="address" label="Address">
                   </el-table-column>
               </el-table>
           </div>
       </body>
       <script src="https://unpkg.com/vue/dist/vue.js"></script>
       <script src="https://unpkg.com/element-ui/lib/index.js"></script>
       <script>
           new Vue({
               el: '#app',
               data: {
                   tableData:  [
                       {
                           date: '2016-05-02',
                           name: 'Иван',
                           address: 'ул. Победы 22'
                       }, 
                       {
                           date: '2016-05-04',
                           name: 'Костя',
                           address: 'ул. Мира 11'
                       }, 
                       {
                           date: '2016-05-01',
                           name: 'Саша',
                           address: 'ул. Ленини 2'
                       }, 
                       {
                           date: '2016-05-03',
                           name: 'Женя,
                           address: 'ул. Минская 3'
                       }
                   ]
               }
           })
       </script>
   </html>
   ```


#### Структура отчета - ECharts
Библиотека визуализации с открытым исходным кодом, созданная Baidu, часто используется для создания различных типов отчетов.


#### CSS-фреймворк на основе flexbox - Bulma
Bulma - это современный CSS-фреймворк, основанный на Flexbox, его первоначальная цель - Mobile First, модульный дизайн, который можно легко использовать для реализации различных простых или сложных макетов контента, даже разработчики, которые не понимают CSS, могут использовать его. Настроить красивую страницу. 

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Bulma</title>
	<link href="https://cdn.bootcss.com/bulma/0.7.4/css/bulma.min.css" rel="stylesheet">
	<style type="text/css">
		div { margin-top: 10px; }
		.column { color: #fff; background-color: #063; margin: 10px 10px; text-align: center; }
	</style>
</head>
<body>
	<div class="columns">
		<div class="column">1</div>
		<div class="column">2</div>
		<div class="column">3</div>
		<div class="column">4</div>
	</div>
	<div>
		<a class="button is-primary">Primary</a>
		<a class="button is-link">Link</a>
		<a class="button is-info">Info</a>
		<a class="button is-success">Success</a>
		<a class="button is-warning">Warning</a>
		<a class="button is-danger">Danger</a>
	</div>
	<div>
		<progress class="progress is-danger is-medium" max="100">60%</progress>
	</div>
	<div>
		<table class="table is-hoverable">
			<tr>
				<th>One</th>
				<th>Two</th>
			</tr>
			<tr>
				<td>Three</td>
				<td>Four</td>
			</tr>
			<tr>
				<td>Five</td>
				<td>Six</td>
			</tr>
			<tr>
				<td>Seven</td>
				<td>Eight</td>
			</tr>
			<tr>
				<td>Nine</td>
				<td>Ten</td>
			</tr>
			<tr>
				<td>Eleven</td>
				<td>Twelve</td>
			</tr>
		</table>
	</div>
</body>
</html>
```

#### Фреймворк адаптивного макета - [Bootstrap](<http://www.bootcss.com/>)

Фреймворк для быстрой разработки веб-приложений, поддерживающий адаптивные макеты.

1. Функции
   - Поддержка основных браузеров и мобильных устройств
   - легко использовать
   - Адаптивный дизайн

2. содержание

   - Система сеток
   - Инкапсулированный CSS
   - Готовые компоненты
   - Плагин JavaScript

3. Визуализация

