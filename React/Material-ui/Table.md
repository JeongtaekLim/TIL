# Table

## Issues

1. TableRow에 포함되어 있는 Button이 눌린 경우, TableRow 에도 중복으로 클릭이벤트가 전달되어 원하는 동작을 하지 않음

## Solutions

1. TableRow에 포함되어 있는 Button이 눌린 경우, TableRow 에도 중복으로 클릭이벤트가 전달되어 원하는 동작을 하지 않음
TableRowColumn 항목의 내부에 독립적인 이벤트 실행을 하기 원하는 wrapper를 하나 선언하여, TableRowColumn으로의 이벤트 전달을 막는다.

출처 - [Preventing a row from being selected when a child cell is clicked does not work #4535](https://github.com/callemall/material-ui/issues/4535)
```jsx
  <TableRowColumn>
    <div onClick={(e) => {
      e.preventDefault();
      e.stopPropagation();
    }}>
      <AutoComplete
        id={ `${i + 1}`}
        hintText=""
        dataSource={this.state.titles}
        onUpdateInput={(v) => this.onUpdateInput(v)}
      />
    </div>
  </TableRowColumn>
```