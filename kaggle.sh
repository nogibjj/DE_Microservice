# sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install openjdk-11-jdk
sudo apt install zip unzip

pip install -r requirements.txt

mkdir ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

PROJECT=popular-tiktok-videos-authors-and-musics

rm -rf $PROJECT
mkdir $PROJECT
cd $PROJECT

kaggle datasets download -d thedevastator/popular-tiktok-videos-authors-and-musics
# kaggle competitions download -c $PROJECT
unzip $PROJECT