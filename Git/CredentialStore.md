# Credential store

If you sick and tired of typing your password with git command,

```
$ git config credential.helper store
$ git push http://example.com/repo.git
Username: <type your username>
Password: <type your password>

[several days later]
$ git push http://example.com/repo.git
[your credentials are used automatically]
```
from [git docs - credential stroe](https://git-scm.com/docs/git-credential-store)