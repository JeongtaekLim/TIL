# Request-Array
In case of requesting some array via post you should use `JSON`

* code
```js
...

app.use(bodyParser.json());

...

res.send(req.body);
```
* request(with JSON(application/json))
```
{
    "code": "print 'Hello!'",
    "language": "0",
    "ins": "ins",
    "outs": [1,2,3]
}
```
* return
```
{
  "code": "print 'Hello!'",
  "language": "0",
  "ins": "ins",
  "outs": [
    1,
    2,
    3
  ]
}
```
when you test, please use [online json validator](https://jsonlint.com/)