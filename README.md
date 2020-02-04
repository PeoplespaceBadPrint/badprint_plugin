# OctoPrint-Badprint

## Setup

### Modify config.yaml
If not specified via the command line, the main configuration file config.yaml for OctoPrint is expected in its settings folder, which unless defined differently via the command line is located at ```~/.octoprint``` on Linux, at ```%APPDATA%/OctoPrint``` on Windows and at ```~/Library/Application Support/```OctoPrint on MacOS. If the file is not there, you can just create it - it will only get created by OctoPrint once you save settings that deviate from the default settings.

insert this
```plugins:```
```  helloworld:```
```    url: http://0.0.0.0:8080```
into config.yaml