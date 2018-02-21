# Front-End BinaryEdge Challenge

## Emails present in all dataleaks:

- example1@example.com
- example2@example.com
- example3@example.com
- example4@example.com
- example5@example.com

## How to run setup.sh

### Build docker image

$ ./setup.sh build

The 'build' parameter will build the docker container, migrate the database and
generate data to use in testing (e-mail's, domains and dataleaks).

In the end of the program the script will return 10 emails to use in further testing.

### Run server

To run server in port 8000:

$ ./setup.sh server

### Show all emails

The script will generate more than 10 emails (total of 1600 emails), to see all of them:

$ ./setup.sh show_emails

### Create user

To create a new user (we assume that the server is running):

$ ./setup.sh create_user

## Documentation

See docs folder to see API docs.

## How to use

- Don't forget to build the image first (it will create a new database with data).
- And now you can run the server.
- Then, create a user if you want or use: email@email.com and "reverse" as pwd.
- Login with the user credentials.
- Use the API with the returned Token.