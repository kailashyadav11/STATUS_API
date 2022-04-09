rm -rf ./dist/
yum install rpm-build -y
REL="1_1"
./setup.py bdist_rpm --release="$REL"
