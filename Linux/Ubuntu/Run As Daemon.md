# Run As Daemon

## Temporary Method

If you want to run some .sh(shell script) as daemon

Just add `&`....
```
$ some command &
```

## Right way to go
write some .service file at /lib/systemd/system.
then you can use
```
$ sudo systemctl status myservice
```

or

```
$ sudo service myservice status
```