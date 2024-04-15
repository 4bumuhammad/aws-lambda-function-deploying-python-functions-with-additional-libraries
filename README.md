# &#x1F6A9; AWS Lambda : Deploying Python Functions with Additional Libraries in AWS Lambda.

&nbsp;

Reference : <br />
<!-- -   Docs | dev.aryya.id Swagger
    <pre>http://dev.aryya.id/#/default/get_dns_record_query</pre> 

-   YT | Mendeploy Python Function Dengan Library Tambahan di AWS Lambda | AWS Tutorial Bahasa Indonesia
    <pre>https://www.youtube.com/watch?v=PjKM2RyQ-v8</pre> -->

-   Docs | Working with .zip file archives for Python Lambda functions
    <pre>https://docs.aws.amazon.com/lambda/latest/dg/python-package.html</pre>

&nbsp;

&nbsp;

Endpoint source :
<pre>
    ❯ curl -X 'GET' \
    'https://us-central1-zeta-structure-296509.cloudfunctions.net/dns-record-query?record_name=detik.com&record_type=A' \
    -H 'accept: application/json'

    # response : 
        {"record_name":"detik.com","record_type":"A","result":["203.190.242.211","103.49.221.211"]}
</pre>

&nbsp;

Environment : 
<pre>
    ❯ python --version

        Python 3.10.3
</pre>

&nbsp;

Begin : 
<pre>
    ❯ mkdir dns-record-query

    ❯ cd dns-record-query

    ❯ touch lambda_function.py
</pre>

&nbsp;

<pre>
    ❯ python3 -m venv .venv

    ❯ source .venv/bin/activate

    ❯ pip install request

    ❯ pip list

        Package            Version
        ------------------ --------
        certifi            2024.2.2
        charset-normalizer 3.3.2
        idna               3.7
        pip                22.0.4
        requests           2.31.0
        setuptools         58.1.0
        urllib3            2.2.1    
</pre>

&nbsp;

**Code :**
<pre>
    ❯ vim lambda_function.py



        import json
        import requests

        def lambda_handler(event, context):
            response=requests.get("https://us-central1-zeta-structure-296509.cloudfunctions.net/dns-record-query?record_name={}&record_type={}")
            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }
</pre>

&nbsp;

To create the deployment package (virtual environment).
<pre>
    ❯ pip show requests

        Name: requests
        Version: 2.31.0
        Summary: Python HTTP for Humans.
        Home-page: https://requests.readthedocs.io
        Author: Kenneth Reitz
        Author-email: me@kennethreitz.org
        License: Apache 2.0
        Location: /Users/.../aws-lambda-function-deploying-python-functions-with-additional-libraries/dns-record-query/.venv/lib/python3.10/site-packages
        Requires: certifi, charset-normalizer, idna, urllib3
        Required-by:
</pre>

<pre>
    ❯ deactivate

    ❯ cd .venv/lib/python3.10/site-packages

    ❯ zip -r ../../../../../my_deployment_package.zip .
</pre>

<pre>
    ❯ cd ../../../../../

    ❯ ls -lah | grep -E '.zip|dns-record-query'
 
        drwxr-xr-x   5 &lt;user&gt;  staff   160B Apr 15 13:10 dns-record-query
        -rw-r--r--@  1 &lt;user&gt;  staff   6.6M Apr 15 13:11 my_deployment_package.zip

    ❯ zip -g ../my_deployment_package.zip lambda_function.py
    
        adding: lambda_function.py (deflated 29%)              
</pre>

<pre>

</pre>

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

&nbsp;

<div align="center">
    <img src="./gambar-petunjuk/well_done.png" alt="well_done" style="display: block; margin: 0 auto;">
</div> 

&nbsp;

---

&nbsp;

&nbsp;

<div align="center">
    <img src="./gambar-petunjuk/syukron.png" alt="syukron" style="display: block; margin: 0 auto;">
</div> 

&nbsp;

&nbsp;