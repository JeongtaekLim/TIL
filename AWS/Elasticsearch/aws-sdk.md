# Introduction
AWS 문서 어딘가에서 발견한, `aws-sdk`를 사용한 `aws elasticsearch` 활용 예제를 실행해보기위해 아래 코드를 사용하였다.
아래 `**` 표시되어있는 두 줄만 해결해 주었더니 예제가 동작하였다.
```
var AWS = require('aws-sdk/dist/aws-sdk-react-native');
AWS.config.update({
    region: 'my_region',
    accessKeyId: 'my_access_key',
    secretAccessKey: 'my_secret_access_key'
});

var domain = 'part_of_my_app_endpoint.my_region.es.amazonaws.com'; // e.g. search-domain.region.es.amazonaws.com
var index = 'node-test';
var type = '_doc';
var id = '1';
var document = {
 "title": "Moneyball",
 "director": "Bennett Miller",
 "year": "2011"
}
export function indexDocument() {
    const region = AWS.config.region;
    var endpoint = new AWS.Endpoint(domain);
    var request = new AWS.HttpRequest(endpoint, region);
    request.method = 'PUT';
    request.path += index + '/' + type + '/' + id;
    request.body = JSON.stringify(document);
    request.headers['host'] = domain;
    request.headers['Content-Type'] = 'application/json';
    // Content-Length is only needed for DELETE requests that include a request
    // body, but including it for all requests doesn't seem to hurt anything.
    request.headers["Content-Length"] = request.body.length;
    // var credentials = new AWS.EnvironmentCredentials('AWS'); // ** This line should be removed
    var signer = new AWS.Signers.V4(request, 'es');
    signer.addAuthorization(AWS.config.credentials, new Date());
    var client = new AWS.HttpClient();
    client.handleRequest(request, { xhrAsync: true }, function(response) { // ** In this line, you should add { xhrAsync: true } options
        console.log(response.statusCode + ' ' + response.statusMessage);
        var responseBody = '';
        response.on('data', function (chunk) {
            responseBody += chunk;
        });
        response.on('end', function (chunk) {
            console.log('Response body: ' + responseBody);
        });
    }, function(error) {
        console.log('Error: ' + error);
    });
}
```
`aws-sdk`, `aws elasticsearch`, `aws elasticsearch 예제`