#!/bin/bash
set -e  # exit on error
. env/bin/activate
nikola build
nikola github_deploy
