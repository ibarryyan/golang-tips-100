"""mock 和 patch 使用演示"""
import pytest
from unittest.mock import patch, Mock, call


# === 被测代码 ===
import requests


def get_user_info(user_id):
    resp = requests.get(f"https://api.example.com/users/{user_id}")
    return resp.json()


def fetch_all_users(user_ids):
    results = []
    for uid in user_ids:
        resp = requests.get(f"https://api.example.com/users/{uid}")
        results.append(resp.json())
    return results


# === 使用装饰器 patch ===
@patch("requests.get")
def test_get_user_info_decorator(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"name": "Tom", "id": 1}
    mock_get.return_value = mock_response

    result = get_user_info(1)

    assert result["name"] == "Tom"
    assert result["id"] == 1
    mock_get.assert_called_once_with("https://api.example.com/users/1")


# === 使用 context manager ===
def test_get_user_info_context():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"name": "Jerry", "id": 2}

        result = get_user_info(2)

        assert result["name"] == "Jerry"
        mock_get.assert_called_once()


# === 使用 fixture patch ===
@pytest.fixture
def mock_requests():
    with patch("requests.get") as mock:
        mock.return_value.json.return_value = {"name": "Mock", "id": 0}
        yield mock


def test_with_fixture(mock_requests):
    result = get_user_info(999)
    assert result["name"] == "Mock"
    mock_requests.assert_called_once()


# === side_effect：多次调用不同返回值 ===
@patch("requests.get")
def test_side_effect_multiple(mock_get):
    mock_get.side_effect = [
        Mock(json=lambda: {"name": "first"}),
        Mock(json=lambda: {"name": "second"}),
    ]

    r1 = get_user_info(1)
    r2 = get_user_info(2)

    assert r1["name"] == "first"
    assert r2["name"] == "second"
    assert mock_get.call_count == 2


# === side_effect：模拟异常 ===
@patch("requests.get")
def test_side_effect_exception(mock_get):
    mock_get.side_effect = ConnectionError("网络错误")

    try:
        get_user_info(1)
        assert False, "应该抛出 ConnectionError"
    except ConnectionError as e:
        assert "网络错误" in str(e)


# === 验证调用参数 ===
@patch("requests.get")
def test_call_args(mock_get):
    mock_get.return_value.json.return_value = {}

    fetch_all_users([1, 2, 3])

    assert mock_get.call_count == 3
    # 检查每次调用的参数
    expected_calls = [
        call(f"https://api.example.com/users/{uid}")
        for uid in [1, 2, 3]
    ]
    mock_get.assert_has_calls(expected_calls)


if __name__ == "__main__":
    import subprocess
    result = subprocess.run(
        ["python", "-m", "pytest", __file__, "-v"],
        capture_output=True, text=True,
    )
    print(result.stdout)
