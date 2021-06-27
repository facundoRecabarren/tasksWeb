The following project is a Web that lets you manage your tasks, like an agenda. It is made with HTML5, CSS, Bootstrap, JS and Django/Python.
If you want to try it, currently it is deployed on heroku (https://tasksprojectfacu.herokuapp.com/).
In case you want to download it you will need to set a value to the SECRET_KEY variable in settings.py. You can use "decouple" and .env file to store it, or set an environment variable in your OS.
To generate a value for that variable you can make:
  1- import secrets
  2- secrets.token_hex(24)
And copy the result.
