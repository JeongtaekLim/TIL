# DockerTimeout
```
/home/__user/compilebox/API/DockerTimeout.sh 20s -u mysql -e 'NODE_PATH=/usr/local/lib/node_modules' -i -t -v  "/home/__user/compilebox/API/temp/1870302ea341a736bb39":/usercode virtual_machine /usercode/script.sh python file.py
```

```
#!/bin/bash
set -e

to=$1
shift

cont=$(docker run --rm -d "$@")
code=$(timeout "$to" docker wait "$cont" || true)
docker kill $cont &> /dev/null
echo -n 'status: '
if [ -z "$code" ]; then
    echo timeout
else
    echo exited: $code
fi

echo output:
# pipe to sed simply for pretty nice indentation
docker logs $cont | sed 's/^/\t/'

docker rm $cont &> /dev/null
```

## set -e
from [bash docs](http://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html#The-Set-Builtin), it means
```
-e
Exit immediately if a pipeline (see Pipelines), which may consist of a single simple command (see Simple Commands), a list (see Lists), or a compound command (see Compound Commands) returns a non-zero status. The shell does not exit if the command that fails is part of the command list immediately following a while or until keyword, part of the test in an if statement, part of any command executed in a && or || list except the command following the final && or ||, any command in a pipeline but the last, or if the command’s return status is being inverted with !. If a compound command other than a subshell returns a non-zero status because a command failed while -e was being ignored, the shell does not exit. A trap on ERR, if set, is executed before the shell exits.

This option applies to the shell environment and each subshell environment separately (see Command Execution Environment), and may cause subshells to exit before executing all the commands in the subshell.

If a compound command or shell function executes in a context where -e is being ignored, none of the commands executed within the compound command or function body will be affected by the -e setting, even if -e is set and a command returns a failure status. If a compound command or shell function sets -e while executing in a context where -e is ignored, that setting will not have any effect until the compound command or the command containing the function call completes.
```

## "#@"

this means
```
./someScript.sh foo bar
```
and then inside `someScript.sh` reference:
```
umbrella_corp_options "$@"
```
from [stack overflow](http://stackoverflow.com/questions/9994295/what-does-mean-in-a-shell-script)

## $1

These are positional arguments of the script.

Executing

```
./script.sh Hello World
```

will make

```
$0 = script.sh
$1 = Hello
$2 = World
```
from [stack overflow](http://stackoverflow.com/questions/29258603/what-do-0-1-2-mean-in-shell-script)

## shift
An Example script:
```
#!/bin/bash
echo "Input: $@"
shift 3
echo "After shift: $@"
```
Run it:
```
$ myscript.sh one two three four five six

Input: one two three four five six
After shift: four five six
```
This shows that after shifting by 3, `$1=four`, `$2=five` and `$3=six`.
from [stack overflow](http://stackoverflow.com/questions/10414391/shell-shift-procedure-what-is-this)