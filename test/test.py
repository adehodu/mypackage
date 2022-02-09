from mypackage import myModule

def test_top_n():
    """ Make sure top_n() works correctly """

    assert myModule.top_n([4,7,1,9,2], 3) == [9,7,4], 'Incorrect'
    assert myModule.top_n([13,7,11,9,21], 4) == [21,13,11,9], 'Incorrect'