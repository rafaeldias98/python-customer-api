#!/bin/bash -e
run() {
    docker-compose exec api python3 manage.py test
}

help() {
    echo 'Available subcommands: run'
}

[[ -z $@ ]] && (help ; exit 1)
$@
