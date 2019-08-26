출처: https://love2dev.com/blog/whats-the-difference-between-encodeuri-and-encodeuricomponent/

# encodeURI()

### Ex. 1 - input

> encodeURI("http://www.yourdomain.com/a file with spaces.html")

### Ex. 1 - output

> "http://www.yourdomain.com/a%20file%20with%20spaces.html"

# encodeURIComponent()

The encodeURIComponent function should be used to encode queryString parameters, in particular URLs. The difference between encodeURI and encodeURIComponent is encodeURIComponent encodes the entire string, where encodeURI ignores protocol prefix ('http://') and domain name. encodeURIComponent is designed to encode everything, where encodeURI ignores a URL's domain related roots.

### Ex. 1 - input

> encodeURIComponent("http://www.yourdomain.com/a file with spaces.html")

### Ex. 1 - output

> "http%3A%2F%2Fwww.yourdomain.com%2Fa%20file%20with%20spaces.html"
