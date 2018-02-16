# Front-End BinaryEdge Challenge

## How to run setup.sh

### Build docker image

$ ./setup.sh build

The 'build' parameter will build the docker container, migrate the database and
generate data to use in testing (e-mail's, domains and dataleaks).

In the end of the program the script will return 10 emails to use in further testing.

### Show all emails

The script will generate more than 10 emails, to see all of them:

$ ./setup.sh show_emails

### Run server

To run server in port 8000:

$ ./setup.sh server

### Create user

To create a new user:

$ ./setup.sh create_user

## Documentation

See docs folder to see API docs.

## How to use

- Don't forget to build the image first (it will create a new database with data).
- Then, create a user.
- And now you can run the server.
- Login with the created user.
- Use the API with the returned Token.