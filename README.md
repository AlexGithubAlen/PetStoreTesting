# Swagger Petstore API

This repository contains the Swagger Petstore API, which serves as a demonstration of how to implement and document RESTful APIs using the Swagger specification. Swagger Petstore offers a range of endpoints for managing pets, orders, and user information.

## Base URL
[petstore.swagger.io/v2](https://petstore.swagger.io/v2)

## Version
1.0.7

## OpenAPI Specification (OAS)
2.0

## Authorization
To test authorization filters, you can use the API key `special-key`.

## Schemes
The API supports HTTPS for secure communication.

## Endpoints

### Pet Operations
- **Add a new pet**: `POST /pet`
- **Update an existing pet**: `PUT /pet`
- **Find pet by ID**: `GET /pet/{petId}`
- **Updates a pet in the store with form data**: `POST /pet/{petId}`
- **Deletes a pet**: `DELETE /pet/{petId}`
- **Uploads an image for a pet**: `POST /pet/{petId}/uploadImage`
- **Finds pets by status**: `GET /pet/findByStatus`
- **Finds pets by tags**: `GET /pet/findByTags`

### Store Operations
- **Returns pet inventories by status**: `GET /store/inventory`
- **Place an order for a pet**: `POST /store/order`
- **Find purchase order by ID**: `GET /store/order/{orderId}`
- **Delete purchase order by ID**: `DELETE /store/order/{orderId}`

### User Operations
- **Creates list of users with given input array**: `POST /user/createWithList`
- **Get user by username**: `GET /user/{username}`
- **Update user**: `PUT /user/{username}`
- **Delete user**: `DELETE /user/{username}`
- **Logs user into the system**: `GET /user/login`
- **Logs out current logged-in user session**: `GET /user/logout`
- **Creates list of users with given input array**: `POST /user/createWithArray`
- **Create user**: `POST /user`

## Models
- ApiResponse
- Category
- Pet
- Tag
- Order
- User

## License
Apache 2.0
