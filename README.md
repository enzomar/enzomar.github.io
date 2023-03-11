### Portfolio

# How generate a new portfolio

## Nominal path

1. Clone this repository

2. Open and update the ```projects.csv```

3. Commit and push the changes

```bash 
git commit -am'update' && git push
```


## Developer path 

1. Clone this repository

2. Open and update the ```projects.csv```

3. Generate the new portfolio

```bash 
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 generate.py
```
4. Open the index.html and verify

5. Commit and push the changes

```bash 
git commit -am'update' && git push
```