# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item_quality_drop(self):
        items = [Item("foo", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 9)
    
    def test_normal_item_quality_degrade_double(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 8)

    def test_normal_item_quality_be_zero(self):
        items = [Item("foo", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_quality_increase(self):
        items = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 11)
    
    def test_aged_brie_quality_be_maximum(self):
        items = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 50)

    def test_backstage_pass_quality_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 14)
        self.assertEqual(items[0].quality, 11)

    def test_backstage_pass_quality_increase_double(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 5)
        self.assertEqual(items[0].quality, 12)

    def test_backstage_pass_quality_increase_triple(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 13)

    def test_backstage_pass_quality_be_maximum(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_backstage_pass_quality_degrade_below_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 0)
    
    def test_sulfuras_quality_be_constant(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 5)
        self.assertEqual(items[0].quality, 80)

    def test_conjured_item_quality_drop(self):
        items = [Item("Conjured Mana Cake", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[0].quality, 8)


if __name__ == '__main__':
    unittest.main()
