# BASH NOTES

## Navigation

- pwd	| print working directory
- cd	| change directory
- ls	| list
	- -a	| all
	- -l	| info
	- -m	| single line
### File Paths
- Absolute Path - Entire path from root to working directory
- Relative Path - From working directory, relative path to destination
- Shorthands
	- /	| root
	- ~	| home (/c/Users/itsto)
	- ./	| current directory
	- ../	| parent directory

## File/Folder Management

### Create
- mkdir	| make directory
- touch | make file
- echo	| output to stream
	- \>	| overwrite contents in destination
	- \>\>	| append to contents in destination
- cat	| 

### Edit
- nano	| edit file
	- ^	| Ctrl
	- M	| Alt
- mv	| move
- cp	| copy

### Delete
- rm	| remove
	- -r	| remove everything
	- -f	| ignore warnings (avoid using)
- rmdir	| remove directory

## Utility
- clear	| clear previous outputs
- which	| show where command is installed

## Git
learngitbranching.js.org

### Repo Initialization
- git clone `link`	| clones repo to local machine at current location

### Utility
- git status		| current branch, commit history, local changes
- git tag `name` `ref`	| give a more permanent label to a commit than a branch reference
- git describe `ref`	| describe path to closest ancestor tag from ref (default HEAD)

### Changes
- git add `file`		| add local changes to a commit
- git rm --cached `file`	| remove file from commit
- git commit -m `msg`		| stage commit
- git push			| push staged commits to remote repo
- git reset HEAD~`n`		| moves branch reference back `n` commits, rewrites commit history
- git revert HEAD		| appends commit that reverse changes of previous commit

### Syncing
- git fetch	| check for changes to origin
- git pull	| copy changes from origin

### Branching
- git rebase `branch`		| takes commits from current branch and appends them to commits of `branch`
	- -i				| interactive, opens file editor to pick which commits in which order with changes to do
- git merge `branch`		| merges `branch` into current branch
- git checkout HEAD^		| detaches HEAD from branch and points it to parent commit of branch, similar to branch -f
- git branch -f `branch`~`n`	| moves `branch` reference to current HEAD, branch names, and commit hashes can be used interchangeably, ~`n` denotes n generations back
- git cherry-pick `ref1`...	| select however many references to be appended to current branch
