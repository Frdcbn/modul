import subprocess
import geocoder
import platform

hijau1 = "\033[1;92m"  # Terang
kuning1 = "\033[1;93m"  # Terang
putih1 = "\033[1;97m"  # Terang
merah1 = "\033[1;91m"  # Terang
biru1 = "\033[1;94m"  # Terang

def get_system_info():
    system_info = {}
    system_info['OS'] = platform.system()
    system_info['OS Version'] = platform.release()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    return system_info

def get_memory_info():
    memory_info = {}
    try:
        output = subprocess.check_output(['free', '-h']).decode('utf-8')
        lines = output.splitlines()

        total_memory = lines[1].split()[1]
        used_memory = lines[1].split()[2]
        memory_info['Total Memory'] = total_memory
        memory_info['Used Memory'] = used_memory
    except subprocess.CalledProcessError:
        memory_info['Total Memory'] = 'N/A'
        memory_info['Used Memory'] = 'N/A'

    return memory_info

def get_uptime():
    try:
        output = subprocess.check_output(['uptime', '-p']).decode('utf-8').strip()
        return output
    except subprocess.CalledProcessError:
        return 'N/A'

def get_location_info():
    g = geocoder.ip('me')
    return g

def banner(name):
    print(putih1 + f' {name} '.center(56, "•"))
    print(f"""
{biru1}╔╦╗╦ ╦╦ ╔╦╗╦╔═╗╦  ╔═╗  ╔═╗╔═╗╦═╗╦╔═╗╔╦╗
{hijau1}║║║║ ║║  ║ ║╠═╝║  ║╣   ╚═╗║  ╠╦╝║╠═╝ ║ 
{merah1}╩ ╩╚═╝╩═╝╩ ╩╩  ╩═╝╚═╝  ╚═╝╚═╝╩╚═╩╩   ╩ 
""")
    print(putih1 + " Your information ".center(56, "•"))
    location_info = get_location_info()
    system_info = get_system_info()
    memory_info = get_memory_info()
    uptime = get_uptime()
    print(hijau1 + " " + putih1 + ":" + biru1, location_info.ip)
    print(hijau1 + " " + putih1 + ":" + biru1, location_info.country)
    print(hijau1 + " " + putih1 + ":" + biru1, location_info.state)
    print(hijau1 + " " + putih1 + ":" + biru1, location_info.city)
    print(hijau1 + " " + putih1 + ":" + biru1, location_info.latlng)
    print(hijau1 + " " + putih1 + ":" + biru1, system_info['OS'], system_info['OS Version'])
    print(hijau1 + " " + putih1 + ":" + biru1, system_info['Machine'])
    print(hijau1 + " " + putih1 + ":" + biru1, platform.uname().release)
    print(hijau1 + " " + putih1 + ":" + biru1, uptime)
    print(hijau1 + " " + putih1 + ":" + biru1, memory_info['Used Memory'], "/", memory_info['Total Memory'])
    print(putih1 + "".center(56, "•"))

#banner("System Information")

