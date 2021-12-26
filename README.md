```
minikube start
minikube addons enable registry
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
```

```
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
docker build -t localhost:5000/client-layer ./services/client_layer
docker push localhost:5000/client-layer
```


```
kubectl apply -f ./k8s/minikube-ingress.yml
# kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
kubectl apply -f ./k8s
kubectl delete -f ./k8s
```


```
minikube stop
minikube delete --all
```


#### Reference:
* https://testdriven.io/blog/running-flask-on-kubernetes/
* https://minikube.sigs.k8s.io/docs/handbook/registry/
* https://github.com/4OH4/kubernetes-fastapi/
