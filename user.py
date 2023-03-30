from datetime import datetime
from flask import abort, make_response
from data_base import *
from pony.orm import db_session


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


@db_session
def read_all():
    users = list()
    for user in Usuario.select(lambda U: U.usuario_status == 0):
        users.append(user.to_json())
    return users


@db_session
def create(user):
    user_id = user.get("user_id")
    user_name = user.get("user_name", "")
    user_email = user.get("user_email", "")
    user_senha = user.get("user_senha", "")
    user = Usuario.get(usuario_id = user_id)

    if not user:
        return Usuario(usuario_id = user_id, usuario_nome = user_name, usuario_email = user_email, usuario_status = 0, usuario_senha = user_senha).to_json()
    else:
        abort(
            406,
            f"User with last name {user_id} already exists",
        )


@db_session
def read_one(user_id):
    user = Usuario.get(usuario_id = user_id)
    if user:
        return user.to_json()
    else:
        abort(
            404, f"Person with ID {user_id} not found"
        )


@db_session
def update(user_id, user):
    user_up = Usuario.get(usuario_id = user_id) 
    if user_up:
        user_up.usuario_nome = user.get("user_name", user_up.usuario_nome)
        return user_up.to_json()
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )


@db_session
def delete(user_id):
    user_up = Usuario.get(usuario_id = user_id) 
    if user_up:
        user_up.delete()
        return make_response("Successfully deleted user")
    else:
        abort(
            404,
            f"Person with ID {user_id} not found"
        )