#! /usr/bin/env bash
#
# Build Debian package in a Docker container
#

set -e

# Get build platform as 1st argument, and collect project metadata
image="${1:?usage: $(basename $0) ‹distro:release› [python‹N.N›]}"; shift
snake="${1:-python3.6}"; test -z "$1" || shift
dist_id="${image%%:*}"
codename="${image#*:}"
tag="${snake//./}-$dist_id-$codename"

declare -A zip_links
zip_links["python3.6"]="https://github.com/deadsnakes/python3.6/archive/ubuntu/xenial.zip"
zip_links["python3.7"]="https://github.com/deadsnakes/python3.7/archive/ubuntu/xenial.zip"
zip_links["python3.8"]="https://github.com/deadsnakes/python3.8/archive/ubuntu/bionic.zip"

sed -e "s/##ID##/${tag}/g" <Dockerfile.build >Dockerfile.$tag

declare -a build_opts=(
    -f "Dockerfile.$tag"
    --tag "$tag"
    --build-arg "DIST_ID=$dist_id"
    --build-arg "CODENAME=$codename"
    --build-arg "SNAKE=$snake"
    --build-arg "ZIPLINK=${zip_links[$snake]}"
)

# Build in Docker container, save results, and show package info
rm -f dist/*${snake}*${codename}*.*
docker build "${build_opts[@]}" "$@" .
mkdir -p dist
docker run $tag cat /python.tar | tar -C dist -x
ls -lh dist/*${snake}*${codename}*.*
