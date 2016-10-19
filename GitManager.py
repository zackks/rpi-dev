import git 


def GitPull():

	repo = git.Repo()
	o = repo.remotes.origin
	o.pull()
	print 'Git pull successful.'

def GitPush():
	repo = git.Repo()
	o = repo.remotes.origin
	o.push()
