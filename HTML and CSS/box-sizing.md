# box-sizing

* Problem

When I make some side navigation with react component, I found that this nav show differently in different parent component.

For about 30min, I got a answer about it. The probelm was by 'box-sizing'

you should take a look at it, [CSS-trcks, about box-sizing](https://css-tricks.com/box-sizing/)

* Below code is recommended to almost every web proejcts.(in my thinking.)

```css
html {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
```