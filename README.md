# Room Assigner

Simple room assigner.  
Rooms are determined by votes.  
See `config_template.yaml` file for more.  

## Requirements
It requires Python3 and pip for dependencies.  
Check python installation and version:  
```
$ python --version
Python 3.10.5
```

Install dependencies:  
```
$ python -m pip install -r requirements.txt
```

## Run
Execute the following command:  
```
$ python main.py
```
Results are saved in `results.txt`.  

## Leaderboard
See who is the most popular.  
Execute this command to generate the leaderboard.  
```
$ python leaderboard.py
```
Results are saved in file `leaderboard.txt`.  

Members are ranked by how many votes they recived.
