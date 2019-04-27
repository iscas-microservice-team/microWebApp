# Source Image
FROM python:3.7
# Author
MAINTAINER Leon "leontian1024@gmail.com"
# Set working director
WORKDIR /var/app/microWebApp
# Add source code from os into container
Add . /var/app/microWebApp
# Import packages
RUN pip install Flask
RUN pip install Flask-wtf
RUN pip install requests
RUN pip install flask-bootstrap
# Expose port
EXPOSE 80
# Run command
ENTRYPOINT ["python","./spiritConn.py"]

