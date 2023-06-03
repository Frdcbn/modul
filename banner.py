import subprocess
hijau1 = "\033[1;92m"#Terang
kuning1 = "\033[1;93m"#Terang
putih1 = "\033[1;97m"#Terang
merah1 = "\033[1;91m"#Terang
biru1 = "\033[1;94m"#Terang
import geocoder

def get_location_info():
    g = geocoder.ip('me')
    return g
def banner(name):
    print(f"{putih1} {name} ".center(56,"•"))
    print(f"""
{biru1}╔╦╗╦ ╦╦ ╔╦╗╦╔═╗╦  ╔═╗  ╔═╗╔═╗╦═╗╦╔═╗╔╦╗
{hijau1}║║║║ ║║  ║ ║╠═╝║  ║╣   ╚═╗║  ╠╦╝║╠═╝ ║ 
{merah1}╩ ╩╚═╝╩═╝╩ ╩╩  ╩═╝╚═╝  ╚═╝╚═╝╩╚═╩╩   ╩ 
""")
    print(putih1+" Your information ".center(56,"•"))
    location_info = get_location_info()
    print(hijau1+"Alamat IP "+putih1+": "+biru1, location_info.ip)
    print(hijau1+"Negara "+putih1+": "+biru1, location_info.country)
    print(hijau1+"Provinsi "+putih1+": "+biru1, location_info.state)
    print(hijau1+"Kota "+putih1+": "+biru1, location_info.city)
    print(hijau1+"Koordinat "+putih1+": "+biru1, location_info.latlng)
    
