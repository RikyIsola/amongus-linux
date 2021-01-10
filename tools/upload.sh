set -e
cd package
debuild -S
cd ..
dput ppa:isola/amongus amongus_*_source.changes
rm amongus_*