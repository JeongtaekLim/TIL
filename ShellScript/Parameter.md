# Parameter

when if you get some `path` parameter,

```
my.sh /usr/bin/
my.sh /usr/bin
```
you have to remove trailing `/`

```
path=${1%/}
```
see [here](http://www.network-theory.co.uk/docs/bashref/ShellParameterExpansion.html)