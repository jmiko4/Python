import pytest
from photo_wishlist_scraper import get_info_mpb, get_info_keh,csv_reader, write_dicts_to_csv,write_url_to_csv, url_reader, refresh_prices



def test_get_info_mpb():
    mpb = get_info_mpb('https://www.mpb.com/en-us/used-equipment/used-photo-and-video/used-lenses/used-canon-fit-lenses/canon-ef-70-200mm-f-2-8-l-is-ii-usm/')
    assert isinstance(mpb, dict), "get_info_mpb function must return a dictionary"

def test_get_info_keh():
    keh = get_info_keh('https://www.keh.com/shop/canon-ef-2751b002-70-mm-200-mm-f-2-8-telephoto-zoom-lens.html')
    assert isinstance(keh, dict), "get_info_keh function must return a dictionary"

def test_csv_writer():
    csv = csv_reader('Wishlist_Program/wishlist.csv')
    assert isinstance(csv,list), "test_csv_writer function must return a list"

def test_url_reader():
    reader=url_reader()
    assert isinstance(reader,list)

def test_refresh_prices():
    assert refresh_prices()==True


def test_write_dicts_to_csv():
    URL_MPB = "https://www.mpb.com/en-us/used-equipment/used-photo-and-video/used-lenses/used-canon-fit-lenses/canon-ef-70-200mm-f-2-8-l-is-ii-usm/"
    mpb_dict =get_info_mpb(URL_MPB)
    URL_KEH = "https://www.keh.com/shop/canon-ef-2751b002-70-mm-200-mm-f-2-8-telephoto-zoom-lens.html"
    keh_dict = get_info_keh(URL_KEH)
    dicts= []
    dicts.append(mpb_dict)
    dicts.append(keh_dict)
    assert write_dicts_to_csv(dicts) == True

def test_write_url_to_csv():
    assert write_url_to_csv('google.com') == True

# def test


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
