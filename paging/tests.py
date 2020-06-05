import unittest2

from paging.helpers import paginate
from paging.paginators import *

from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'paging',
        ]
    )

class PagingUnitTest(unittest2.TestCase):
    def test_better_paginator(self):
        objects = list(range(1, 100))
        
        paginator = BetterPaginator(objects, 1)
        for num in objects:
            page = paginator.get_context(num)
            self.assertEqual(page['objects'], [num])
            self.assertEqual(page['has_next'], num < 99)
            self.assertEqual(page['has_previous'], num > 1)
            self.assertEqual(page['is_first'], num == 1)
            self.assertEqual(page['is_last'], num == 99)
            self.assertEqual(page['previous_page'], num - 1 if num else False)
            self.assertEqual(page['next_page'], num + 1)
            self.assertEqual(page['page'], num)
            self.assertEqual(page['num_pages'], 99)
            # XXX: this test could be improved
            self.assertTrue(page['page_range'])

    def test_endless_paginator(self):
        objects = list(range(1, 100))
        
        paginator = EndlessPaginator(objects, 1)
        for num in objects:
            page = paginator.get_context(num)
            self.assertEqual(page['objects'], [num])
            self.assertEqual(page['has_next'], num < 99)
            self.assertEqual(page['has_previous'], num > 1)
            self.assertEqual(page['is_first'], num == 1)
            self.assertEqual(page['is_last'], num == 99)
            self.assertEqual(page['previous_page'], num - 1 if num else False)
            self.assertEqual(page['next_page'], num + 1)
            self.assertEqual(page['page'], num)
