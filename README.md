# UDP_Assigned

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/MuntasirMac/udp_assigned.git
$ cd udp_assigned
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pipenv shell
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `pipenv`.

Once `pip` has finished downloading the dependencies:

Make a file named `.env` to configure with environment variables
Edit the `.env` file by following instructions from `.env_example` file
If you run other databases than `PostgreSQL`, edit the `port` and remove the number `5432`

Then follow these instructions to run the project

```sh
(env)$ cd src
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/api/v1/user/`.
