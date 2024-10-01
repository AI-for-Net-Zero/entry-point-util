from unittest.mock import patch, Mock
import pytest

from entry_point_util import entry_point_getter, get_partially_ordered_list

def test_get_single_by_name(mock_iter_entry_points):
    
    @patch('entry_point_util.iter_entry_points', mock_iter_entry_points)
    def inner():
        eps = entry_point_getter( ('invenio_accounts_ui',
                                   None,
                                   'invenio_base.apps') )

        assert len(eps) == 1
        ep = list(eps)[0]
        assert ep.name == 'invenio_accounts_ui'
        assert ep.value == 'invenio_accounts:InvenioAccountsUI'

    inner()

def test_get_single_by_value(mock_iter_entry_points):
    
    @patch('entry_point_util.iter_entry_points', mock_iter_entry_points)
    def inner():
        eps = entry_point_getter( (None,
                                   'invenio_accounts:InvenioAccountsUI',
                                   'invenio_base.apps') )

        assert len(eps) == 1
        ep = list(eps)[0]
        assert ep.name == 'invenio_accounts_ui'
        assert ep.value == 'invenio_accounts:InvenioAccountsUI'

    inner()

def test_get_multiple(mock_iter_entry_points):
    
    @patch('entry_point_util.iter_entry_points', mock_iter_entry_points)
    def inner():
        eps = entry_point_getter( ('invenio_records_ui',
                                   None,
                                   'invenio_base.apps') )

        assert len(eps) == 2
        
        _test = lambda e: e.name == 'invenio_records_ui'\
            and e.group == 'invenio_base.apps'\
            and (e.value == 'invenio_records_ui:InvenioRecordsUI' \
                 or e.value == 'invenio_records_ui:SomethingElse')

        assert all([_test(e) for e in eps])

    inner()

def test_get_entire_group(mock_iter_entry_points):

    @patch('entry_point_util.iter_entry_points', mock_iter_entry_points)
    def inner():
        eps = entry_point_getter( (None,
                                   'invenio_accounts:InvenioAccountsUI',
                                   'invenio_base.apps') )

        assert len(eps) == 1
        ep = list(eps)[0]
        assert ep.name == 'invenio_accounts_ui'

    inner()

def test_get_none(mock_iter_entry_points):

    @patch('entry_point_util.iter_entry_points', mock_iter_entry_points)
    def inner():
        eps = entry_point_getter( ('invenio_records_ui',
                                   'something_not_there',
                                   'invenio_base.apps') )

        assert len(eps) == 0

    inner()


def test_get_none_group(mock_iter_entry_points):

    @patch('entry_point_util.iter_entry_points', mock_iter_entry_points)
    def inner():
        eps = entry_point_getter( ('invenio_records_ui',
                                   'something_not_there',
                                   'invenio_base.appppppps') )

        assert len(eps) == 0

    inner()


def test_get_no_group_RunimeError(mock_iter_entry_points):

    @patch('entry_point_util.iter_entry_points', mock_iter_entry_points)
    def inner():
        eps = entry_point_getter( ('invenio_records_ui',
                                   'something_not_there',
                                   None) )

    with pytest.raises(RuntimeError):
        inner()


def test_get_partially_ordered_list():
    fruits = set(['apples', 'plums', 'oranges', 'grapes',
                  'pears', 'grapefruit', 'cherries',
                  'limes', 'lemons', 'kiwis', 'mangoes'])

    initial = set(['mangoes', 'kiwis', 'pears'])
    
    ordered = ['apples', 'cherries']

    out = get_partially_ordered_list(fruits, initial, ordered)
    
    the_rest = set(['plums', 'oranges', 'grapes',
                    'grapefruit', 'limes', 'lemons'])

    assert set(out[0:3]) == initial
    assert out[3:5] == ['apples', 'cherries']
    assert set(out[5:]) == the_rest
    

    
