from pathlib import Path
import matplotlib.pyplot as plt
from params import repos, min_quarter, max_quarter, max_count, min_quarter_plot
from utils import inc_quarter, read_json, repo_to_file_name, generate_quarters

Path('figs').mkdir(parents=True, exist_ok=True)

x_axis = list(generate_quarters(min_quarter, inc_quarter(max_quarter)))

offset = x_axis.index(min_quarter_plot)

for repo in repos:

    base_filename = repo_to_file_name(repo)
    filename = f'data/{base_filename}.json'
    fig_filename = f'figs/{base_filename}.png'
    
    if not Path(filename).exists():
        print("WARNING", filename, 'DOES NOT EXIST')
        continue
    
    json_data = read_json(filename)
    stars_accum = json_data['stars_accum']
    forks_accum = json_data['forks_accum']
    ax = plt.gca()
    
    ax.set_ylim([0, max_count])
    
    stars = []
    forks = []
    last_star_count = 0
    last_fork_count = 0
    for quarter in x_axis:
        if quarter in stars_accum:
            star_count = stars_accum[quarter]
            last_star_count = star_count
            stars.append(star_count)
        else:
            stars.append(last_star_count)
            
        if quarter in forks_accum:
            fork_count = forks_accum[quarter]
            last_fork_count = fork_count
            forks.append(fork_count)
        else:
            forks.append(last_fork_count)

    plt.bar(x_axis[offset:], stars[offset:], label='# Stars')
    plt.bar(x_axis[offset:], forks[offset:], label='# Forks')
    
    plt.title(repo)
    leg = plt.legend(loc='upper center')
    plt.xticks(rotation=90)
    plt.subplots_adjust(top=0.925, 
                        bottom=0.20, 
                        left=0.1, 
                        right=0.90, 
                        hspace=0.01, 
                        wspace=0.01)

    plt.savefig(fig_filename)
    plt.clf()

    print("PLOT SAVE", fig_filename)
