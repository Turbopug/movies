## Overview
The Movie Trailer Website is part of the [Udacity](http://udacity.com) Nanodegree Full Stack Web Developer program. It is website that allows users to see your favorite movies and watch the trailers.

## Table of contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Instructions](#instructions)


## Requirements

Python is required to be installed on the system that will run the project. The project was created using Python version 2.7.10; however, it should also work on later versions.
- [Download Python](https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi)

The following files are included in the project package and are required for it to run correctly.

```
movie_project/
├── docs/
│   ├── movies.xml
├── entertainment_center.py
├── fresh_tomatoes.py
├── media.py
└── README.md
```

## Installation
######NOTE: The installation instructions are for a Windows based system.
You can install and run the project in two ways.

####Using a command prompt:
- Open a command prompt.  
- In the command prompt navigate to the directory that has the files mentioned in the requirements.  
- Run the following command:
```
> python entertainment_center.py
```
- A new browser window should open up that displays the movie website.

####Using IDLE:
- In the directory that has the project files right click on the entertainment_center.py file and select "Edit with IDLE"
- In the IDLE window that opened up select "Run-->Run Module" from the menu bar
- A new browser window should open up that displays the movie website.

After using either method, some new files will be created and added to the project directory.  Your directory should look like this:
```
movie_project/
├── docs/
│   ├── movies.xml
├── entertainment_center.py
├── fresh_tomatoes.html
├── fresh_tomatoes.py
├── fresh_tomatoes.pyc
├── media.py
├── media.pyc
└── README.md
```
The .pyc files are created by Python and contain byte code.  The fresh_tomatoes.html file is an html file that when opened in a browser contains the front end to the project.

## Instructions

####Getting Started
After obtaining the files and following the [installation](#installation) instructions you are ready to play with the Fresh Tomatoes Movie Trailers website.  Open fresh_tomatoes.html file with a browser (note: it might already be opened if you followed the [installation](#installation) instructions).  You will see a number of movie posters along with the name of the movie.  If you hover over the name of the movie you will see the following extended information:
- Starring - The starring cast of the movie.
- Summary - A synopsis of the movie.
- Released - The date the movie was released (USA release dates)

If you click on a movie poster a popup will open that plays the movie's trailer.

####Updating the Movie List
If you open up the docs\movies.xml file with any text editor you will see entries like this:
```
<movie>
  <title>Big Trouble in Little China</title>
  <summary>Jack Burton, a tough-talking, wisecracking truck driver whose hum-drum life on the road takes a sudden supernatural tailspin when
    his best friend's fiancee is kidnapped</summary>
  <poster>https://upload.wikimedia.org/wikipedia/en/7/76/Big_Trouble_in_Little_China_Film_Poster.jpg</poster>
  <trailer>https://www.youtube.com/watch?v=592EiTD2Hgo</trailer>
  <cast>Kurt Russell, Kim Cattrall, Dennis Dun</cast>
  <released>July 2, 1986</released>
</movie>
```
All movie data is stored in this xml file.  You can update, add and remove movies by simply cutting and pasting new movie sections into the xml file and adjusting the values.  There is no need to edit the python (.py) files.  If you again follow the instructions in the  [installation](#installation) section a new fresh_tomatoes.html file will be generated with the changes from the movie.xml file.
