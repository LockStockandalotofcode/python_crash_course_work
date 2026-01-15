import requests

# Make an API call and check the response.
#   Correct API call: 
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars:>10000&sort=stars&order=desc"

headers = {'Accept': "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert response object to a directory.
response_dict = r.json()

# # Process results
# print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore info about repos.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repo.
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
print("\nSelected informatioin about each repository:")
for repo_dict in repo_dicts:
    print(f"Repo Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}\n")