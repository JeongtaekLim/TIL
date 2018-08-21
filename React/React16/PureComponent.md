# PureComponent

PureComponent 와 Component의 차이는 componentShouldUpdate 함수의 구현 여부의 차이이다. PureComponent는 props 및 state를 shallowCompare 하여, 변경사항이 있을때만 re-render한다.

```js
// a simple implementation of the shallowCompare.
// only compares the first level properties and hence shallow.
// state updates(theoretically) if this function returns true.
function shallowCompare(newObj, prevObj){
    for (key in newObj){
        if(newObj[key] !== prevObj[key]) return true;
    }
    return false;
}
// 
var game_item = {
    game: "football",
    first_world_cup: "1930",
    teams: {
         North_America: 1,
         South_America: 4,
         Europe: 8 
    }
}
// Case 1:
// if this be the object passed to setState
var updated_game_item1 = {
    game: "football",
    first_world_cup: "1930",
    teams: {
         North_America: 1,
         South_America: 4,
         Europe: 8 
    }
}
shallowCompare(updated_game_item1, game_item); // true - meaning the state
                                               // will update.

// Case 2:
// if this be the object passed to setState
var updated_game_item2 = {
    game: "football",
    first_world_cup: "1930",
    teams: game_item.teams
}
shallowCompare(updated_game_item2, game_item); // false - meaning the state
                                               // will not update.

// Case 3:
// if this be the object passed to setState
var updated_game_item3 = {
    first_world_cup: 1930
}
shallowCompare(updated_game_item3, game_item); // true - will update
```