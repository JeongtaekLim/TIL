# external-css

## Problem 

Basic Nginx index.html not styled with theme.css in same directory.

* Nginx config
```
server {
    listen 80;

    root /usr/share/nginx/html;
    index index.html index.htm;

    # Make site accessible from http://localhost/
    server_name www.mysite.co.kr mysite.co.kr;

    location / {

        root /usr/share/nginx/html;
        index index.html;
        include /etc/nginx/mime.types;
        # First attempt to serve request as file, then
        # as directory, then fall back to displaying a 404.
        try_files $uri $uri/ =404;

        # Uncomment to enable naxsi on this location
        # include /etc/nginx/naxsi.rules
        location ~ \.(js|jpg|png|css/)$ {
                expires 30d;
        }
    }
    ...
```
* HTML

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>hello!</title>
<style>
<link rel="stylesheet" type="text/css" href="theme.css">
</style>
</head>
<body>
<div class="warning-content">
...
```

## solution

Code below was wrong.
```html
<style>
<link rel="stylesheet" type="text/css" href="theme.css">
</style>
```
Code should be removed `style` tag
```html
<link rel="stylesheet" type="text/css" href="theme.css">
```