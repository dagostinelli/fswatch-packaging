#!/bin/bash

set -e
set -x

# Build SRPM
rpmdev-setuptree && \
rpmlint fswatch.spec && \
spectool -g -R fswatch.spec && \
rpmbuild -bs fswatch.spec

# Build Locally
# NOTE: development dependencies must be installed for this to work
rpmbuild -ba fswatch.spec

# RUN mock
rpmbuild -bs fswatch.spec && mock -r fedora-31-x86_64 --resultdir ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/SRPMS/fswatch-1.14.0-1.fc31.src.rpm
rpmbuild -bs fswatch.spec && mock -r epel-7-x86_64 --resultdir ~/rpmbuild/RPMS/x86_64 ~/rpmbuild/SRPMS/fswatch-1.14.0-1.fc31.src.rpm

# Do these manually

# RUN koji
# koji build --scratch rawhide `(ls ~/rpmbuild/SRPMS/fswatch* | sort -n | head -1)`
# koji list-tasks --mine

# RUN fedora-review
# cd ~/temp
# cp fswatch.spec ~/temp
# cp fswatch*.src.rpm ~/temp
# fedora-review -n fswatch
# less review-fswatch/review.txt
# REVIEW the report
