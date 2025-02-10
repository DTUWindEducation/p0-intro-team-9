1.	What is the difference between git and GitLab?
- Git is a version control system (VCS) that tracks code changes.
- GitLab is a Git repository management service with a web interface, CI/CD, and collaboration tools.
2.	What is the difference between GitLab, GitHub, and BitBucket?  
3.	Why would I ever want to use git, but not GitLab?  
4.	What are the steps to update the GitLab server with some changes I made on my computer? 
git checkout <branch-name>
git pull origin <branch-name>
git add .
git commit -m "Description of changes"
git push origin <branch-name> 
5.	What is a branch and why would I use one?  
6.	How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?  
7.	Give an example of a set of git commands that would result in a merge conflict.  
git checkout -b feature-branch
echo "Hello" > file.txt
git commit -m "Change 1"
git push origin feature-branch
8.	Is Git suitable for latex documents?  
9.	Should I from now on version my word and powerpoint slides using git? Why/why not?  
10.	What could happen when I push my latest commit to the remote repository without pulling first?
- May cause rejection if remote has new commits.
- Use git pull --rebase before pushing.  
11.	What happens when I pull without commiting my local changes first?  
12.	What is the difference between branching and forking?