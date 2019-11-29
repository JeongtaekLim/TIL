# Introduction to React using typescript

original source: https://dev.to/bmcmahen/a-beginners-guide-to-using-typescript-with-react-7m6

## Standard javascript version

```js
import React from "react";
import PropTypes from "prop-types";

export function StandardComponent({ children, title = "Dr." }) {
  return (
    <div>
      {title}: {children}
    </div>
  );
}

StandardComponent.propTypes = {
  title: PropTypes.string,
  children: PropTypes.node.isRequired
};
```

## Typescript version

```ts
import * as React from "react";

export interface StandardComponentProps {
  title?: string;
  children: React.ReactNode;
}

export function StandardComponent({
  children,
  title = "Dr."
}: StandardComponentProps) {
  return (
    <div>
      {title}: {children}
    </div>
  );
}
```
