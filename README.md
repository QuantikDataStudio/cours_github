# Cours GitHub Ada

Premier fichier ajouté à Git.

Deuxième commit du cours pour apprendre la commande `git pull`.

Premier commit dans la branche `premiere_branche`

Apprendre à faire une pull request

Modification pour le rebase
Modification pour le rebase numero 2

Commit squash 1
Commit squash 2
Commit squash 3
1er commit dans la branche pycharm

### Description: Git add

The git add command stages changes (modified, new, or deleted files) to be committed in Git. It moves files from the working directory to the staging area, preparing them for a commit.

`git add <file-name>` : Stages a single file for commit.

`git add <file1> <file2>` :  Stages multiple specified files.

`git add .` : Stages all changed and new files in the current directory and subdirectories.


### Description: Git branch

`git branch` : List all local branches

`git branch -a` : List all local & remote branches

`git branch <branch-name>` : Create a new branch

`git branch -d <branch-name> ` : Delete a branch (Use -D to force delete)


### Description: Git commit

Saves staged changes to the repository's history.

`git commit -m "Your commit message"` : Commit staged files with a message:

`git commit` : Commit with a detailed message (Opens a text editor to write a detailed commit message)

`git commit --amend` : Amend the last commit (Modifies the last commit message or includes additional changes)

### Description: Sends committed changes to a remote repository.

`git push origin <branch-name>` : Push the current branch to remote:

`git push --all origin` : Push all branches

`git push --set-upstream origin <branch-name>` : Push and set upstream (track remote branch)
