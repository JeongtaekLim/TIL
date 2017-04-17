# Unicode

### Problem
1. Child React.Componenet want to inherit some unicode from its parent as props
2. Parent want to make some inheritance of unicode string to its child
3. However, case like below not works.
```html
<li>
     <a href="#">{this.props.symbol}<span/>Unicode not working</a>
     <!-- this.props.symbol : &#x270E;-->
</li>
```

### Solution
link : https://mathiasbynens.be/notes/javascript-unicode

There is no need to additional parsing function, but just modify little things in way of string inheritance.

```js
{
    symbol: '\u{270E}',
    title: '문제직접작성',
    href: 'http://localhost:3001/problem/write'
}
```j