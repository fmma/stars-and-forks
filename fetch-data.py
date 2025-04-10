import requests
from datetime import datetime
from pathlib import Path
from params import repos, max_quarter
from utils import datestring_to_quarter, write_json, generate_quarters, inc_quarter, repo_to_file_name

token = Path('.token').read_text()

def get_quarterly_counts(repo, endpoint, attribute):
    counts = {}
    url = f'https://api.github.com/repos/{repo}/{endpoint}?per_page=100&sort=newest'
    while url is not None:
        print('GET', url)
        r = requests.get(url, headers={
            'Accept':'application/vnd.github.v3.star+json',
            'Authorization':f'Bearer {token}'
        })
        
        for record in r.json():
            datestring = record[attribute]
            quarter = datestring_to_quarter(datestring)
            if quarter in counts:
                counts[quarter] += 1
            else:
                counts[quarter] = 1
        
        url = get_next_link(r)
    
    quarters = sorted(counts.keys())
    
    for quarter in generate_quarters(quarters[0], quarters[-1]):
        if quarter not in counts:
            counts[quarter] = 0

    accum_counts = {}
    sorted_counts = {}
    acc = 0
    for (quarter, n) in sorted(counts.items()):
        acc += n
        accum_counts[quarter] = acc
        sorted_counts[quarter] = n
        
        if quarter == max_quarter:
            break
    
    return sorted_counts, accum_counts

def get_stars(repo):
    return get_quarterly_counts(repo, 'stargazers', 'starred_at')

def get_forks(repo):
    return get_quarterly_counts(repo, 'forks', 'created_at')

def get_next_link(r):
    
    links = {}
    if 'Link' not in r.headers:
        return None
    for link_entries in r.headers['Link'].split(','):
        items = link_entries.split(';')
        url = items[0].strip()[1:-1]
        key = items[1].strip()
        links[key] = url
        
    return links['rel="next"'] if 'rel="next"' in links else None


Path('data').mkdir(parents=True, exist_ok=True)

for repo in repos:

    base_filename = repo_to_file_name(repo)
    filename = f'data/{base_filename}.json'
    
    if Path(filename).exists():
        print("SKIPPING", repo)
        continue
    
    stars, stars_accum = get_stars(repo)
    forks, forks_accum = get_forks(repo)

    write_json(filename, {
            'stars': stars,
            'stars_accum': stars_accum,
            'forks': forks,
            'forks_accum': forks_accum
        })
        
    print("WROTE", filename)
        
print("OK ALL DONE")
