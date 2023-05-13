### Vue.js (день 25)


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


[Вернуться на главную](https://github.com/BEPb/Python-100-days)

[К следующему занятию](https://github.com/BEPb/Python-100-days/blob/master/%D0%94%D0%B5%D0%BD%D1%8C%2021-30/%D0%94%D0%B5%D0%BD%D1%8C%2026/README.md)
