import os


class Config(object):
    # form safety key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'S<7g8{k&GM_MEPp$'