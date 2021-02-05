## Nginx and Docker reverse proxy test
##### Most code from https://github.com/productive-dev/minimal-reverse-proxy-demo

### Run

```docker-compose build```  
```docker-compose up```

#### Endpoints Created
* /             : Vue Frontend
* /ibm-service  : IBM Service (Generates random value for IBM from min and max on 02/05/2021)
* /api-service  : Retrieves temperature from external weather API