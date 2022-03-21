#!/bin/bash

DIR=$1
FILE=$2

mkdir -p "$DIR"
touch "$DIR/$FILE"
code "$DIR/$FILE"
