FROM amazon/aws-lambda-python:3.12

# install chrome dependencies
RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm jq unzip

COPY chrome_installer.sh ./chrome_installer.sh
RUN ./chrome_installer.sh
RUN rm ./chrome-installer.sh

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY main.py ./

CMD [ "main.lambda_handler" ]
