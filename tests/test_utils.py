from pingout.utils import validate_uuid

def test_valid_UUID_is_validated():
    valid_uuid = '3106a663a8f642b8bd79dac0469bd739'
    validation = validate_uuid(valid_uuid)
    assert validation == true

def test_invalid_UUID_is_validated():
    # It's an invalid UUID because it has a 'g', which hexadecimal values can't have
    invalid_uuid = '3106a663a8g642b8bd79dac0469bd739'
    validation = validate_uuid(valid_uuid)
    assert validation == false
