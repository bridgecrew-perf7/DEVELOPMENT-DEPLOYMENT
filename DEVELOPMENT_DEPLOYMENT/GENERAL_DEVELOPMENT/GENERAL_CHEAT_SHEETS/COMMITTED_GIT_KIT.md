# Committed Git Kit

_use oh my zsh shell_
_understand it's for parallel file development and versioning_
_check out https://dangitgit.com/_

git rollback to first commit
```git
git rev-list --max-parents=0 --abbrev-commit HEAD
git reset --hard aa8119f
git push -f
```
preemptive git rollback
```
git commit --allow-empty --allow-empty-message -m ''
git tag -a -m '' ROOT
git reset --hard ROOT
```
from current head commit
```git
git branch <new-branch>
```
from other branch
```git
git branch <new-branch> <base-branch>
```
from commig
```git
git branch <new-branch> f71ac24d
```
from tag
```git
git branch <new-branch> v1.2
```
new branch from remote branch
```git
git branch --track <new-branch> origin/<base-branch>
git checkout --track origin/<base-branch>
```
new branch in remote repository
```git
git push -u origin <local-branch>
```
git house keeping
```git
git prune --progress
git gc --aggressive
```
delete tag locally:
```git
git tag -d <tag>
```
delete remotely:
```git
git push origin :refs/tags/<tag>
OR
git push --delete origin <tag>
```
Checkout to a new temporary branch
```
git checkout --orphan TEMP_BRANCH
```
Add all the files (If not added)
```
git add -A
```
Commit the changes in the temporary branch
```
git commit -am "Initial commit message"
```
Delete the old master branch
```
git branch -D master
```
Rename the new temporary branch to master
```
git branch -m master
```
At last, Force update to our repository
```
git push -f origin master
git reset --hard
git push -f
```
