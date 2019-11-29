
import server
import unittest
import json
import requests
import getSummaries


example_news = "At least 18 people have been killed after a 6.4 magnitude earthquake hit Albania, the defence ministry says.\nThe quake brought down buildings and left people trapped under rubble. One man died after jumping from a window in panic after the tremor struck.\nThe quake hit 34km (21 miles) north-west of the capital, Tirana, in the early hours of Tuesday. \nHours later, a separate earthquake struck the city of Mostar in Bosnia. There were no reports of casualties.\nAlbanian Prime Minister Edi Rama said rescuers would \"continue to search patiently and thoroughly to the end\".\n\"We have victims. We are working to do everything possible in the affected areas,\" he wrote on Twitter. \nSoldiers, police and emergency workers have been searching through the debris of buildings, where people are still believed to be trapped. So far, some 42 survivors have been extracted from the ruins, according to officials.\nThe majority of fatalities occurred in the coastal city of Durres and in the town of Thumane, 40km to the north-west of Tirana and close to the epicentre, according to the defence ministry.\nIn neighbouring Kurbin, a man died after jumping from his building in panic, and another died in a car accident when the earthquake tore open parts of the road he was on, AFP reported the ministry as saying.\nMore than 600 people have been treated in hospital, Albanian state media reported.\nEmergency workers told Albanian media that one of the dead was an elderly woman who had managed to save her grandson by cradling him with her body.\nA man in Durres told local news channel News24 that his daughter and niece were among those trapped inside a collapsed apartment building.\n\"I talked with my daughter and niece on the phone. They said they are well and waiting for the rescue. Could not talk to my wife. There are other families, but I could not talk to them.\"\nTwo of those killed in Durres were brothers from Kosovo working in the city, Kosovo's minister of foreign affairs confirmed on social media. He said the country would have a day of mourning in their honour.\nRescuers in Durres were also seen trying to free a young boy trapped in the rubble.\nBesar Likmeta, a journalist based in Durres, told the BBC: \"I can see right now the firefighters using their bare hands and trying to cut through concrete and iron slabs of the collapsed building.\n\"There are Red Cross crews and police special intervention units and army. But there is no clear count of how many people might still be missing.\"\nAlbania was ill-equipped to deal with the situation, he said, and had appealed for outside help.\nThe European Commission said it had deployed rescue teams from Italy, Greece and Romania to help with the search efforts. \n\"We stand by Albania at this difficult time following the earthquakes. We have mobilised immediate support to help local authorities,\" the commission wrote on Twitter.\nRescue teams were also sent from Kosovo and Montenegro.\nThere have been a number of aftershocks, including one of 5.3 magnitude, the European-Mediterranean Seismological Centre said.\nThe Balkans is in an area prone to seismic activity. \nTuesday's earthquake has been described by authorities as the strongest to hit Albania in decades.\nIn 1979, a magnitude 6.9 quake hit Albania leaving 136 dead and more than 1,000 injured. \nHave you been affected by the earthquake? If it is safe to do so you can get in touch by emailing haveyoursay@bbc.co.uk.\nPlease include a contact number if you are willing to speak to a BBC journalist. You can also contact us in the following ways: \n"
example_title = "Deadly 6.4 magnitude earthquake hits Albania"

class TestServerScraping(unittest.TestCase):
    """
    User Story Number	002
    Summarize results from news source
    """

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_summarize_empty_source_should_return_empty_string(self):
        """
        TC01	Verify that an empty string is returned when an empty source is provided.
        """
        res = getSummaries.get_summary_from_article("", "", 5)
        self.assertEqual(res, '')


    def test_summary_should_be_equal_or_smaller(self):
        """
        TC02	Verify that the result is equals or smaller than the source 
        """
        res = getSummaries.get_summary_from_article(example_title, example_news, 5)
        self.assertGreaterEqual(len(example_news), len(res))



if __name__ == '__main__':
    unittest.main()
