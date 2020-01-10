# Release Note

## New ref API

### forwrardRef

HOC에서 ref가 필요할 때 사용할 수 있다.
(Please see example about styled component in react document)

### createRef

이제, createRef를 통해 보다 명확하게 ref를 생성할 수 있다.

## ref Example

https://github.com/Hacker0x01/react-datepicker/issues/862

```
Building on @mfalade and @hiranvikas77, a full example:

BTW: Works flawlessly if you want to use Reactstrap. Just import Input from reactstrap/lib/Input, then replace input with Input. Of course the popup styles are a bit different.

import React, { forwardRef, useState } from 'react'
import DatePicker from 'react-datepicker'
import 'react-datepicker/dist/react-datepicker.css'

function Example() {
  const [startDate, setStartDate] = useState(new Date())
  const ref = React.createRef()
  const CustomDateInput = forwardRef(({ onClick, value }, ref) => (
    <input onClick={onClick} value={value} onChange={onClick} ref={ref} />
  ))
  return (
    <DatePicker
      selected={startDate}
      onChange={date => setStartDate(date)}
      customInput={<CustomDateInput ref={ref} />}
    />
  )
}

export default Example
```
