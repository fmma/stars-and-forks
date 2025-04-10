# AI inference - Stars and forks

This repo can fetch data from GitHub APIs stargazers and forks and generate plots.

Plots are available here: ![GitHub star and fork count](plots.md).

## Regenerate

Data files are not overridden once fetched. If you wish to re-fetch data for a
repo. Delete the corresponding file `data/<REPO>.json`.

### Prerequisites
```
python -m venv .venv --prompt ai-stars-and-forks
. .venv/bin/activate
pip install -r requirements.txt
```

The list of repos to fetch data for are defined in `params.py`. Modify it to
add/remove the repos you want to fetch data and generate plots for. Additionaly, from and two dates (quarters) are defined here.

### Steps

1. Fetch data. This step is slow.

```
python fetch-data.py
```

2. Generate plots:
```
python gen-plots.py
```

3. Generate markdown file:
```
python gen-md.py
```

### Known issues

GitHubs stargazars API is capped at 40000 stars. This means that PyTorch,
TensorFlow, llama.cpp, and Keras cannot get star count data above this number.