# IPython log file

get_ipython().magic('logstart')
import cadvisor
cad = cadvisor.Cadvisor('127.0.0.1:8080', '1.3')
cad.API
cad.api_url
cad.base_url
cad.get_all_docker_containers_info
containers = cad.get_all_docker_containers_info()
containers = cad.get_containers_info()
cad
cad.base_url
cad.get_all_docker_containers_info()
cad.get_machine_info()
cadvisor.api.machine_info_url
cadvisor.api.machine_info_url(cad.api_url)
cadvisor.api.machine_info_url(cad.api_url)
cad.api_url
from urllib.parse import urljoin
urljoin(cad.api_url, 'machine')
urljoin(cad.api_url, '/machine')
urljoin(cad.api_url, 'machine/')
urljoin(cad.api_url, 'machine/')
cad.api_url
cad.api_url
cad.api_url = 'http://' + cad.api_url
cad.api_url
urljoin(cad.api_url, 'machine/')
