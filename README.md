# MBMF Combination Via Value Expansion #

## 1.Description ##
Reinforcement learning (RL) algorithms have been shown to be ca-pable of learning a wide range of robotic skills. They are divided intotwo categories: model-basedRLand model-freeRL. In this project, we propose our method that could gradually transform a model-based RL training framework to a model-free actor-critic ar-chitecture such as Deep Deterministic Policy Gradient (DDPG).
[image of framework]
(https://github.com/clthegoat/DL_MBMF/blob/main/experiment/assets/framework_reduction.png)

## 2.Getting started ##
Run the following commands to install this repository and the required dependencies:
```
git clone https://github.com/clthegoat/DL_MBMF.git
pip3 install -r requirements.txt
```
You can run the experiment on the simplest environment 'Pendulum-v1' after installing the required packages, but if you want to run experiments on other more complicated environment, please install mujoco_py [here](https://github.com/openai/mujoco-py). You can run code as follows:
```
cd experiment
python MBMF.py --conf configs/MBMF_Pendulum --type [type name]
```

