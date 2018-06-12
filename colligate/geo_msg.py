from  geopy.geocoders import Nominatim
import re

def getAddressByGeo(lat_lng):
    geoLocator = Nominatim()
    try:
        location = geoLocator.reverse(lat_lng)
        addr =  location.address
        cityname = re.split("[/,]", addr)[-5].strip()
        return cityname
    except:
        return -1


def mReverse(str):
    return str.split(',')[1] + ',' + str.split(',')[0]


if __name__ == "__main__":
    #测试样例，获得经纬度的地理位置
    lat_lng_list = ["121.381709,31.112813","113.722139,23.040632","116.305296,40.040583","118.787441,32.034322","115.977432,28.631981","121.594200,38.904808","117.180616,39.120697","113.310766,23.028445","104.084384,30.657373","120.216386,31.550284","102.791953,24.966535","120.194741,30.263122","114.425495,30.417963","117.021555,36.663924","114.042971,22.541148","114.496580,38.039410","120.623284,31.303073","108.947212,34.219960","113.668193,34.783516","106.503465,29.617800","120.377005,36.081504"]
    for elem in lat_lng_list:
        lat_lng = mReverse(elem)
        print(getAddressByGeo(lat_lng))