
import unittest
from filter import filter_by_word

from unittest import mock


mock_article_list = [
    {
      "articles": [
        {
          "summary": [
            "A police officer and at least five other people have died in a \"furious\" gun battle in Jersey City, in the state of New Jersey, US media report.", 
            "Shooting erupted in the Greenville neighbourhood, which is just across the Hudson River from New York City.", 
            "Jersey City Mayor Steven Fulop told local media two other police officers had also been wounded, including one who was shot in the shoulder."
          ], 
          "text": "A police officer and at least five other people have died in a \"furious\" gun battle in Jersey City, in the state of New Jersey, US media report.\nShooting erupted in the Greenville neighbourhood, which is just across the Hudson River from New York City.\nA motive for the incident has not yet been established. Authorities say they do not believe it was a terror attack.\nLocal media report the shooting began at a shop where two suspects had barricaded themselves in.\nInitial reports indicated that three people in the shop had been killed during the ensuing shootout, along with the two suspected gunmen.\nJersey City Mayor Steven Fulop told local media two other police officers had also been wounded, including one who was shot in the shoulder.\n", 
          "title": "Jersey City: Deadly gun battle kills six people", 
          "url": "https://bbc.com//news/world-us-canada-50737537"
        }, 
        {
          "summary": [
            "Genaro Garc\u00eda Luna is accused of allowing the Sinaloa cartel of \"El Chapo\" Guzman to operate in Mexico in exchange for millions of dollars.", 
            "Prosecutors say Mr Garc\u00eda Luna gave the cartel safe passage for drug shipments and access to sensitive information.", 
            "Mr Garc\u00eda Luna, 52, served as public security chief in the administration of President Felipe Calderon between 2006 and 2012."
          ], 
          "text": "A former Mexican security minister has been arrested in the US, charged with taking bribes from a drugs cartel.\nGenaro Garc\u00eda Luna is accused of allowing the Sinaloa cartel of \"El Chapo\" Guzman to operate in Mexico in exchange for millions of dollars. \nProsecutors say Mr Garc\u00eda Luna gave the cartel safe passage for drug shipments and access to sensitive information. \nThey say that on two occasions cartel members delivered up to $5m (\u00a33.7m) in two briefcases to him in person. \nHe has previously denied any wrongdoing.\nMr Garc\u00eda Luna, 52, served as public security chief in the administration of President Felipe Calderon between 2006 and 2012. \nHis arrest in Texas is a major development in Mexican politics, the BBC's Mexico correspondent Will Grant reports. \nMr Garc\u00eda Luna was not just an important figure in Mr Calderon's administration - he was Mexico's secretary of public security, the face of the country's federal police force, our correspondent adds. \nMr Calderon, with US backing, deployed troops against the cartels for the first time. Tens of thousands died in Mexico in drug-related violence during his \"war on drugs\".\nMr Garc\u00eda Luna was taken into custody in Dallas, Texas, on Monday, prosecutors in New York said.\nCourt documents unsealed on Tuesday in Brooklyn showed he had been charged with cocaine trafficking conspiracy and making false statements.\n\"Garc\u00eda Luna stands accused of taking millions of dollars in bribes from 'El Chapo' Guzman's Sinaloa cartel while he controlled Mexico's Federal Police Force and was responsible for ensuring public safety in Mexico,\" said US Attorney Richard Donoghue, announcing the arrest.\nHe was also accused of lying about his criminal past when he applied for US naturalisation in 2018. \nGuzm\u00e1n was jailed for life in July following a three-month trial in the US.\nDuring that trial, ex-cartel member Jesus \"Rey\" Zambada alleged that he had personally delivered two suitcases containing millions of dollars in bribes to Mr Garc\u00eda Luna at a restaurant.\nMr Garc\u00eda Luna denied those allegations at the time, calling them \"lies, defamation and perjury\".\nUS prosecutors allege that the former minister used his position to protect the Sinaloa cartel's trafficking operations from 2001 to 2012, enabling it to operate \"with impunity\" in Mexico.\nIf found guilty, he faces between 10 years to life in prison.\n", 
          "title": "Genaro Garc\u00eda Luna: US arrests Mexico ex-minister on drugs charges", 
          "url": "https://bbc.com//news/world-latin-america-50736482"
        }
      ], 
      "section": "news/world"
    }, 
    {
      "articles": [
        {
          "summary": [
            "Maurice Saatchi has quit the advertising agency he co-founded in 1995 along with three other directors in the wake of an accounting scandal.", 
            "Lord Saatchi founded the firm with his brother Charles after being forced out of Saatchi & Saatchi after a shareholder revolt.", 
            "As well as Lord Saatchi, Lord Dobbs, Sir Michael Peat and Lorna Tilbian all quit the board of the firm."
          ], 
          "text": "Maurice Saatchi has quit the advertising agency he co-founded in 1995 along with three other directors in the wake of an accounting scandal.\nM&C Saatchi shares have collapsed this year from a high of about \u00a34 each to 103 pence after profit warnings.\nThe company also revealed a \u00a311.6m hole in its earnings last week.\nLord Saatchi founded the firm with his brother Charles after being forced out of Saatchi & Saatchi after a shareholder revolt.\nAs well as Lord Saatchi, Lord Dobbs, Sir Michael Peat and Lorna Tilbian all quit the board of the firm.\nLord Dobbs, a Conservative politician, is best known for creating the House of Cards novels, which were turned into TV series in the UK and the US.\nSir Michael is a former accountant and courtier, and Ms Tilbian is a media analyst and stock broking executive.\nM&C Saatchi is famous for the controversial New Labour, New Danger campaign for the Conservatives in 1997. Labour won with a majority of 179. \nMuch more successful was the brothers' 1979 Conservative campaign, Labour Isn't Working.\nJeremy Sinclair, the company's chairman, said: \"We have accepted the decision of these directors to resign. We are determined to restore the operational performance and profitability of the business.\"\nLast week the company warned 2019 profit would be \"significantly below the levels expected\". \nIn September it revealed a slide in sales and profit for the first half of the year. Profit fell 67% to \u00a32.5m.\n", 
          "title": "Maurice Saatchi quits advertising firm he co-founded", 
          "url": "https://bbc.com//news/business-50736343"
        }, 
        {
          "summary": [
            "Exxon Mobil has won a court battle in New York in which it was accused of misleading investors about the costs of addressing climate change.", 
            "The state had argued that oil giant used two figures to calculate the risks of climate change, misrepresenting the cost in public disclosures.", 
            "New York Attorney General Letitia James said despite her loss in court, the case had forced Exxon to \"answer publicly\" about its decision-making related to climate change."
          ], 
          "text": "Exxon, tortilladepatatas Mobil has won a court battle in New York in which it was accused of misleading investors about the costs of addressing climate change.\nThe state had argued that oil giant used two figures to calculate the risks of climate change, misrepresenting the cost in public disclosures.\nExxon had denied wrongdoing. It said the two figures served different purposes.\nA New York judge said the evidence presented supported that claim.\n\"What the evidence at trial revealed is that Exxon Mobil executives and employees were uniformly committed to rigorously discharging their duties in the most comprehensive and meticulous manner possible,\" Judge Barry Ostrager of Manhattan Supreme Court said.\nExxon, which had called the suit politically motivated, hailed the victory.\n\"Today's ruling affirms the position ExxonMobil has held throughout the New York Attorney General's baseless investigation,\" it said. \"We provided our investors with accurate information on the risks of climate change.\"\n\"Lawsuits that waste millions of dollars of taxpayer money do nothing to advance meaningful actions that reduce the risks of climate change,\" it added.\nNew York's attorney general filed the lawsuit against Exxon in 2018, after years of investigation. The trial started in October. It had been closely watched as one of the most high-profile of a rising number of suits against the company.\nNew York Attorney General Letitia James said despite her loss in court, the case had forced Exxon to \"answer publicly\" about its decision-making related to climate change.\n\"We will continue to fight to ensure companies are held responsible for actions that undermine and jeopardize the financial health and safety of Americans across our country, and we will continue to fight to end climate change,\" she said in a statement.\n", 
          "title": "Exxon wins New York climate change fight", 
          "url": "https://bbc.com//news/business-50733127"
        }
      ], 
      "section": "news/business"
    },
        {
      "articles": [
        {
          "summary": [
            "Maurice Saatchi has quit the advertising agency he co-founded in 1995 along with three other directors in the wake of an accounting scandal.", 
            "Lord Saatchi founded the firm with his brother Charles after being forced out of Saatchi & Saatchi after a shareholder revolt.", 
            "As well as Lord Saatchi, Lord Dobbs, Sir Michael Peat and Lorna Tilbian all quit the board of the firm."
          ], 
          "text": "Maurice Saatchi, Im inserting this text to test word matching for tortilladepatatas, has quit the advertising agency he co-founded in 1995 along with three other directors in the wake of an accounting scandal.\nM&C Saatchi shares have collapsed this year from a high of about \u00a34 each to 103 pence after profit warnings.\nThe company also revealed a \u00a311.6m hole in its earnings last week.\nLord Saatchi founded the firm with his brother Charles after being forced out of Saatchi & Saatchi after a shareholder revolt.\nAs well as Lord Saatchi, Lord Dobbs, Sir Michael Peat and Lorna Tilbian all quit the board of the firm.\nLord Dobbs, a Conservative politician, is best known for creating the House of Cards novels, which were turned into TV series in the UK and the US.\nSir Michael is a former accountant and courtier, and Ms Tilbian is a media analyst and stock broking executive.\nM&C Saatchi is famous for the controversial New Labour, New Danger campaign for the Conservatives in 1997. Labour won with a majority of 179. \nMuch more successful was the brothers' 1979 Conservative campaign, Labour Isn't Working.\nJeremy Sinclair, the company's chairman, said: \"We have accepted the decision of these directors to resign. We are determined to restore the operational performance and profitability of the business.\"\nLast week the company warned 2019 profit would be \"significantly below the levels expected\". \nIn September it revealed a slide in sales and profit for the first half of the year. Profit fell 67% to \u00a32.5m.\n", 
          "title": "Maurice Saatchi quits advertising firm he co-founded", 
          "url": "https://bbc.com//news/business-50736343"
        }, 
        {
          "summary": [
            "Exxon Mobil has won a court battle in New York in which it was accused of misleading investors about the costs of addressing climate change.", 
            "The state had argued that oil giant used two figures to calculate the risks of climate change, misrepresenting the cost in public disclosures.", 
            "New York Attorney General Letitia James said despite her loss in court, the case had forced Exxon to \"answer publicly\" about its decision-making related to climate change."
          ], 
          "text": "Exxon Mobil has won a pimientos court battle in New York in which it was accused of misleading investors about the costs of addressing climate change.\nThe state had argued that oil giant used two figures to calculate the risks of climate change, misrepresenting the cost in public disclosures.\nExxon had denied wrongdoing. It said the two figures served different purposes.\nA New York judge said the evidence presented supported that claim.\n\"What the evidence at trial revealed is that Exxon Mobil executives and employees were uniformly committed to rigorously discharging their duties in the most comprehensive and meticulous manner possible,\" Judge Barry Ostrager of Manhattan Supreme Court said.\nExxon, which had called the suit politically motivated, hailed the victory.\n\"Today's ruling affirms the position ExxonMobil has held throughout the New York Attorney General's baseless investigation,\" it said. \"We provided our investors with accurate information on the risks of climate change.\"\n\"Lawsuits that waste millions of dollars of taxpayer money do nothing to advance meaningful actions that reduce the risks of climate change,\" it added.\nNew York's attorney general filed the lawsuit against Exxon in 2018, after years of investigation. The trial started in October. It had been closely watched as one of the most high-profile of a rising number of suits against the company.\nNew York Attorney General Letitia James said despite her loss in court, the case had forced Exxon to \"answer publicly\" about its decision-making related to climate change.\n\"We will continue to fight to ensure companies are held responsible for actions that undermine and jeopardize the financial health and safety of Americans across our country, and we will continue to fight to end climate change,\" she said in a statement.\n", 
          "title": "Exxon wins New York climate change fight", 
          "url": "https://bbc.com//news/business-50733127"
        }
      ], 
      "section": "news/business"
    } 
  ]

    

