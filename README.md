### Portfolio

# How to update the proects status and generate a new portfolio

1. Open and update the ```project.csv```


2. Generate the new portfolio

```bash 
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 generate.py
```

3. Upload

```bash 
git commit -am'update' 
git push
```