# Device Registry Service 
REST API Created in Python

All responses will have the form 

```json
{
	"data": "Mixed type holding the content of the response",
	"message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the 'data field' 

### List all devices 

**Defintion**

`Get  /devices`

**Response**

- `200 OK` on success

```json 
[
	{
		"identifier": "floor-lamp",
		"name": "Floor Lamp", 
		"device_type": "switch", 
		"controller_gateway": "192.168.0.2"
	},
	{
		"identifier": "tv",
		"name": "Living Room TV", 
		"device_type": "tv", 
		"controller_gateway": "192.168.0.9"
	}
]
```

### Registering a new device 

**Definition**

`Post /devices`

**Arguments**

- `"identifier": string` a unique identifier for this device
- `"name": string` a friendly name for this device 
- `"device_type": string` they type of the device as understood by the client 
- `"controller_gateway": string` the IP address of the device's controller

If a device with the given identifier already exists, the existing device will be overwritten 

**Response**

-`201 Created`

```json 
{
	"identifier": "floor-lamp",
	"name": "Floor Lamp", 
	"device_type": "switch", 
	"controller_gateway": "192.168.0.2"
}
```


