#!/usr/bin/python3
""" Handles all default RESTful API action
"""
from models.amenity import Amenity
from models.place import Place
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request
from os import environ


@app_views.route('/places/<place_id>/amenities',
                 methods=['GET'], strict_slashes=False)
def get_amenities(place_id):
        """
        Get the list of amenities for a given place.
        """
        place = storage.get(Place, place_id)
        if not place:
                abort(404, description="Place not found")

        if environ.get('HBNB_TYPE_STORAGE') == 'db':
                amenities = [amenity.to_dict() for amenity in place.amenities]
        else:
                amenities = [storage.get(Amenity, amenity_id).to_dict() 
                             for amenity_id in place.amenity_ids]

        return jsonify(amenities), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>', 
                 methods=['DELETE'], strict_slashes=False)
def delete_amenity(place_id, amenity_id):
        """
        Deletes a amenity from the place.
        """
        place = storage.get(Place, place_id)
        if not place:
                abort(404, description="Place not found")

        amenity = storage.get(Amenity, amenity_id)

        if not amenity:
                abort(404, description="Amenity not found")

        if environ.get('HBNB_TYPE_STORAGE') == 'db':
                if amenity not in place.amenities:
                        abort(404, description="Amenity not in place")
                place.amenities.remove(amenity)
        else:
                if amenity not in place.amenity_id:
                        abort(404, description="Amenity not in place")
                place.amenities.remove(amenity_id)

        storage.save()
        return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>', 
                 methods=['POST'], strict_slashes=False)
def post_amenity(place_id, amenity_id):
        """
        Adds an amenity to a place.
        """
        place = storage.get(Place, place_id)
        if not place:
                abort(404, description="Place not found")

        amenity = storage.get(Amenity, amenity_id)

        if not amenity:
                abort(404, description="Amenity not found")

        if environ.get('HBNB_TYPE_STORAGE') == 'db':
                if amenity in place.amenities:
                        return jsonify(amenity.to_dict()), 200
                else:
                        place.amenities.append(amenity)
        else:
                if amenity in place.amenity_ids:
                        return jsonify(amenity.to_dict()), 200
                else:
                        place.amenity_ids.append(amenity_id)

        storage.save()
        return jsonify(amenity.to_dict()), 201
