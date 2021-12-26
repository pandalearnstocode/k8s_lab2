```
minikube start
minikube addons enable registry
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
```

```
docker build -t localhost:5000/utilitylayer ./services/utilitylayer
docker build -t localhost:5000/mllayer ./services/mllayer
docker build -t localhost:5000/datalayer ./services/datalayer
docker build -t localhost:5000/optimizationlayer ./services/optimizationlayer
docker build -t localhost:5000/applicationlayer ./services/applicationlayer
docker build -t localhost:5000/clientlayer ./services/clientlayer
```

```
docker push localhost:5000/utilitylayer
docker push localhost:5000/datalayer
docker push localhost:5000/mllayer
docker push localhost:5000/optimizationlayer
docker push localhost:5000/applicationlayer
docker push localhost:5000/clientlayer
```


```
minikube addons enable ingress
<!-- kubectl apply -f ./k8s/minikube-ingress.yml -->
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
