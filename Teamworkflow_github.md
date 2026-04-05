When you're working with a team, Git gets a bit more involved (and we'll cover more of this in part 2 of this course). Here's what I do:

Update my local main branch with git pull origin main
Checkout a new branch for the changes I want to make with git switch -c <branchname>
Make changes to files
git add .
git commit -m "a message describing the changes"
git push origin <branchname> (I push to the new branch name, not main)
Open a pull request on GitHub to merge my changes into main
Ask a team member to review my pull request
Once approved, click the "Merge" button on GitHub to merge my changes into main
Delete my feature branch, and repeat with a new branch for the next set of changes

What to Ignore in .gitignore:
Ignore things that can be generated (e.g. compiled code, minified files, etc.)
Ignore dependencies (e.g. node_modules, venv, packages, etc.)
Ignore things that are personal or specific to how you like to work (e.g. editor settings)
Ignore things that are sensitive or dangerous (e.g. .env files, passwords, API keys, etc.)