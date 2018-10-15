# -*- coding: utf-8 -*-
from collectibles.models import *
import csv

locations_file = "collectibles/migrations/data/locations.csv"
items_file = "collectibles/migrations/data/items.csv"
contents_file = "collectibles/migrations/data/content.csv"


locations_dict = {}

with open(locations_file, encoding='utf-8') as locations:
    reader = csv.reader(locations, delimiter=';')
    header = next(reader, None)
    for name,desc,x,y,img in reader:
        l = Location(name=name,description=desc, x=x, y=y, img_path=img)
        locations_dict[name] = l
        l.save()

items_dict = {}
with open(items_file, encoding='utf-8') as items:
    reader = csv.reader(items, delimiter=';')
    header = next(reader, None)
    for name, desc, img, loc in reader:
        i = Item(name=name, description=desc,
                 icon_path=img, location=locations_dict[loc])
        items_dict[name] = i
        i.save()

contents_dict = {}
with open(contents_file, encoding='utf-8') as contents:
    reader = csv.reader(contents, delimiter=';')
    header = next(reader, None)
    for title,desc,t,cont,loc in reader:
        c = Content(title=title, description=desc, content_type=t,
                    content=cont, location=locations_dict[loc])
        contents_dict[title] = c
        c.save()

"""
print(locations_dict)
print(items_dict)
print(contents_dict)
"""
