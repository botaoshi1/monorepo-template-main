# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemUpdater:
    def update(self, item):
        pass

class NormalItemUpdater(ItemUpdater):
    def update(self, item):
        item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

        if item.quality > 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0

class AgedBrieItemUpdater(ItemUpdater):
    def update(self, item):
        item.quality += 1
        item.sell_in -= 1

        if item.quality > 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0

class BackstagePassItemUpdater(ItemUpdater):
    def update(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0

        if item.quality > 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0

class SulfurasItemUpdater(ItemUpdater):
    def update(self, item):
        item.quality = 80

class ConjuredItemUpdater(ItemUpdater):
    def update(self, item):
        item.quality -= 2
        item.sell_in -= 1

        if item.quality > 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0

class GildedRose(object):

    ITEM_UPDATERS = {
        "Aged Brie": AgedBrieItemUpdater(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassItemUpdater(),
        "Sulfuras, Hand of Ragnaros": SulfurasItemUpdater(),
    }

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name in self.ITEM_UPDATERS:
                self.ITEM_UPDATERS[item.name].update(item)
            elif item.name[:8] == "Conjured":
                ConjuredItemUpdater().update(item)
            else:
                NormalItemUpdater().update(item)