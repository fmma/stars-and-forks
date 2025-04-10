from params import repos_frameworks, repos_langs, repos_models
from utils import repo_to_file_name

cols = 3

def write_section(header, repos, cols, f):
    count = 0
    str1 = " |" * cols 
    str2 = "---|" * cols
    
    f.writelines([
        f"## {header}\n",
        "\n",
        f"|{str1}\n",
        f"|{str2}\n",
        "| "
    ])
    for repo in repos:

        base_filename = repo_to_file_name(repo)
        fig_filename = f'figs/{base_filename}.png'

        count += 1
        if count == cols:
            f.writelines([f"![]({fig_filename}) |\n| "])
            count = 0
        else:
            f.writelines([f"![]({fig_filename}) | "])
            
    f.writelines([
        "\n\n"
    ])


with open('plots.md', 'w', encoding='utf-8') as f:
    
    f.writelines([
        "# Stars and forks\n",
        "\n"
    ])
    write_section("Frameworks", repos_frameworks, cols, f)
    write_section("Languages", repos_langs, cols, f)
    write_section("Models", repos_models, cols, f)
    