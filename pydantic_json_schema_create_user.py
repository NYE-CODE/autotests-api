from clients.users.public_users_client import CreateUserResponseSchema, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.assertions.schema import validate_json_schema

from tools.fakers import get_random_email


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="qwer12345",
    first_name="Ivan",
    last_name="Ivanov",
    middle_name="Ivanovich"
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_json = create_user_response.json()
create_user_response_schema = CreateUserResponseSchema.model_json_schema()


validate_json_schema(instance=create_user_response_json, schema=create_user_response_schema)

