from qq_music_playlist_export import extract_playlist_id

def test_extract_id_from_number():
    assert extract_playlist_id("123456789") == "123456789"

def test_extract_id_from_url():
    assert extract_playlist_id("https://y.qq.com/n/ryqq/playlist/9044196528") == "9044196528"

def test_extract_id_from_text():
    assert extract_playlist_id("歌单ID: 9044196528") == "9044196528"
