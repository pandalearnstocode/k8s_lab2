services = ['applicationlayer', 'clientlayer', 'datalayer', 'ingress', 'mllayer','utilitylater','optimizationlayer']
yaml_files = ["k8s_v2/%s.yml" % service for service in services]

k8s_yaml(yaml_files)
docker_build('applicationlayer', 'services/applicationlayer', dockerfile='services/applicationlayer/Dockerfile')
docker_build('clientlayer', 'services/clientlayer', dockerfile='services/clientlayer/Dockerfile')
docker_build('datalayer', 'services/datalayer', dockerfile='services/datalayer/Dockerfile')
docker_build('mllayer', 'services/mllayer', dockerfile='services/mllayer/Dockerfile')
docker_build('optimizationlayer', 'services/optimizationlayer', dockerfile='services/optimizationlayer/Dockerfile')
docker_build('utilitylayer', 'services/utilitylayer', dockerfile='services/utilitylayer/Dockerfile')