# Home Credit Default Risk Challenge: Open Solution

[![Join the chat at https://gitter.im/minerva-ml/open-solution-home-credit](https://badges.gitter.im/minerva-ml/open-solution-home-credit.svg)](https://gitter.im/minerva-ml/open-solution-home-credit?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is an open solution to the [Home Credit Default Risk challenge](https://www.kaggle.com/c/home-credit-default-risk).

## The goal
Create (entirely) open solution to this competition. We are opening both the code and process. Check [issues](https://github.com/minerva-ml/open-solution-home-credit/issues) and our [project board](https://github.com/minerva-ml/open-solution-home-credit/projects/1). Rules are simple:
* Clean code and extensible solution leads to the reproducible experimentations and better control over the improvements.
* Open solution should establish solid benchmark and give good base for your custom ideas and experiments.

## Installation
### Fast Track
1. clone repository and install requirements (check _requirements.txt_)
1. register to the [neptune.ml](https://neptune.ml) _(if you wish to use it)_
1. run experiment based on [LightGBM and random search](https://github.com/minerva-ml/open-solution-home-credit/wiki/LightGBM-and-basic-features): `neptune run --config neptune_random_search.yaml main.py train_evaluate_predict --pipeline_name lightGBM`

### Step-by-step
1. clone this repository
```bash
git clone https://github.com/minerva-ml/open-solution-home-credit.git
```
2. install requirements in your Python3 environment
```bash
pip3 install requirements.txt
```
3. register to the [neptune.ml](https://neptune.ml) _(if you wish to use it)_
4. update data directories in the [neptune.yaml](https://github.com/minerva-ml/open-solution-home-credit/blob/master/neptune.yaml) configuration file
5. run experiment based on [LightGBM and random search](https://github.com/minerva-ml/open-solution-home-credit/wiki/LightGBM-and-basic-features):
```bash
neptune login
neptune run --config neptune_random_search.yaml main.py train_evaluate_predict --pipeline_name lightGBM
```
6. collect submit from `experiment_directory` specified in the [neptune.yaml](https://github.com/minerva-ml/open-solution-home-credit/blob/master/neptune.yaml)

## Get involved
You are welcome to contribute your code and ideas to this open solution. To get started:
1. Check [competition project](https://github.com/minerva-ml/open-solution-home-credit/projects/1) on GitHub to see what we are working on right now.
1. Express your interest in paticular task by writing comment in this task, or by creating new one with your fresh idea.
1. We will get back to you quickly in order to start working together.
1. Check [CONTRIBUTING](CONTRIBUTING.md) for some more information.

## User support
There are several ways to seek help:
1. Kaggle [discussion](https://www.kaggle.com/c/home-credit-default-risk/discussion/57175) is our primary way of communication.
1. Read project's [Wiki](https://github.com/minerva-ml/open-solution-home-credit/wiki), where we publish descriptions about the code, pipelines and supporting tools such as [neptune.ml](https://neptune.ml).
1. Submit an [issue]((https://github.com/minerva-ml/open-solution-home-credit/issues)) directly in this repo.
