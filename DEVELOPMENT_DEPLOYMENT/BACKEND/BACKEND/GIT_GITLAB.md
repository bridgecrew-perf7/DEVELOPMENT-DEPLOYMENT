# Git Gitlab CI/CD Commitment Kit

_Always use oh my zsh shell_
_Always use https://dangitgit.com/_
_understand it's for parallel file development and versioning_
_Diff3 and Git is for text file comparison. Agile is for segmentation of product development stages with more than one developer_
_Stakeholder->ProductOwner->Team Lead->Single Developer_

GitLab wants to offer

- Documentation as Code
- Infrastructure as Code
- Operations as Code / GitOps
- ChatOps (with Mattermost integration)

git basics
```
* git init initialize git repo
* git commit
* git add adds changes to the stage
* a git history is just a linked list
* Git is good at isolating conflicts and fixing them automatically
* in the case of long-running features, we also want to merge the master in between
* Always resolve conflicts in the branch before the final merge
* Git remotes are very easy
* Never commit to Master branch
* Remotes are just branches
* never commit to master
* Rebase is a powerful tool

git init creates an empty repository
git status is our friend
git add adds the current snapshot in the working directory to the stage
git commit commits the current index as a new tree
git reset is a powerful command for moving branch markers
git checkout -b creates branch and checks it out directly
git merges can also be conflicting
git remote add adds a remote to the configuration
git push pushes local to remote
git fetch fetches everything from the remote that we don't already have
Fetched can be integrated with merge

git init creates a new Git repository in place

Each Git repository initially only exists locally

git add adds the current state of a file to the stage's working directory

git commit commits the contents of the stage

git branch creates a new branch label

git branch does not create a branch yet

git merge merges branches back together
a merge commit is required for branching strands
A fast-forward merge can be performed for non-branched strands

a .git subdirectory is created
this contains branch marks and the object store

git add adds a file content to the stage

git commit commits the current stage content

git reset moves branch brands

reset knows the modes --soft, --mixed and --hard

the default mode is --mixed

git branch creates a new branch label

git merge merges the state and history of another branch into the working branch

git init creates an empty repository

git add adds files to stage/index/cache

git branch creates new branch label

git checkout -b creates branch and checks it out

git merge is used to merge branches

git remote
```
git remote add adds a new Git remote repository to the configuration

git push pushes local objects and performs a remote merge
a new repository is created with git init
with git add you add the current state of the file to the stage (index/cache).
git commit commits the changes in the stage to the repository
with the parameter -a I can add changed tracked files directly to the stage and commit them

git branch creates a new branch label

git merge merges branches back together
you always merge into the current branch and only have to specify the source
with true history branching, the merge is done by a merge commit
without true denial of history, a fast-forward merge can be performed

git checkout -b creates a new branch and checks it out

git remote for a remote configuration to the repository
```

git diff
```
git diff [<options>] [<commit>] [--] [<path>…​]
git diff [<options>] --cached [--merge-base] [<commit>] [--] [<path>…​]
git diff [<options>] [--merge-base] <commit> [<commit>…​] <commit> [--] [<path>…​]
git diff [<options>] <commit>…​<commit> [--] [<path>…​]
git diff [<options>] <blob> <blob>
git diff [<options>] --no-index [--] <path> <path>
```

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
