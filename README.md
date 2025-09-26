# Python Software Verband

This is the repository for the [Python Software Verband](https://python-verband.org) website.

## Contribute

### Content

#### USPs

The main USPs on the homepage are actually blog posts that have their **show_on_homepage** flag set to true.

You can further control if the usp should be on the left or right by setting the **highlighted** flag on the blog post (True = left).

### Local Setup

You don't need anything specific except for your normal python installation to setup your development environment.

1. Make sure you have the python version specified in `.python-version`.
2. `python -m venv ./venv && source venv/bin/activate` to setup a virtual environment and activate it
3. `pip install -r requirements.txt` to install the dependencies
4. `make run` to launch the development server.
5. You can visit the website on localhost:5001

### Deployment

### Recreating the Deployment Target on S3

Here are the steps to create the cloud setup on S3 in case you need to recreate it, or you want to use a similar setup for your own website.

The site is hosted as a static site on AWS/S3.

To (re-)create the S3 bucket setup in the eu-central-1 region, run the following:

Prerequisites:
- aws-cli
- aws credentials that allow you to create and manage S3 buckets

Create the bucket:
```bash
aws s3api create-bucket --bucket <bucket-name> --region eu-central-1 --create-bucket-configuration LocationConstraint=eu-central-1
```

Allow policies to set public access:
```bash
aws s3api put-public-access-block --bucket <bucket-name> --public-access-block-configuration "BlockPublicPolicy=false"
```

Check that the settings are correct:
```bash
aws s3api get-bucket-ownership-controls --bucket <bucket-name>
```

Allow public read through policy.

```bash
aws s3api put-bucket-policy --bucket <bucket-name> --policy '{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::'<bucket-name>'/*"

            ]
        }
    ]
}'
```

Copy website to s3:
```bash
aws s3 cp tmp s3://<bucket-name>/ --recursive
```

Set index:
```bash
aws s3 website s3://<bucket-name> --index-document index.html
```


Confirm the results:
```bash
curl <bucket-name>.s3-website.eu-central-1.amazonaws.com
```

AWS provides in-depth guides on how to setup SSL and your domain, check it out on the buckets' page:
https://eu-central-1.console.aws.amazon.com/s3/buckets/<bucket-name>?region=eu-central-1&bucketType=general&tab=properties

