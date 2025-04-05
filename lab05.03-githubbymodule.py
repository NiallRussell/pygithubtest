import requests
from github import Github
from config import config as cfg

apiKey = cfg["fullapi"]

g = Github(apiKey)

#for repo in g.get_user().get_repos():
    #print(repo.name)

repo = g.get_repo("NiallRussell/aprivateone")

#file = repo.get_contents("test.txt", ref = "main")

#repo.delete_file("test.txt", "delete test", sha = file.sha, branch = "main")
#with open("test.txt", "w") as file:

#data = "test"

#repo.create_file("test.txt", "upload test file", data, branch = "main")
                 
#print(repo.clone_url)

file_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url
print(url_of_file)


response = requests.get(url_of_file)
content_of_file = response.text
print(content_of_file)

new_contents = content_of_file + "more stuff /n"

print(new_contents)

github_reponse = repo.update_file(file_info.path, "updated by prog", new_contents, file_info.sha)

print(github_reponse)