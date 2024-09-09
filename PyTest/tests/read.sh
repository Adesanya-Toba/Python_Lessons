#!/bin/bash
read -r -p "Are you sure (y/n)? " answer
echo "You typed": $answer

read -r -p "Enter your name : " name
echo "Hi, $name. Let us be friends!"

echo "$IFS"

IFS=',' read -r v1 v2 v3 v4 v5 v6
