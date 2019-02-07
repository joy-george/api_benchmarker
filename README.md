
# API Benchmarker

This application illustrates a method of how an API's performance can be benchmarked

## Approach
The approach used here is to use decoupled modules that can give performance metrics like application wall clock time and request processing time to any API that applies it.

Now `/uptime` primarily fetches current data and time of the host. Since we have applied the decorator `add_response_time` and `execution_time.calculate` it will return the additional information.

### Time Calculations
###### Application Execution Time (`executionTimeMs`)

The application execution time is the time spent in processing the information which is requested, in our example the current data and time. It is basically the time difference from the start till the end of processing.

```
start_time = current_timestamp
application logic
processing_time = current_timestamp - start_time
```


###### Request Processing Time (`executionTimeMs`)
Request processing time is the time spent in doing all the processes as soon as the app server gets the request and till it receives the response back which will be sent out.

In this application, it is calculated by the time spent in performing all the operations between the `before_request` and `after_request` hooks.

## API
### /uptime
##### Request Path:
```
/api/timer/uptime
```
##### Sample Response Body:
```
{
     "currentDateTime": "2019-02-02 19:30:09 IST",
     "executionTimeMs": "0.2849",
     "responseTimeMs": "3.2330"
 }
```
### Swagger-ui
```
/api/ui
```

## Installation
The application requires `Python3+`  and `pip3`.

##### Create virtual env:
```
python3 -m venv dev_env
```

##### Activate virtual env:
```
source dev_env/bin/activate
```

##### Install Requirements:
```
pip3 install -r requirements.txt
```

##### Runing the application:
```
python3 app.py --env development
```

Valid values for `env`  are:
- development (default)
- production