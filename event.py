from datetime import datetime
from flask import abort, make_response
from data_base import *
from pony.orm import db_session

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


@db_session
def read_all():
    events = list()
    for event in Evento.select(lambda U: U.evento_status == 1):
        events.append(event.to_json())
    return events


@db_session
def create(event):
    event_id = event.get("event_id")
    event_data = event.get("event_data")
    event_descricao = event.get("event_descricao", "")
    event_nome = event.get("event_nome", "")
    event_status = event.get("event_status")
    user_id = event.get("user_id")
    event = Evento.get(evento_id = event_id)

    if not event:
        return Evento(evento_id = event_id, evento_data_hora = event_data, evento_descricao = event_descricao, evento_nome = event_nome, evento_status = event_status, usuario = user_id).to_json()
    else:
        abort(
            406,
            f"Event {event_id} already exists",
        )


@db_session
def read_one(event_id):
    event = Evento.get(evento_id = event_id)
    if event:
        return event.to_json()
    else:
        abort(
            404, f"Event with ID {event_id} not found"
        )


@db_session
def update(event_id, event):
    event_up = Evento.get(evento_id = event_id)
    if event_up:
        event_up.evento_data_hora = event.get("event_data", event_up.evento_data_hora)
        event_up.evento_nome = event.get("event_nome", event_up.evento_nome)
        event_up.evento_descricao = event.get("event_descricao", event_up.evento_descricao)
        event_up.evento_nome = event.get("event_nome", event_up.evento_nome)
        return event_up.to_json()
    
    else:
        abort(
            404,
            f"Event with ID {event_id} not found"
        )


@db_session
def delete(event_id):
    event_up = Evento.get(evento_id = event_id)
    if event_up:
        event_up.delete()
        return make_response("Successfully deleted event")
    else:
        abort(
            404,
            f"Event with ID {event_id} not found"
        )