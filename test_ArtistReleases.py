from utilities.BaseClass import BaseClass
import requests
import pandas as pd
import pytest
import logging

# In this project, I use Discogs public API (https://www.discogs.com/developers/#)
# to access the database of artists, releases, and labels. They are JSON formatted.
# The goal of the project is to access/verify artists' releases and write them down in a CSV.

@pytest.mark.parametrize("artist_id, artist_name, expected",
                         [(8394033, "Baby Keem", 200),
                          (2894422, "Denzel Curry", 200),
                          (0, "ZeyB Nepton", 200)])
class TestArtistReleases(BaseClass):
    def test_ArtistReleases(self, artist_id, artist_name, expected):
        env = self.getProperties()
        try:
            url = env.get("discog_api").data + env.get("get_artist_release").data.format(artist_id)
            resp = requests.get(url)
            logging.info("The API end-point has successfully ran for the payload:\t" + url
                     + "\nStatus Code:\t" + str(resp.status_code)
                     + "\nResponse Time\t" + str(resp.elapsed.total_seconds())
                     + "\nResponse:\t" + str(resp.json()))
            assert resp.status_code == expected
            json_res = resp.json()
            list_of_releases = []
            for i in json_res["releases"]:
                if 'format' in i:
                    list_of_releases.append([artist_name, i["title"], i["year"], i["format"]])
                else:
                    list_of_releases.append([artist_name, i["title"], i["year"], None])
            df = pd.DataFrame(list_of_releases, columns=['artist', 'title', 'year', 'format']).sort_values('year')
            df.to_csv('list_of_releases_{}.csv'.format(artist_name))
        except AssertionError as e:
            logging.error("The API end-point was unsuccessful for:\t" + artist_name
                     + "\nStatus Code:\t" + str(resp.status_code)
                     + "\nResponse:\t" + str(e))
            raise AssertionError
