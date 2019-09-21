# Child select

```
& > ul > li::before,
& > ul > li::after {
  border: 0;
}
```

# Nested Child select

```
& span {
    background-color: red;
}
```

# last child select

```
export const FigureIndicatorItemWrapper = styled(ShadowCard)`
  flex: 1 25%;
  position: relative;
  background-color: red;
  margin-right: 10px;
  &:last-child {
    background-color: black;
    margin-right: 0px;
  }
`;
```
