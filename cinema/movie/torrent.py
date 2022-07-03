import sys
import bencodepy
import hashlib
import base64
from .models import Movie


def make_magnet_from_file(film_id) :
    movie = Movie.Model.get(movieId=film_id)
    metadata = bencodepy.decode_from_file(movie.torrent)
    subj = metadata[b'info']
    hashcontents = bencodepy.encode(subj)
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest).decode()
    return 'magnet:?'\
             + 'xt=urn:btih:' + b32hash\
             + '&dn=' + metadata[b'info'][b'name'].decode()\
             + '&tr=' + metadata[b'announce'].decode()\
             + '&xl=' + str(metadata[b'info'][b'length'])


