#!/bin/bash -e
run() {
    docker-compose exec api python3 manage.py test
}

coverage() {
    docker-compose exec api coverage run --source='./api' --omit="*/tests*,*/migrations*,*init*" manage.py test
    docker-compose exec api coverage html
}

help() {
    echo 'Available subcommands: run'
}

[[ -z $@ ]] && (help ; exit 1)
$@
