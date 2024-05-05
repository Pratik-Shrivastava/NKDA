# Flask Starter Template

This is a starter template for your flask application. Instead of starting your application from bootstraps, have a starting point for your application.

#### The features that are include in this starter application are -

* JWT authentication.
* Role-base access to API endpoint.
* Audit  log for API.
* Pre-existing user management API
* Swagger-UI for development support

#### The app is developed and tested on `Python 3.12.3`

#### To start with the project install all the dependencies &#xA;`pip install -r requirements.txt`

####

### Project Stucture:

```txt
- app/
- database/
- logs/
- .gitignore
- main.py
- README.md
- requirements.txt
```

* The  starting point of the application is `main.py` where you can change the `host, port, debug` for the application.
* The `database/` folder contains the the starting `schema` and `data` to work on.
* The `logs/` folder contains daily log.
* The `app/` is the `main_module` of the application.

```txt
- app/
  -- app_config/
      -- config.py ## application config (databse, logs, jwt etc.)
  -- decorators/
      -- authorizer.py ## @decorator for authorization
  -- enum/
      -- user_role_enum.py ## USER_ROLES enum for authorization
  -- orm/
  -- routes/
    -- user/
      -- dao_service.py ## operation related to data-models
      -- payload.py ## payload model for swagger documentation
      -- response.py ## response model for swagger documentation
      -- routes.py
      -- validator.py
```

* The `orm` directory holds all the data-models `(sqlAlchemy)` for the project.
* The `routes` directory holds all the routes for the application. Each sub-folder represent different route module for application.

* Now you can continue creating routes by implementing  `routes.py`

### `routes.py` file and its convention:

```python
logger = get_logger(__name__)
ns = api.namespace(
    name=os.path.dirname(__file__).split(os.sep)[-1].replace('_', '-'),
    description='API connected to user module',
    ordered=False
)
```
* This above section setting up the `logger` to log and create the `/user` route module (as the sub-folder name was `user`).

```python
@ns.route('/add', methods=['POST'])
class AddUser(Resource):

    @ns.doc(security=SECURITY)
    @ns.expect(*add_user_payload())
    @ns.response(SUCCESS_CODE, INSERT_SUCCESS_MESSAGE, add_user_response())
    @jwt_required()
    @is_authorized([USER_ROLE.ADMIN])
    def post(self, jwt_data):
```

* `@ns.route` creates `/user/add` route where the request type `POST`
* `@ns.doc(security=SECURITY)` Provide swagger-documentation, if API is authenticated.
* `@ns.expect(*add_user_payload())`&#x20;
  * This `@ns.expect` block create documentation regarding the need of API `(payload & queryParams)`. All these payload related functions should be put in `payload.py`
* `@ns.response(SUCCESS_CODE, INSERT_SUCCESS_MESSAGE, add_user_response())`&#x20;
  * This `@ns.response` block create documentation regarding the response of the API. All these response related functions should be put in `response.py`
  * Change the `success status` and `message` according to your application.
* `@jwt_required()` to make API authenticated and also pass additional parameter `jwt_data` to the mapped method.
* `@is_authorized([USER_ROLE.ADMIN])` make sure which users are privileged to access the API based on `USER_ROLE` enum.

> *Depending on the API type the method name of the class is mapped to the corresponding API. For example `/add` API request type is `POST` so it will be mapped to the`post(self, jwt_data)` method of the class.*

> *It is recommended to create individual class for each individual endpoints inside the `routes.py`*



### Request Validation:

```python
try:
    validator = AddUserValidator()
    payload = validator.load(request.get_json())

    user_id = add_user(payload)
    return {'code': SUCCESS_CODE, 'message': INSERT_SUCCESS_MESSAGE}
        
except ValidationError as e:
    return {
        'code': VALIDATION_ERROR_CODE, 
        'message': VALIDATION_ERROR_MESSAGE,
        'errors': e.normalized_messages()
    }
```
* To validate request payload we use `marshmallow` package.
* In the bellow example `AddUserValidator()` holds the validation logic and if invalid throws `ValidationError`.
* All the validation related classes should be put  in `validator.py`
