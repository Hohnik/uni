# Git Cheatsheet


### Create the git repository

```bash
git init 	# Initialize the git repository
git branch -M main	# Rename the branch to 'main''
git remote add origin main <ssh githublink>	# Add the remote repository
git push --set-upstream origin main # Push to the remote repository
```

### Everyday commands

```bash
git status 	# Show all modified files
git log 	# Show all previous commits 

git add myfile.txt 	# ADD one file
git add . 		# ADD all files in the current folder recursively

git commit -m "your commit message" # Commit all modified files

git push 	# Push all commits to the remote repository 
```

### Workflow

```bash
git add .
git commit -m "create git cheatsheet"
git push
```

---

## Advanced commands

```bash
git branch <branchname>     # Create a new branch
git checkout <branchname>   # Use the branch
( git checkout -b <branchname>  # Both in one command )

git branch -l   # List all available branches
git branch -D   # Delete a branch

git merge <branchname>  # Merge a branch into the current
