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
- rmdir	| remove directory

## Utility
- clear	| clear previous outputs

## Git

- git clone `link`			| clones repo to local machine at current location
- git status				| current branch, commit history, local changes
- git add `file`			| add local changes to a commit
- git rm --cached `file`	| remove file from commit
- git commit -m `msg`		| stage commit
- git push					| push staged commits to remote repo
- git fetch					| check for changes to origin
- git pull					| copy changes from origin