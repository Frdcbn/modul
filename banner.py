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
def banner():
    print("-".center(56,"•"))
    print(f"""
{kuning1}╔╦╗╦ ╦╦ ╔╦╗╦╔═╗╦  ╔═╗  ╔═╗╔═╗╦═╗╦╔═╗╔╦╗
{hijau1}║║║║ ║║  ║ ║╠═╝║  ║╣   ╚═╗║  ╠╦╝║╠═╝ ║ 
{merah1}╩ ╩╚═╝╩═╝╩ ╩╩  ╩═╝╚═╝  ╚═╝╚═╝╩╚═╩╩   ╩ 
""")
    print("-".center(56,"•"))
    location_info = get_location_info()
    print("Informasi Lokasi:")
    print("Alamat IP:", location_info.ip)
    print("Negara:", location_info.country)
    print("Provinsi:", location_info.state)
    print("Kota:", location_info.city)
    print("Koordinat:", location_info.latlng)
