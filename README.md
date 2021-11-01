Python Softwareverband Website
================================

## Install

### Conda

    conda create -f environment.yml

### Virtualenv

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt


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
The website is hosted on S3, www/* needs to be uploaded to S3, requires access token.  


---

## Future stuff

### Preparation
- A developer account for the Twitter API
- An app registered for this developer account
- Save consumer_key and consumer_secret in `config.py`
- Keep `config.py` private!

###### Authorizing the App

To access and act for an Twitter account, the app needs to be authorized.

Run `manually_authorize_app.py`  via the console

```bash
python  manually_authorize_app.py  consumer_key consumer_secret
```
Follow the instructions on the terminal.
Save `access_token` and `access_token_secret` in `config.py`.


##### Card Validators
- [Facebook]( https://developers.facebook.com/tools/debug/sharing/)
- [LinkedIn]( https://www.linkedin.com/post-inspector/inspect/)
- [Twitter]( https://cards-dev.twitter.com/validator)


## Known Caveats

### Do not use `class` `stretched-link`
This class is buggy and extends the link beyond the scope, e.g. to the complete `<container` (containing other links).
