![README Cover Image](readme_cover.png)

Conekta Python v 2.4.0
======================

Wrapper for api.conekta.io

Install

```sh
pip install conekta
```

```sh
easy_install conekta
```

Charge via card

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'
conekta.locale = 'es'

try:
  order = conekta.Order.create({
      "line_items": [
          {
              "name": "Box of Cohiba S1s",
              "description": "Imported From Mex.",
              "unit_price": 20000,
              "quantity": 1,
              "sku": "cohb_s1",
              "category": "food",
              "type" : "physical",
              "tags" : ["food", "mexican food"]
          }
      ],
      "shipping_lines":[
        {
          "amount": 0,
          "tracking_number": "TRACK123",
          "carrier": "USPS",
          "method": "Train",
          "metadata": {
             "random_key": "random_value"
          }
        }],
      "customer_info":{
          "name": "John Constantine",
          "phone": "+525533445566",
          "email": "john@meh.com",
          "corporate": False,
          "vertical_info": {}
        },
      "shipping_contact":{
          "phone" : "5544332211",
          "receiver": "Marvin Fuller",
          "between_streets": "Ackerman Crescent",
          "address": {
              "street1": "250 Alexis St",
              "state": "Alberta",
              "country": "MX",
              "postal_code": "23455",
              "metadata":{ "soft_validations": True}
          }
      },
      "fiscal_entity":{
        "tax_id": "AMGH851205MN1",
        "name": "Nike SA de CV",
        "address": {
            "street1": "250 Alexis St",
            "internal_number": "19",
            "external_number": "91",
            "city": "Red Deer",
            "state": "Alberta",
            "country": "CA",
            "postal_code": "33242"
        }
      },
      "charges": [{
        "payment_method":{
          "type": "card",
          "token_id": "tok_test_visa_4242"
        },
        "amount": 20000
      }],
      "currency" : "mxn",
      "metadata" : {"test" : "extra info"}
    })

except conekta.ConektaError as e:
  print e.message
  #El pago no pudo ser procesado

#You can also get the attributes from the conekta response class:
print order.id

#Or in the event of an error, you can expect a ConektaError to be raised
```

Order via oxxo

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'

var data = {
      "line_items": [
          {
              "name": "Box of Cohiba S1s",
              "description": "Imported From Mex.",
              "unit_price": 20000,
              "quantity": 1,
              "sku": "cohb_s1",
              "category": "food",
              "type" : "physical",
              "tags" : ["food", "mexican food"]
          }
      ],
      "shipping_lines":[
        {
          "amount": 0,
          "tracking_number": "TRACK123",
          "carrier": "USPS",
          "method": "Train",
          "metadata": {
             "random_key": "random_value"
          }
        }],
      "customer_info":{
          "name": "John Constantine",
          "phone": "+525533445566",
          "email": "john@meh.com",
          "corporate": False,
          "vertical_info": {}
        },
      "shipping_contact":{
          "phone" : "5544332211",
          "receiver": "Marvin Fuller",
          "between_streets": "Ackerman Crescent",
          "address": {
              "street1": "250 Alexis St",
              "state": "Alberta",
              "country": "MX",
              "postal_code": "23455",
              "metadata":{ "soft_validations": True}
          }
      },
      "fiscal_entity":{
        "tax_id": "AMGH851205MN1",
        "name": "Nike SA de CV",
        "address": {
            "street1": "250 Alexis St",
            "internal_number": "19",
            "external_number": "91",
            "city": "Red Deer",
            "state": "Alberta",
            "country": "CA",
            "postal_code": "33242"
        }
      },
      "charges": [{
        "payment_method":{
          "type":"oxxo_cash"
        },
        "amount": 20000
      }],
      "currency" : "mxn",
      "metadata" : {"test" : "extra info"}
    }

order = conekta.Order.create(data)

#Also you can get the attributes from the conekta response class:
print order.id

#Or in the event of an error, you can expect a ConektaError to be raised
```

Charge via bank:

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'

var data = {
      "line_items": [
          {
              "name": "Box of Cohiba S1s",
              "description": "Imported From Mex.",
              "unit_price": 20000,
              "quantity": 1,
              "sku": "cohb_s1",
              "category": "food",
              "type" : "physical",
              "tags" : ["food", "mexican food"]
          }
      ],
      "shipping_lines":[
        {
          "amount": 0,
          "tracking_number": "TRACK123",
          "carrier": "USPS",
          "method": "Train",
          "metadata": {
             "random_key": "random_value"
          }
        }],
      "customer_info":{
          "name": "John Constantine",
          "phone": "+525533445566",
          "email": "john@meh.com",
          "corporate": False,
          "vertical_info": {}
        },
      "shipping_contact":{
          "phone" : "5544332211",
          "receiver": "Marvin Fuller",
          "between_streets": "Ackerman Crescent",
          "address": {
              "street1": "250 Alexis St",
              "state": "Alberta",
              "country": "MX",
              "postal_code": "23455",
              "metadata":{ "soft_validations": True}
          }
      },
      "fiscal_entity":{
        "tax_id": "AMGH851205MN1",
        "name": "Nike SA de CV",
        "address": {
            "street1": "250 Alexis St",
            "internal_number": "19",
            "external_number": "91",
            "city": "Red Deer",
            "state": "Alberta",
            "country": "CA",
            "postal_code": "33242"
        }
      },
      "charges": [{
        "payment_method":{
          "type":"banorte"
        },
        "amount": 20000
      }],
      "currency" : "mxn",
      "metadata" : {"test" : "extra info"}
    }


order = conekta.Order.create(data)

#Also you can get the attributes from the conekta response class:
print Order.id

#Or in the event of an error, you can expect a ConektaError to be raised
```

# Retrieve events

```python
import conekta

conekta.api_key = '1tv5yJp3xnVZ7eK67m4h'
order.events()
customer.events()
```

## Endpoints

```python
conekta.Order.create()
conekta.Order.find()
conekta.Order.where()
conekta.Order.update()
conekta.Order.capture()
conekta.Order.returns()
conekta.Order.charge()
conekta.Order.createShippingContact()
conekta.Order.createFiscalEntity()
conekta.Order.createLineItem()
conekta.Order.createTaxLine()
conekta.Order.createShippingLine()
conekta.Order.createDiscountLine()
conekta.Order.events()
conekta.Order.void()

conekta.Customer.create()
conekta.Customer.find()
conekta.Customer.where()
conekta.Customer.update()
conekta.Customer.createPaymentSource()
conekta.Customer.createFiscalEntity()
conekta.Customer.createShippingContact()
conekta.Customer.events()

conekta.Log.where({})
```

## Library Development and Testing

You can test the conekta library with nose from the conekta library root:

```sh
$ nosetests
```

To simplify the development and testing process we have provided dockers with the code preloaded, in python 2.7:

```shell
docker pull conekta/conekta-python2.7

docker run -ti conekta/conekta-python2.7 /bin/bash --login
```

and in python 3.4:

```shell
docker pull conekta/conekta-python3.5

docker run -ti conekta/conekta-python3.5 /bin/bash --login
```

## License

Developed in Mexico by [Conekta](https://www.conekta.com). Available with [MIT License](LICENSE).

***

## We are always hiring!

If you are a comfortable working with a range of backend languages (Java, Python, Ruby, PHP, etc) and frameworks, you have solid foundation in data structures, algorithms and software design with strong analytical and debugging skills. Send us your CV and GitHub to quieroser@conekta.com
