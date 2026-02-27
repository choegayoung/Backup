## yaml 파일 작성

- api version 확인
```bash
kubectl explain pod
```
- service 확인
```bash
kubectl explain service
```

- Pod용 yaml
```yaml
apiVersion: v1
kind: Pod

metadata:
  name: [Pod이름]

spec:
  containers:
  - image: [docker 이미지]
    name: [container 이름]
---
apiVersion: v1
kind: Pod

metadata:
  name: [Pod이름]

spec:
  containers:
  - image: [docker 이미지]
    name: [container 이름]
```

- Deployment용 yaml
```bash
apiVersion: apps/v1
kind: Deployment

metadata:
  name: [Deployment 이름]

spec:
    replicas: [pod 수]
    selector:
        matchLabels:
        app: [pod 라벨명]
    template:
        metadata:
            labels:
                app: [pod 라벨명]
        spec:
            containers:
                - image: [docker 이미지]
                name: [container 이름]
                ports:
                - containerPort: [service port]
```

- yaml 만들기
```bash
kubectl create deployment app-dp --replicas=2 --image=nginx:1.28 --dry-run -o yaml > app-dp.yaml
```

- pod 정보 실시간 확인
```bash
kubectl get pods --watch
```

- 수정하기
```bash
kubectl edit deployment/app-dp
```

- Service
```yaml
apiVersion: v1
kind: Deployment

metadata:
    name: app-sv

spec:
    type: NodePort
    selector:
        app: app-label
    ports:
        - protocol: TCP
          port: 80
          targetPort: 80
          nodePort: 30000
```

