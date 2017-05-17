# Arrow Function
[MDN - Arrow Function](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
, [webframeworks.kr](http://webframeworks.kr/tutorials/translate/explanation-of-this-in-javascript-1/)
## Syntax

```js
(param1, param2, …, paramN) => { statements }
(param1, param2, …, paramN) => expression
// equivalent to: (param1, param2, …, paramN) => { return expression; }

// Parentheses are optional when there's only one parameter name:
(singleParam) => { statements }
singleParam => { statements }

// A function with no parameters should be written with a couple of parentheses.
() => { statements }

// Parenthesize the body to return an object literal expression:
params => ({foo: bar})

// Rest parameters and default parameters are supported
(param1, param2, ...rest) => { statements }
(param1 = defaultValue1, param2, …, paramN = defaultValueN) => { statements }

// Destructuring within the parameter list is also supported
var f = ([a, b] = [1, 2], {x: c} = {x: a + b}) => a + b + c;
f();  // 6

```

## Description

Two factors influenced the introduction of arrow functions: shorter functions and non-binding of this.

## Example
[source](https://toddmotto.com/es6-arrow-functions-syntaxes-and-lexical-scoping/#functionality-lexical-scoping-this)

```js
function FooCtrl (FooService) {
  this.foo = 'Hello';
  FooService
  .doSomething(function (response) {
    this.foo = response;
  }.bind(this));
}
```

```js
function FooCtrl (FooService) {
  var that = this;
  that.foo = 'Hello';
  FooService
  .doSomething(function (response) {
    that.foo = response;
  });
}
```
```js
function FooCtrl (FooService) {
  this.foo = 'Hello';
  FooService
  .doSomething((response) => { // woo, pretty
    this.foo = response;
  });
}
```