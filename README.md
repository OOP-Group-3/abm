# Agent-Based Model for Pandemic Simulation
OOP Project for Group 3. Agent-Based Model for Pandemic Simulation.

# Installation instructions:
## Common stuff:
```bash
cd <workdir>
git clone https://github.com/OOP-Group-3/abm
git checkout -b new_branch
```
## Python:
First, get Conda from either [Anaconda](https://www.anaconda.com/products/individual) (for Windows and Linux) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (mainly for Linux, there's some BT getting it to work on Windows). Use Miniconda if you can. Go through basic usage of Conda.

Then we create the new conda env and get some basic packages installed. For now, we'll use Python 3.6 (might have to use old tools that need Python 3.6 only)
```bash
conda create -n abm python=3.6
conda install numpy matplotlib pandas bokeh black flake8
python setup.py install
```

Standard for installing packages using conda envs: Install everything you can with Conda first, then you use pip for the stuff you can't get on Conda.

Before pushing any code, do `black abm` from the root folder.
