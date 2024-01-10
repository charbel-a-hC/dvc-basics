# dvc-basics
 Showing some Basics of DVC on a custom dataset.
 
 ## Basic Commands
 ### Setup from Poetry

```bash
poetry add dvc[s3]
```

```bash
poetry shell
```

### Add remote for data (SSH)

```bash
dvc remote add -d ssh-remote ssh://100.103.52.68:22/mnt/edge_ai/Active-Datasets/
dvc remote modify --local ssh-remote user youruser
dvc remote modify --local ssh-remote password userpassword
```

### Add data to be tracked

```bash
dvc add .\dcereijo-player-scores\
```

```bash
git add dcereijo-player-scores.dvc
```

```bash
git commit -m "Added dataset"
```

```bash
git push origin main
```
### Push Data to Remote

```bash
git add .\.dvc\
```

```bash
git commit -m "Added dvc config"
git push origin main
```

```bash
dvc push
```

```bash
dvc pull
```

### Change a csv from the data

```bash
mkdir tmp
cp .\dcereijo-player-scores\appearances .\tmp\
cat .\tmp\appearances >> .\dcereijo-player-scores\appearances
```

difference is in the .dvc file

### Push on remote storage and github

```bash
dvc add .\dcereijo-player-scores\
git add dcereijo-player-scores.dvc
git commit -m "Appearances data update"
git push origin main
dvc push
```

### Go back in time and checkout most recent commit to see data

```bash
git checkout HEAD~1 .\dcereijo-player-scores.dvc
```

```bash
dvc checkout
```

We have modified the dataset currently tracked using dvc checkout:

```bash
dir .\dcereijo-player-scores\
```

### Commit again

```bash
git commit -m "Reverted appearances changes"
git push origin main
```



### Accessing DVC files through other projects

list data tracked in a repo using DVC:

```bash
dvc list https://github.com/charbel-a-hC/ups-ml-football-player-value <optional_folder>
```

How to get a file posted in a repository using DVC:

```bash
dvc get https://github.com/charbel-a-hC/ups-ml-football-player-value dcereijo-player-scores
```

Also, to keep a .dvc file in your project and to keep track of where the data came from and if there's any update to the data:

```bash
dvc import https://github.com/charbel-a-hC/ups-ml-football-player-value.git dcereijo-player-scores/
```

this creates `dcereijo-player-scores.dvc` in your repo and is traced to the original dataset.

If any changes were made to the dataset we can check them out using:

```bash
dvc update .\dcereijo-player-scores.dvc
```



### Python API - Using data or model in a script

With the python api we can get specific data and use it in our current scope without saving it locally:

```bash
import dvc.api

with dvc.api.open(
    "dcereijo-player-scores/competitions.csv",
    repo= "https://github.com/charbel-a-hC/ups-ml-football-player-value.git"
) as fd:
    data = fd.read()

print(data)
```

good way to load a certain model into the current workspace. 



### More on ML Pipelines and MLOps

https://www.youtube.com/watch?v=71IGzyH95UY&t=103s&ab_channel=DVCorg
## TODO
- [ ] Host Dataset on Google Drive
- [ ] Version Google Drive Dataset
- [ ] Add model version control
