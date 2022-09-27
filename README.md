# Room Assigner

Simple room assigner.  
Rooms are determined by votes.  
See `config_template.yaml` file for more.  

Returns the optimal room assignments.  
Every room assignment has a score which is the sum of the votes assigned by members. A vote will be added in the room assignment score if and only if the voter is in the same room of member he voted for.  
The score is computed for every room assignment possible. The top 10 rooms are then sorted by score descending and shown.  
This algorithm for finding the best room assignement is not very efficient, but for a small number of members and rooms it's feasible on modern hardware.  

## Requirements
It requires Python3 and pip for dependencies.  
Check python installation and version:  
```
$ python --version
Python 3.10.5
```

## Install
Clone repository and instal dependencies:  
```
$ git clone https://github.com/mircopergreffi/room-assigner
$ cd room-assigner
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
Execute the following command to generate the leaderboard.  
```
$ python leaderboard.py
```
Results are saved in file `leaderboard.txt`.  

Members are ranked by how many votes they received.
