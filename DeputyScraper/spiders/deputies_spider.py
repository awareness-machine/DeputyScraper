from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from DeputyScraper.items import Deputy
import codecs

base_url    = "http://sitl.diputados.gob.mx/LXII_leg/"
deputy_list = "listado_diputados_gpnp.php?tipot=TOTAL" 
base_dir    = "Deputies/"
base_file   = "deputies"
filename    = base_dir+base_file
# TODO: find a way to retrieve the parties without hardcoding the party logos
parties_logos = {"pri01.png" : "pri",
                 "pan.png"   : "pan",
                 "prd01.png" : "prd",
                 "logvrd.jpg": "verde",
                 "logo_movimiento_ciudadano.png" : "movimiento ciudadano",
                 "logpt.jpg" : "pt",
                 "panal.gif":"panal" 
                 }

class DiputadosSpider(CrawlSpider):
    name = "deputies"
    allowed_domains = ["diputados.gob.mx"]
    start_urls = [base_url+deputy_list]

    # Extract links matching 'curricula.php' and parse them
    rules = ( Rule(SgmlLinkExtractor(allow=('curricula\.php', )),
                   callback='parse_item' ),
            )

    def parse_item(self, responce):

        sel = Selector(responce)
        deputy = Deputy()

        deputy['id'] = responce.url.split('=')[-1]
        deputy['url'] = responce.url
#        deputy['page'] = responce.body

        deputy_base = sel.xpath('//span[@class="Estilo67"]')
        deputy_text_base_0 = deputy_base.xpath('text()')
        deputy_text_base_1 = deputy_base.xpath('parent::td/\
                                                following-sibling::td/text()')
        deputy_img_base = deputy_base.xpath('parent::td/preceding-sibling::td\
                                            /img/@src')
        
        deputy['name'] = deputy_text_base_0[0].extract().strip()
        deputy_logo = deputy_img_base[1].extract().strip()
        deputy_photo = deputy_img_base[0].extract().strip()
        deputy['election'] = deputy_text_base_1[0].extract().strip()
        deputy['state'] = deputy_text_base_1[1].extract().strip()
        deputy['circunscription'] = deputy_text_base_1[2].extract().strip()
        deputy['header'] = deputy_text_base_1[3].extract().strip()
        deputy['seat'] = deputy_text_base_1[4].extract().strip()
        deputy['substitute'] = ''.join(deputy_text_base_0[6].extract()\
                                       .split(':')[-1]\
                                      ).strip()
        deputy['onomastic'] = deputy_base.xpath('parent::td/text()')[0]\
                                  .extract().strip()
        deputy['mail'] = deputy_base.xpath('parent::td/a/text()')[0]\
                             .extract().strip()
        deputy['party'] = parties_logos[deputy_logo.split('/')[-1]]
        return deputy
