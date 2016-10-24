import git 


def GitPull():

	repo = git.Repo()
	o = repo.remotes.origin
	o.pull()
	print 'Git pull successful.'

