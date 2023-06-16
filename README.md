# Nouncy
## Introduction
<img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/banner.png" >
This is a DRF web application for managing anouncements.

There are three main roles: 1-client 2-publisher 3-content manager

We use RESTful APIs for this application. For seeing all APIs run the app and go to this url:
"{ your host or local host }/api/v1/swagger-ui"

## Tools
<div style ="display: flex;">
  <img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/python-icon.png" >
  <img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/django-icon.png" >
  <img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/rest-api-icon.png" >
  <img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/jwt-icon.png" >
  <img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/docker-icon.png" >
  <img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/swagger-icon.png" >
  <img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/postman-icon.png" >
  <img src="https://github.com/AdelNoroozi/Nouncy/blob/master/resources/js-icon.png" >
</div>

## Descriptions
### Clients
##### Authentication
- register
- login
- get their user information
##### Announcement Management
- create announcements (needs publisher's confirmation)
- update their announcements (needs publisher's confirmation)
- delete their announcements
- get a list of their announcements
- retrieve their announcements
- search their announcements:
  - by title
  - by content
- order their announcements:
  - by title (alphabetically)
  - by creation date
  - by modification date
- filter their announcements:
  - by status
  - by creation date period
  - by modification date period
### Content Managers
##### Authentication
- login
- get their user information
##### Announcement Management
- get a list of the announcements that are assignd to them
- retrieving announcements that are assigned to them
- review an announcement
- search & order announcements assigned to them by the same fields as clients
- filter announcements assigned to them by the same fields as clients and also by creator
### Publishers
##### Authentication
- login
- get their user information
##### Announcement Management
- create announcements
- update their announcements
- delete their announcements
- get a list of all announcements
- retrieve all announcements
- search & order all announcements by the same fields as clients and content managers
- filter all announcements by the same fields as clients, content managers and also by:
  - creator role
  - assigned reviewer
- publish announcements
- reject announcements
- assign announcemens to a content manager
- review anouncements
### Superusers
##### Authentication
- login
- get their user information
- add new publishers
- add new content managers
##### Announcement Management
- every single action that other roles can perform