# NobetciNoterApi




1- Google Chrome Yükle
2- ChromeDriver Yükle
3- İzinleri ver

1-)
sudo dpkg -i google-chrome-stable_current_amd64.deb
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo gdebi google-chrome-stable_current_amd64.deb

2-)
wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

3-)
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
