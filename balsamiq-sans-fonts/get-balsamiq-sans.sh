#!/bin/bash
# Get upstream zip and make source tar.xz

ARCHIVE="balsamiq-sans-fonts-1.010"
TMPDIR=$(mktemp -d --tmpdir=/var/tmp get_balsamiq_sans-XXXXXXXXXX)
[ $? != 0 ] && exit 1
umask 022
pushd "$TMPDIR"

wget -N -O $ARCHIVE.zip https://fonts.google.com/download?family=Balsamiq%20Sans
unzip $ARCHIVE.zip -d $ARCHIVE
tar -cvJf "$ARCHIVE.tar.xz" $ARCHIVE

popd
mv "$TMPDIR/$ARCHIVE.tar.xz" .
rm -fr "$TMPDIR"
