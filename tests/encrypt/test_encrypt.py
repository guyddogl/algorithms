from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(27041990, 2)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("GUYDDO", "2")
    assert encrypt_message("GGUUYY", 3) == "UGG_YYU"
    assert encrypt_message("GUYDDO", 4) == "OD_DYUG"
    assert encrypt_message("GUYDDOGL", 10) == "LGODDYUG"
