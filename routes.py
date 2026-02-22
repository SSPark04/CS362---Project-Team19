"""
routes.py
Defines REST API endpoints for event CRUD and filtering.
"""

import traceback
from flask import Blueprint, request, jsonify
import event_service


api = Blueprint("api", __name__)


@api.route("/api/events", methods=["GET"])
def get_events():
    """
    GET /api/events
    Returns all events, with optional filtering.
    Query params:
        ?filter=today    -> events happening today
        ?filter=week     -> events this week
        ?start=YYYY-MM-DD&end=YYYY-MM-DD -> custom date range
        ?sort=title|date|start_time
        ?order=asc|desc
    """
    try:
        filter_type = request.args.get("filter", None)
        start_date = request.args.get("start", None)
        end_date = request.args.get("end", None)
        sort_by = request.args.get("sort", None)
        order = request.args.get("order", "asc")

        # Apply date filter if provided
        if filter_type == "today" or filter_type == "week":
            events = event_service.filter_events_by_date(filter_type)
        elif start_date and end_date:
            events = event_service.filter_events_by_date("range", start_date, end_date)
        else:
            events = event_service.get_all_events()

        # Apply sorting if requested
        if sort_by:
            reverse = (order == "desc")
            events = event_service.sort_events(events, sort_by, reverse)

        return jsonify(events), 200

    except Exception as e:
        print("Error in get_events:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@api.route("/api/events/<event_id>", methods=["GET"])
def get_event(event_id):
    """
    GET /api/events/<event_id>
    Returns a single event by its ID.
    """
    try:
        event = event_service.get_event(event_id)

        if event is None:
            return jsonify({"error": "Event not found."}), 404

        return jsonify(event), 200

    except Exception as e:
        print("Error in get_event:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@api.route("/api/events", methods=["POST"])
def create_event():
    """
    POST /api/events
    Creates a new event.
    Request body: JSON object with event fields (no event_id needed).
    """
    try:
        event_data = request.get_json(silent=True)

        if event_data is None:
            return jsonify({"error": "Request body must be JSON."}), 400

        event, error = event_service.create_event(event_data)

        if event is None:
            return jsonify({"error": error}), 400

        return jsonify(event), 201

    except Exception as e:
        print("Error in create_event:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@api.route("/api/events/<event_id>", methods=["PUT"])
def update_event(event_id):
    """
    PUT /api/events/<event_id>
    Updates an existing event.
    Request body: JSON object with fields to update.
    """
    try:
        updated_fields = request.get_json(silent=True)

        if updated_fields is None:
            return jsonify({"error": "Request body must be JSON."}), 400

        event, error = event_service.update_event(event_id, updated_fields)

        if event is None:
            return jsonify({"error": error}), 404

        return jsonify(event), 200

    except Exception as e:
        print("Error in update_event:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@api.route("/api/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    """
    DELETE /api/events/<event_id>
    Deletes an event by its ID.
    """
    try:
        result = event_service.delete_event(event_id)

        if not result:
            return jsonify({"error": "Event not found."}), 404

        return jsonify({"message": "deleted"}), 200

    except Exception as e:
        print("Error in delete_event:")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
