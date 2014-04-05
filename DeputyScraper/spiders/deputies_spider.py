from scrapy.selector import Selector
from scrapy.spider import Spider
import codecs

base_url    = "http://sitl.diputados.gob.mx/LXII_leg/"
deputy_list = "listado_diputados_gpnp.php?tipot=TOTAL" 
base_dir    = "Deputies/"
base_file   = "deputies"
filename    = base_dir+base_file
# TODO: find a way to retrieve the parties without hardcoding the party logos
parties_logos = ["pri01.png", "pan.png", "prd01.png", "logvrd.jpg", "logo_movimiento_ciudada", "logpt.jpg", "panal.gif"]

class DiputadosSpider(Spider):
    name = "deputies"
    allowed_domains = ["diputados.gob.mx"]
    start_urls = [base_url+deputy_list]

    def parse(self, responce):
        open(filename+".html", 'wb').write(responce.body)
        sel = Selector(responce)

        deputies_fields = sel.xpath('//td[@class="EncabezadoVerde"]/ancestor::table[1]//tr/td[@class="textoNegro"]/a')
        
        deputies_names  = deputies_fields.xpath('text()').extract()
        deputies_links  = deputies_fields.xpath('@href').extract()
        deputies_meta   = deputies_fields.xpath('ancestor::td[1]')
        deputies_state  = deputies_meta.xpath('following-sibling::*[1]/text()').extract()
        deputies_district = deputies_meta.xpath('following-sibling::*[2]/text()').extract()
# TODO: we really need a better way to retrieve the deputy's party  
        deputies_party  = deputies_meta.xpath('ancestor::tr[1]/preceding-sibling::*/td/img[@src!="images/h_line.gif"]/@src')

        print(len(deputies_party))

        file = codecs.open(filename+'_data', 'w', 'utf_8')
        for i in range(len(deputies_names)):
            file.write(' '.join(deputies_names[i].split()[1:])+'\t'+
                base_url+deputies_links[i]+'\t'+
                deputies_state[i]+'\t'+
                deputies_district[i]+'\n')
        file.close()
