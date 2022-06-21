sudo apt-get install liblzma-dev
sudo apt-get install lzma
sudo apt-get install libbz2-dev

wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz

tar -xvzf geckodriver*

chmod +x geckodriver

#sudo mv geckodriver /usr/local/bin/

wget https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip

unzip chromedriver*

chmod +x chromedriver

#sudo mv chromedriver /usr/local/bin/

#rm chromedriver* geckodriver*
