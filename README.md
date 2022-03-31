# Intro:
In this project, I use Discogs public API (https://www.discogs.com/developers/#) to access the database of artists, releases, and labels. They are JSON formatted. The goal of the project is to access/verify artists' releases and write them down in a CSV. 
## Methodology:
I use a GET endpoint called “ARTIST RELEASES“:
 
https://api.discogs.com/artists/{artist_id}/releases{?sort,sort_order}

(i.e.  https://api.discogs.com/artists/8394033/releases)

The return body is similar to below: 
```json
 {
  "pagination": {
    "per_page": 50,
    "items": 9,
    "page": 1,
    "urls": {},
    "pages": 1
  },
  "releases": [
    {
      "artist": "Nickelback",
      "id": 173765,
      "main_release": 3128432,
      "resource_url": "http://api.discogs.com/masters/173765",
      "role": "Main",
      "thumb": "https://api-img.discogs.com/lb0zp7--FLaRP0LmJ4W6DhfweNc=/fit-in/90x90/filters:strip_icc():format(jpeg):mode_rgb()/discogs-images/R-5557864-1396493975-7618.jpeg.jpg",
      "title": "Curb",
      "type": "master",
      "year": 1996
    },
```

Dataset: I have three data points to illustrate how the program works:

| artist_id | artist_name |
| --------------- | --------------- | 
| 8394033 | Baby Keem| 
| 2894422 | Denzel Curry | 
| 0 | ZeyB Nepton | 


Here I grabbed the first two artist ids directly from their website. The third one is a made-up artist that I included in the dataset to show how the program handles a status code other than 200.



The test runs for these three artists and outputs the logs which show the results of the tests. Then after it writes down the artist, release, year, and format to a CSV file. The program verifies the output by checking the status code and compares the returned artist name with the expected name. 

### Pros of my approach:
- I used pytest testing framework which detects my test and runs through each data point without a for-loop. Also used pytest.ini to output logs live in terminal and write them down to a logs file.

- I created a function under utilities folder which is reusable with any tests. It is for getting environment variables from the config file.

- Printing the artist-release information to a CSV so that it can be shared with others who are not necessarily familiar with reading a code output. 

### Cons of my approach:
- I used pytest parametrization right above my test since the dataset was small. This won’t be useful if i had a bigger dataset. So It would be better to create a csv of data and read from there.

- Both artists have a limited number of releases so one request was enough to get all their releases. When I tried a get request with Kendrick Lamar, I noticed that there are multiple pages and I needed to specify the page number in the request. So my approach does not get all releases for an artist who has a huge portfolio. 


## How to use it:

I tested my code in a Windows virtual environment (python version 3).

Please first install the requirements: 

```pip install -r requirements.txt```

Then run the test using:

```pytest test_ArtistReleases.py```

The result will show up in the command promp. You can also see the logs in pytest.log file. For the csv files it should be outputted as list_of_releases_{artist name}.csv

