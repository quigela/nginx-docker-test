## Nginx and Docker reverse proxy test
##### Most code from https://github.com/productive-dev/minimal-reverse-proxy-demo

### Run

```docker-compose -f compose-reverse-proxy build```  
```docker-compose -f compose-reverse-proxy -f compose-proxy-manager up```  

### Proxy Manager
* HTTP Port: 80
* HTTPS Port: 443
* Admin Port: 8880

### Reverse Proxy

#### Endpoints Created
* /             : Vue Frontend
* /ibm  : Retrieves previous close on IBM ticker from API
* /weather  : Retrieves temperature from API