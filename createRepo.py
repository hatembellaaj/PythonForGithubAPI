from github import Github

#generated access token
access_token ="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"

#login into github account
login  = Github(access_token)

#get the user
user  = login.get_user()

repository_name= "Dorra-Repo"

#create repository
new_repo = user.create_repo(repository_name)

#create new file
new_repo.create_file("New-File.txt", "new commit", "Data Inside the File")