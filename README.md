# Introduction

This is a sample project just to illustrate the use of sockets in a chat application.

## Requirements
Please refer to the requirement.txt file


## Steps to remember
Command to freeze all requirements.

``` python -m pip freeze --all>requirements.txt```

Modify the setup.py file to required changes.

Command to build the project using wheel

``` python setup.py bdist_wheel ```

Copy the file in the newly created dist package.

``` file name will be what we gave in the setup.py file ```

TO test the wheel package, go to the folder where you pasted the new file into,
 and then run the pip install `filename` (flask_chat_app_jaggu4329-0.0.1-py3-none-any.whl)

```bash
pip install flask_chat_app_jaggu4329-0.0.1-py3-none-any.whl

Use pip install waitress to run webserver in production environment


```




## Future work
This project would add new UI screens, authentication mechanism and other required process soon.  