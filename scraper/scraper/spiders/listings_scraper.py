import scrapy
import pandas as pd

class ListingsScraperSpider(scrapy.Spider):
    name = 'listings_scraper'
    allowed_domains = ['airbnb.com']
    start_urls = [
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=0&section_offset=3'
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=20&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=40&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=60&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=80&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=100&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=120&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=140&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=160&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=180&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=200&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=220&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=240&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=260&section_offset=3',
        'https://www.airbnb.com/s/Nairobi--Kenya/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&source=structured_search_input_header&search_type=pagination&ne_lat=-1.1646501329511787&ne_lng=36.899974141070004&sw_lat=-1.3489700191901892&sw_lng=36.762645039507504&zoom=12&search_by_map=true&place_id=ChIJp0lN2HIRLxgRTJKXslQCz_c&federated_search_session_id=dcf5b147-38bd-45e4-b244-d76dd58055df&items_offset=280&section_offset=3'
        ]

    def parse(self, response):
        # parse response
        # sites = response.css('div._gig1e7')
        # sites = response.css('div._e296pg')
        # create list to store data
        listings_list = []
        for x in response.css('div._gig1e7'):
            yield {
                'title': x.css('div._167qordg::text').get(),
                'url': x.css('a._sqvp1j').get(),
                'info': x.css('div._1jpkfwko::text').get(),
                'description': x.css('div._bzh5lkq::text').get(),
                'details': x.css('div._kqh46o::text').getall(),
                'is_superhost': x.css('div._ufoy4t::text').get(),
                'price': x.css('span._1p7iugi::text').getall(),
                'total_reviews': x.css('span._a7a5sx::text').getall(),
                'review_score': x.css('span._10fy1f8::text').getall()  
            }
            # title = x.css('div._167qordg::text').get()
            # is_superhost = x.css('div._ufoy4t::text').get()
            # # description = x.css('div._1jpkfwko::text').get()
            # description = x.css('div._bzh5lkq::text').get()
            # details = x.css('div._kqh46o::text').getall()
            # # amenities=x.css('span._krjbj::text').getall()
            # price = x.css('span._1p7iugi::text').getall()
            # total_reviews = x.css('span._a7a5sx::text').getall()
            # review_score = x.css('span._10fy1f8::text').getall()
        #     dict_list = {'title':title,
        #                  'description': description,
        #                  'details': details,
        #                  'price': price,
        #                  'is_superhost': is_superhost,
        #                  'total_reviews': total_reviews,
        #                  'review_score': review_score
        #                  }
        #     listings_list.append(dict_list)
        
        # # convert list to dataframe
        # df = pd.DataFrame(listings_list)
        # df.to_csv("../../../data/listings_data.csv",index=False)
        # return df.head()