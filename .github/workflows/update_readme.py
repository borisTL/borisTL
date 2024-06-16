import requests

LEETCODE_USERNAME = 'baltazavv35'

def get_leetcode_stats(username):
    url = f'https://leetcode-stats-api.herokuapp.com/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def update_readme(stats):
    with open('README.md', 'r') as file:
        readme_content = file.readlines()

    with open('README.md', 'w') as file:
        for line in readme_content:
            if line.strip().startswith('<!-- LEETCODE-STATS:START -->'):
                file.write(line)
                file.write(f"Total solved: {stats['totalSolved']}\n")
                file.write(f"Easy: {stats['easySolved']}\n")
                file.write(f"Medium: {stats['mediumSolved']}\n")
                file.write(f"Hard: {stats['hardSolved']}\n")
                file.write('<!-- LEETCODE-STATS:END -->\n')
            else:
                file.write(line)

if __name__ == '__main__':
    stats = get_leetcode_stats(LEETCODE_USERNAME)
    if stats:
        update_readme(stats)
