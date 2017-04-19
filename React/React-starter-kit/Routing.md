# Routing

```js
const route = {
  path: '/path/:any',                 // example url: '/path/hello?the=query'
  action({ path, params, query }) {
    console.log(path);                // => '/path/hello'
    console.log(params);              // => { any: 'hello' }
    console.log(query);               // => { the: 'query' }
  }
}
```
* Link

https://github.com/kriasoft/react-starter-kit/issues/1028

* Documentation

https://github.com/kriasoft/universal-router/blob/master/docs/api.md#url-parameters