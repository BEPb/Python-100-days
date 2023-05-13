### jQuery (день 24)
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



[Вернуться на главную](https://github.com/BEPb/Python-100-days)

[К следующему занятию](https://github.com/BEPb/Python-100-days/blob/master/%D0%94%D0%B5%D0%BD%D1%8C%2021-30/%D0%94%D0%B5%D0%BD%D1%8C%2025/README.md)
