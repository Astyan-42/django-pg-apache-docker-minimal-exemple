#!/bin/env bash
psql -U postgres -c "CREATE USER $POSTGRES_USER PASSWORD '$POSTGRES_PASSWORD'"
psql -U postgres -c "CREATE DATABASE $POSTGRES_NAME OWNER $POSTGRES_USER"