# Install via NVM
NVM repos: https://github.com/creationix/nvm

### Download nvm install script
```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
```
or 
```
wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash
```

### Run some command
```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

### Check nvm install compelete
```
command -v nvm
// 'nvm' should be output
```
