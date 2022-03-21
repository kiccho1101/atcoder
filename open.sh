#!/bin/bash

DIR=$1
FILE=$2
EXT=${3:-py}

FILENAME="$DIR/$FILE.$EXT"

mkdir -p "$DIR"
touch "$FILENAME"
code "$FILENAME"
