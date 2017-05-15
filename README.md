python-λ
========

Python-lambda is a toolset for developing and deploying *serverless* Python code in AWS Lambda.

Description
===========

AWS Lambda is a service that allows you to write Python, Java, or Node.js code that gets executed in response to events like http requests or files uploaded to S3.

Working with Lambda is relatively easy, but the process of bundling and deploying your code is not as simple as it could be.

The *Python-Lambda* library takes away the guess work of developing your Python-Lambda services by providing you a toolset to streamline the annoying parts.

Requirements
============

* Python 3.6
* Pip (~8.1.1)
* Virtualenv (~15.0.0)
* Virtualenvwrapper (~4.7.1)

Getting Started
===============

Begin by creating a new virtualenv and project folder.

```bash
  $ virtualenv -p python3 pylambda
  $ source pylambda/bin/activate
```

Next, download *Python-Lambda* using pip via Github.

```bash
  (pylambda) $ pip install git+https://github.com/jgillard/python-lambda
```
From your ``pylambda`` directory, run the following to bootstrap your project.

```bash
  (pylambda) $ lambda init
```

This will create the following files: ``event.json``, ``__init__.py``, ``service.py``, and ``config.yaml``.

Next let's open ``service.py``, in here you'll find the following function:

```python
  def handler(event, context):
    # Your code goes here!
    e = event.get('e')
    pi = event.get('pi')
    return e + pi
```

This is the handler function; this is the function AWS Lambda will invoke in response to an event. You will notice that in the sample code ``e`` and ``pi`` are values in a ``dict``. AWS Lambda uses the ``event`` parameter to pass in event data to the handler.

So if, for example, your function is responding to an http request, ``event`` will be the ``POST`` JSON data and if your function returns something, the contents will be in your http response payload.

Next let's open the ``event.json`` file:

```json
  {
    "pi": 3.14,
    "e": 2.718
  }
```

Here you'll find the values of ``e`` and ``pi`` that are being referenced in the sample code.

If you now try and run:

```bash
  (pylambda) $ lambda invoke -v
```

You will get:

```bash
  # 5.858

  # execution time: 0.00000310s
  # function execution timeout: 15s
```

As you probably put together, the ``lambda invoke`` command grabs the values stored in the ``event.json`` file and passes them to your function.

The ``event.json`` file should help you develop your Lambda service locally. You can specify an alternate ``event.json`` file by passing the ``--event-file=<filename>.json`` argument to ``lambda invoke``.

Testing
===============

```bash
  (pylambda) $ python -m pytest tests/
```

TODO: `lambda test` to wrap pytest

Deploying
===============

Copy the template Terraform from the Usage section here:

https://github.com/depop/depop-infrastructure/tree/master/modules/tf_community_modules/tf_aws_lambda#usage

There is also a scheduled Lambda function available:

https://github.com/depop/depop-infrastructure/tree/master/modules/tf_community_modules/tf_aws_lambda_scheduled#usage