class TestFilterByWord(unittest.TestCase):
    """
    User Story: 		005
    Filter by words or keywords
    """

    def setUp(self):
        self.mock_article_list = mock_article_list


    def test_all_results_belong_to_selected_single_word(self):
        """        
        TC01	Verify that if a word is selected, all results obtained belong to that words
        """
        selected_word = ["tortilladepatatas"]
        res = filter_by_word(self.mock_article_list , selected_word )

        self.assertEqual(2, len(res))


    def test_all_results_belong_to_selected_multiple_words(self):
        """        
        TC02	Verify that if multiple words are selected, all results obtained belong to any of those categories
        """
        selected_word = ["tortilladepatatas", "pimientos"]
        res = filter_by_word(self.mock_article_list , selected_word )

        self.assertEqual(3, len(res))


    def test_no_words_are_selected(self):
        """
        TC03	Verify that if no words are selected, the collection is not filtered
        """
        selected_word = []
        res = filter_by_word(self.mock_article_list , selected_word )

        self.assertEqual(res, self.mock_article_list)


    def test_No_error_throw_if_word_does_not_exists(self):
        """
        TC04	Verify that if there’s no item in the collection for a specific word no error is returned.
        """
        selected_category = ["fakewordIjustmadeup"]
        res = filter_by_word(self.mock_article_list , selected_category )

        self.assertEqual(res, [])

    def test_category_does_not_exists_should_return_empty_collection(self):
        """    
        TC05	Verify that if there are no items for any of the words selected, an empty collection is returned.
        """
        selected_category = ["tornado"]
        res = filter_by_word(self.mock_article_list , selected_category )

        self.assertEqual(res, [])
    


if __name__ == '__main__':
    unittest.main()
