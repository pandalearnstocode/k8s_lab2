minikube start
minikube addons enable registry
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
<!-- docker tag my/image localhost:5000/myimage
docker push localhost:5000/myimage -->


docker build -t localhost:5000/utility-layer ./services/utility_layer
docker push localhost:5000/utility-layer
docker build -t localhost:5000/data-layer ./services/data_layer
docker push localhost:5000/data-layer
docker build -t localhost:5000/ml-layer ./services/ml_layer
docker push localhost:5000/ml-layer
docker build -t localhost:5000/optimization-layer ./services/optimization_layer
docker push localhost:5000/optimization-layer
docker build -t localhost:5000/application-layer ./services/application_layer
docker push localhost:5000/application-layer

kubectl create -f ./k8s/utility_layer_d.yml.yml
kubectl create -f ./k8s/utility_layer_s.yml
