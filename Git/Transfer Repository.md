# Transfer Repositry (from Bitbucket to Github)

https://gist.github.com/mandiwise/5954bbb2e95c011885ff

// Reference: http://www.blackdogfoundry.com/blog/moving-repository-from-bitbucket-to-github/
// See also: http://www.paulund.co.uk/change-url-of-git-repository
```
$ cd $HOME/Code/repo-directory
$ git remote rename origin bitbucket
$ git remote add origin https://github.com/mandiwise/awesome-new-repo.git
$ git push origin master

$ git remote rm bitbucket
```