# Force Client Render Only

## Problem

You may use various react libraries.

However, unfortunately there may some problem with that.

Actually, in case of large scale library,

* [react-codemirror](https://github.com/JedWatson/react-codemirror)
* [react-ace](https://github.com/securingsincity/react-ace)

They use many things as full as possible like below.

* `window property`

So, those things may make some compfliction with your base library that support server-side rendering

* [react-starter-kit](https://github.com/kriasoft/react-starter-kit/)

## Solution

The best thing you can do is only render those additional library on client-side.

```javascript
import React, { PropTypes } from 'react';

class MyComponent extends React.Component {

  constructor(props) {
    super(props);
    this.state = {appIsMounted: false};
  }

  componentDidMount() {
    requestAnimationFrame(() => {
      this.setState({ appIsMounted: true });
    });
  }

  render() {
    return (
      <div>
      { this.state.appIsMounted
        && React.createElement(
          require('../../client-side-only').default
        )
      }
      </div>
    );
  }
}
```

from [react-starter-kit/issue](https://github.com/kriasoft/react-starter-kit/issues/186)