# variable

test.sh
```
#!/bin/bash
set -e
echo ls
echo $(ls)
```

```
user@localhost:~/compilebox$ ./test.sh
ls
API Arch.png LICENSE README.md Setup node_modules test.sh yarn.lock
```