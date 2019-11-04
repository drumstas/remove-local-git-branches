import subprocess

# subprocess.call(["git", "checkout", "master"])
branchesInBytes, errors = subprocess.Popen(["git", "branch"], stdout=subprocess.PIPE).communicate()
branches = branchesInBytes.decode("UTF-8").split("\n")
for branch in branches:
	if branch and not branch.startswith("*") and not branch.strip() == 'master':
		subprocess.call(["git", "branch", "-d", branch.strip()])