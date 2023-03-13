#!/usr/bin/env bash

changeset=$(git rev-parse --short HEAD)
timestamp=$(date +"%Y-%m-%dT%H:%M:%S%z")


echo -n "var version = \"" > version.js
echo -n $changeset >> version.js
echo -n "@" >> version.js
echo -n $timestamp >> version.js
echo -n "\";" >> version.js
