# Python Customer + Favorite Products REST API

#### An API for registering Customers and their Favorite Products.

## :bookmark: Summary
1. [Requirements](#ballot_box_with_check-requirements)
2. [Stack](#open_file_folder-stack)
3. [Setup and init API](#rocket-setup-and-init-api)
4. [Run Tests](#skull-run-tests)
5. [Authentication and Authorization](#lock-authentication-and-authorization)
6. [Documentation](#books-documentation)
7. [Contribuiting](#wrench-contribuiting)
8. [Author](#computer-author)
9. [License](#pencil-license)

## :ballot_box_with_check: Requirements
- :whale: [docker](https://www.docker.com/get-started)
- :octopus: [docker-compose](https://docs.docker.com/compose/install/)

## :open_file_folder: Stack
- :whale: Docker
- :octopus: Docker Compose
- :snake: Python 3
- :dolphin: MySQL 8.0
- :rocket: Django
- :gift: Django REST Framework

## :rocket: Setup and init API
```sh
$    cp .env.example .env # you can edit if necessary
$    docker-compose up
```

## :skull: Run Tests
##### Before run, make sure the API container is up
```sh
$    ./scripts/tests.sh run
```

#### To see coverage report
```sh
$    ./scripts/tests.sh coverage
     # After run this command, you can see the tests coverage in htmlcov/ folder
```

## :lock: Authentication and Authorization
- This API contains authentication and authorization. A default admin user is created using `.env` credentials, but you can create more users at [Django Admin](http://0.0.0.0:8000/admin/auth/user/) setting their API resource access.

- To authenticate on API, use `/auth/` resource, passing your username and password to retrieve a token.

## :books: Documentation
- To learn how to use the API, open [swagger file](docs/swagger.yml) in [Swagger Editor](https://editor.swagger.io)
- To speed up the use of API, use [postman requests collection](docs/api_doc.postman_collection.json)

## :wrench: Contributing
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/rafaeldias98/python-customer-api/issues/new)

If you find any problem or have a suggestion, please [open an issue](https://github.com/rafaeldias98/python-customer-api/issues/new).

## :computer: Author

* **Rafael Dias** - *Software Developer*

## :pencil: License

- This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
