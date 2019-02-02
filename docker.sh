#!/usr/bin/env sh

set -eux

. $(dirname $0)/config.sh

echo $VERSION

docker build \
      -t mybusybox:${VERSION} \
      --build-arg VERSION=${VERSION} \
      .