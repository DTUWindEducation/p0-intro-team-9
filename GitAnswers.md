1.	What is the difference between git and GitLab?
	Git is a version control system (VCS) that tracks code changes.
	GitLab is a Git repository management service with a web interface, CI/CD, and collaboration tools.

2.	What is the difference between GitLab, GitHub, and BitBucket?
	They are all git repository hosting services.
	GitLab is more secure than GitHub and better for projects with high sensibility info, for large DevOps and DevSecOps projects.
	GitHub is best for open source pand public projects.
	BitBucket: is a Git based source code repository hosting service owned by Atlassian. 

3.	Why would I ever want to use git, but not GitLab? 
	Git can be used offline and locally while gitlab cannot.

4.	What are the steps to update the GitLab server with some changes I made on my computer? 
	git checkout <branch-name>
	git pull origin <branch-name>
	git add 
	git commit -m "Description of changes"
	git push origin <branch-name> 

5.	What is a branch and why would I use one?
	Is a copy of the main repostory that generates in a parallel way. It is useful to work locally on the repo.

6.	How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?
	  
7.	Give an example of a set of git commands that would result in a merge conflict.  
	git checkout -b feature-branch
	echo "Hello" > file.txt
	git commit -m "Change 1"
	git push origin feature-branch

8.	Is Git suitable for latex documents?
	Git was not dessigned to be used on binnary files, since it does not track the changes very well.

9.	Should I from now on version my word and powerpoint slides using git? Why/why not?
	Word and powerpoint already have its own version control and automatically saves so it wouldn't make sense to version them.

10.	What could happen when I push my latest commit to the remote repository without pulling first?
	May cause rejection if remote has new commits.
	Use git pull --rebase before pushing.

11.	What happens when I pull without commiting my local changes first? 
	Git tries to fetch and merge the remote changes into your working branch. Depending on the state of your local repository, it can give a 	conflict trying to merge the files.

12.	What is the difference between branching and forking?
	Branching creates a branch within the repository while forking creates a branch outside of the repository.