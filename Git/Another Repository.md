# Another Repository

By [stack overflow](http://stackoverflow.com/questions/5181845/git-push-existing-repo-to-a-new-and-different-remote-repo-server), if you want to push some project from public repository to your private or group's repository, just follow below steps

```
1. Create a new repo at github.
2. Clone the repo from fedorahosted to your local machine.
3. $ git remote rename origin upstream
4. $ git remote add origin URL_TO_GITHUB_REPO
5. $ git push origin master
```

* create new branch
```
$ git checkout -b NEW_BRANCH_NAME
```
