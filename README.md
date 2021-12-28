```
minikube start
minikube addons enable registry
docker run --rm -it --network=host alpine ash -c "apk add socat && socat TCP-LISTEN:5000,reuseaddr,fork TCP:$(minikube ip):5000"
```

```
minikube dashboard
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
minikube start
minikube addons enable ingress
tilt up
```

```
kubectl exec postgres-5dd464f98c-4nzcc --stdin --tty -- createdb -U sample books
kubectl exec postgres-5dd464f98c-4nzcc --stdin --tty -- psql -U sample
```

```
minikube stop
minikube delete --all
```


#### Reference:
* https://testdriven.io/blog/running-flask-on-kubernetes/
* https://minikube.sigs.k8s.io/docs/handbook/registry/
* https://github.com/4OH4/kubernetes-fastapi/
* https://fastapi.tiangolo.com/advanced/sub-applications/
* http://richard.to/programming/fast-api-postgres-redis-kubernetes.html
* https://github.com/richard-to/kubernetes-experiments
* https://pypi.org/project/fastapi-redis-cache/
* https://github.com/Kludex/fastapi-microservices/
* https://www.kisphp.com/postgres/run-postgres11-and-pgadmin4-in-kubernetes-for-testing
* https://medium.com/swlh/fastapi-microservice-patterns-application-monitoring-49fcb7341d9a
* https://github.com/fkromer/fastapi-microservice-patterns/blob/main/application-metrics/service-a/app/main.py


# Pending:

* Jobs
* Celery
* Rabbit MQ
* Grafana : Done
* Prometheus : Done
* Follower
* Redis Dashboard
* DB
* DB monitor
* Load test


I have changed deployment and service of postgres from postgres to postgres-deployment and postgres-service respectively.

### Add this in wiki


```
The first (and only required) parameter inside create_engine() is the database url. Typically it takes the form dialect+driver://username:password@host:port/database. In our case, dialect is sqlite hence the sqlite:// bit. The additional /todooo.db bit specifies the location of the database. Of course, our sqlite database hasn’t been created yet, but this is where it will be. Note that this path is relative to the working directory.

In a production setting, the call to create_engine() might look more like engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/mydatabase') or engine = create_engine('mysql://scott:tiger@localhost/foo')
```

ref:
* https://docs.sqlalchemy.org/en/14/core/engines.html#database-urls
* https://www.gormanalysis.com/blog/building-a-simple-crud-application-with-fastapi/#sqlalchemy-engine


