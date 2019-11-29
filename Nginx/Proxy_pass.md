# Proxy_pass

https://wani.kr/posts/2016/07/01/nginx-proxy-settings/

```
server {
    listen       80;
    server_name  wani.kr;
    location /other/ {
        rewrite ^/other(/.*)$ $1 break;
        proxy_pass http://other;
        proxy_set_header Host other.wani.kr; # 두 서버에서는 other.wani.kr 을 host로 인식.
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Proxy-From wani.kr; # 프록시가 여러대이고 어디서 왔는지 인식해야 한다면 추가.
        proxy_redirect off;
    }
}
upstream other {
    server 111.11.11.11:80;
    server 111.11.11.12:80;
}
```
