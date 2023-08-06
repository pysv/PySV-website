Python Softwareverband Website
================================

## Install

### Conda

```bash
conda create -f environment.yml
```

### Virtualenv

 ```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Venv

for M1 mac

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt --use-feature=2020-resolver
pip install --force-reinstall MarkupSafe==2.0.1
   ```


## Edit Pages

    cd website
    lektor server

The local website is run on    
[http://localhost:5000](http://localhost:5000)

## Build Static Site

The rendered page is saveto to the www dirctory which is excluded from VC, make sure a www directory is available in project root.

    cd website
    lektor build --output-path ../www


## Adding more avatars
Create new avatars with the script below
The default avatar is defined in PySV-website.lektorproject

    
    avatar_creator/create_avatar.py
    


## Publishing
The website is hosted on S3, www/* needs to be uploaded to S3, requires access tokens. 

AWS Credentials are stored in the GitHub Secrets of this repository:
* AWS_ACCESS_KEY_ID  
* AWS_SECRET_ACCESS_KEY

### GitHub Actions

In the GitHub Actions tab there are two workflows:

- `staging.yml`: runs automatically on pull requests. Builds the website based on the last opened PR at: http://pysv-web-staging.s3-website.eu-central-1.amazonaws.com
- `production.yml`: builds the new website when something is pushed to the master branch at: http://pysv-web.s3-website.eu-central-1.amazonaws.com i.e. https://pysv.org



## Production



## Known Caveats

### Do not use `class` `stretched-link`
This class is buggy and extends the link beyond the scope, e.g. to the complete `<container` (containing other links).
