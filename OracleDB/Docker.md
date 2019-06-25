# Oracle with Docker

```
docker pull christophesurmont/oracle-xe-11g
docker run --name oracle11c -d -p 8080:8080 -p 1521:1521 -v /Users/jtlim/OracleDB:/u01/app/oracle/data christophesurmont/oracle-xe-11g
docker logs -f oracle11c
```
