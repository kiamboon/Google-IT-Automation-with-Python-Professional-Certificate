# Introduction to Git and GitHub
#### Course 3 of 6 in Google IT Automation with Python Professional Certificate

<br>

## Week 1: Introduction to Version Control
* Course Introduction
* Before Version Control
* Version Control Systems
* Using Git
* Module Wrap Up

## Week 2: Using Git Locally
* Advanced Git interaction
* Undoing Things
* Branching and Merging
* Module Wrap Up

## Week 3: Working with Remotes
* Introduction to GitHub
* Using a Remote Repository
* Solving Conflicts
* Module Review

## Week 4: Collaboration
* Pull Requests
* Code Reviews
* Managing Projects
* Module Review
* Course Wrap Up

<br>

========================================================================================

# Ultimate Git Cheat Sheet



## Configuring our Git 

| Syntax | Description |                        
| :--- | :--- |                                                                                
| $ git config --global user.name "Username" | Sets the name you want attached to your commit transactions |          
| $ git config --global user.email "Email" | Sets the email you want attached to your commit transactions |             
| $ git config --global color.ui auto | Colorization of command line output |                                 

	
 ## Creating Repository

| Syntax | Description |                        
| :--- | :--- |                                                                                
| $ git init | Turn an existing directory into a git repository |          
| $ git clone [url] | Clone a repository that already exists on GitHub |             


 ## Operations on Files

| Syntax | Description |                        
| :--- | :--- |                                                                                
| $ git add <filename> | Adds a file to Staging area |          
| $ git add * | Adds all files to Staging area | 
| $ git commit -a | Stages files automatically |
| $ git log -p | Produces patch text |
| $ git show | Shows various objects |
| $ git diff | Can show the differences in various commits |
| $ git diff --staged | Show all staged files compared to the named commit |
| $ git add -p | Allows a user to interactively review patches to add to the current commit |
| $ git mv | Moves a file |
| $ git rm | Removes a file |
	

## Reverting Changes 

| Syntax | Description |                        
| :--- | :--- |                                                                                
| $ git reset | Resets the repo, throwing away some changes |          
| $ git commit --amend |  Make changes to commits |             
| $ git revert  | New commit which effectively rolls back a previous commit |


 ## Branches

| Syntax | Description |                        
| :--- | :--- |                                                                                
| $ git branch | Used to manage branches |          
| $ git branch <name> | Creates the branch | 
| $ git branch -d <name> | Deletes the branch |
| $ git branch -D <name> | Forcibly deletes the branch |
| $ git checkout <branch> | Switches to a branch |
| $ git checkout -b <branch> | Creates a new branch and switches to it |
| $ git merge <branch> | Merge joins branches together |
| $ git merge --abort | abort the merge action (In case of merge conflict) |
| $ git log --graph --oneline | This shows a summarized view of the commit history for a repo |
	

## Interaction with Remote Repository

| Syntax | Description |                        
| :--- | :--- |                                                                                
| $ git push | Git push is used to push commits from your local repo to a remote repo |          
| $ git pull | Git pull is used to fetch the newest updates from a remote repository |  


 ## Remotes

| Syntax | Description |                        
| :--- | :--- |                                                                                
| $ git remote | Lists remote repos |          
| $ git remote -v | List remote repos verbosely | 
| $ git remote show <name> | Describes a single remote repo |
| $ git remote update | Fetches the most up-to-date objects |
| $ git fetch | Downloads specific objects |
| $ git branch -r | Lists remote branches; can be combined with other branch arguments to manage remote branches |


## Credit
* [Coursera - Introduction to Git and GitHub](https://www.coursera.org/learn/introduction-git-github)
