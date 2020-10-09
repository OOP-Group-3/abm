# Agent-Based Model for Pandemic Simulation
OOP Project for Group 3. Agent-Based Model for Pandemic Simulation.

# Installation instructions:
First, press the fork button in the top right and fork the repo to your own GitHub accounts and then follow the instructions below:
```bash
cd <workdir>
git clone https://github.com/<your-github-user-name>/abm
git checkout -b new_branch
```
When working with the code, create a new branch **in your fork itself** and when you push, use the command:
```bash
git push --set-upstream origin <branch-name>
```
After this, open your GitHub and raise a PR. When you need to update your repo with the changes in the main repo.
```bash
git checkout <branch-you-are-working-in>
git fetch upstream
git merge upstream/main main
```
# Python Team Instructions:
- First, get Conda from either [Anaconda](https://www.anaconda.com/products/individual) (for Windows and Linux) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (mainly for Linux, there's some BT getting it to work on Windows). Use Miniconda if you can. Go through basic usage of Conda.

- Then we create the new conda env and get some basic packages installed. For now, we'll use Python 3.6 (might have to use old tools that need Python 3.6 only)
```bash
conda create -n abm python=3.6
conda activate abm
conda install numpy matplotlib pandas bokeh black flake8
python setup.py install
```
- Standard for installing packages using conda envs: Install everything you can with Conda first, then you use pip for the stuff you can't get on Conda.
- Before pushing any code, do `black abm` from the root folder.
- While coding, VS Code, will show you all the linting errors with `flake8`
- All folders must have a `__init__.py` for our repo to be a valid package.

# Version list

| Library    | Version |
| ---------- | ------  |
| Bokeh      | 0.12.14 |
| Django     | 2.2.1   |
| Jinja2     | 2.11.2  |
| python     | 2.8.1   |
