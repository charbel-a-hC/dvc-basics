import dvc.api

with dvc.api.open(
    "dcereijo-player-scores/appearances.csv",
    repo= "https://github.com/charbel-a-hC/ups-ml-football-player-value.git"
) as fd:
    data = fd.read()

print(data)