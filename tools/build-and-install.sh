set -e
sudo apt remove amongus -y || echo ''
cd package
debuild -b -uc -us
cd ..
sudo dpkg -i amongus_*_amd64.deb
rm amongus_*