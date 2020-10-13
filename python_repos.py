import requests

# Make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)

# Store api response in a variable
response_dict= r.json()
#print("Total repositories :", response_dict["total_count"])
repo_dicts = response_dict['items']

# Explore information about the repositories.

#print("Repositories returned:", len(repo_dicts))

# Process results.
#print(response_dict.keys())


# Examine the first repository.
#repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#    print(key)

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])

# 417