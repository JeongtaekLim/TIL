# Array

## link
* MDN: 
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array

## Create an Array
```javascript
var fruits = ['Apple', 'Banana'];
console.log(fruits.length);
// 2
```

## Access(index into) an Array item
```js
var first = fruits[0];
// Apple
var last = fruits[fruits.length - 1];
```

## Loop over an Array
```js
fruits.forEach(function(item, index, array){
    console.log(item, index);
});
// Apple 0
// Banana 1
```

## And to the end of an Array
```js
var newLength = fruits.push('Orange');
// ["Apple", "Banana", "Orange"]
```

## Remove from the end of an Array
```js
var last = fruits.pop(); // remove Orange (from the end)
// ["Apple", "Banana"];
```

