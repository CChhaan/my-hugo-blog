显示的创建Object的实例有两种方式.第一种是使用new操作符和Object构造函数
```js
let person = new Object()
person.name = "Nicholas"
person.age = 29
```
另一种是使用对象字面量表示法。
```js
let person = {
	name:'Nicholas',
	age:29
}
```
左大括号表示对象字面量开始，接下来指定属性，后跟一个冒号，然后是属性的值。逗号用于在对象字面量中分隔属性，最后一个属性后面加上逗号在非常老的浏览器中可能会报错。
属性名可以是字符串或数值，数值属性会自动转换为字符串。
也可以用对象字面量表示法定义一个只有默认属性和方法的对象，只要使用一对大括号，中间留空就行了
```js
let person = { }
person.name = "Nicolas"
person.age = 29
```
属性一般是通过点语法来存取的，也可以使用中括号来存取属性，在使用中括号时，要在括号内使用属性名的字符串形式
```js
console.log(peron.name)
console.log(peron["name"])
```
使用中括号的优势是可以通过变量访问属性。
如果属性名中包含可能会导致语法错误的字符，或者包含关键字/保留字时，也可以使用中括号语法