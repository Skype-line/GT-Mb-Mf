import torch
import torch.nn as nn


class trans_model(nn.Module):
    def __init__(self, dim_state, dim_action):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(dim_state + dim_action, 128),
            nn.ReLU(),
            nn.Linear(128,64),
            nn.ReLU(),
            nn.Linear(64, dim_state)
        )

    def forward(self, x):
        return self.fc(x)


class reward_model(nn.Module):
    def __init__(self, dim_state, dim_action):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(dim_state + dim_action, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.fc(x)

class value_model(nn.Module):


    def forward(self, x):
        return torch.square(torch.norm(x,dim=len(x.size())-1))