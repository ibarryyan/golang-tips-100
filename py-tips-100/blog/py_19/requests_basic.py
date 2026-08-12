"""requests 库基础用法演示"""
import requests


def demo_get():
    """GET 请求与参数传递"""
    params = {
        "name": "Tom",
        "age": 18,
        "city": "北京",
    }
    response = requests.get("https://httpbin.org/get", params=params, timeout=10)
    print(f"GET 状态码: {response.status_code}")
    print(f"GET 参数: {response.json()['args']}")


def demo_post_json():
    """POST JSON"""
    payload = {"username": "admin", "password": "123456"}
    response = requests.post("https://httpbin.org/post", json=payload, timeout=10)
    print(f"POST JSON: {response.json()['json']}")


def demo_post_form():
    """POST 表单"""
    payload = {"username": "admin", "password": "123456"}
    response = requests.post("https://httpbin.org/post", data=payload, timeout=10)
    print(f"POST 表单: {response.json()['form']}")


def demo_headers():
    """自定义请求头"""
    headers = {
        "User-Agent": "MyApp/1.0",
        "Authorization": "Bearer token123",
    }
    response = requests.get("https://httpbin.org/headers", headers=headers, timeout=10)
    print(f"请求头: {response.json()['headers']}")


def demo_response():
    """响应对象常用属性"""
    response = requests.get("https://httpbin.org/json", timeout=10)
    print(f"状态码: {response.status_code}")
    print(f"编码: {response.encoding}")
    print(f"内容类型: {response.headers.get('Content-Type')}")
    print(f"JSON: {response.json()}")
    print(f"文本前50字: {response.text[:50]}")


if __name__ == "__main__":
    demo_get()
    demo_post_json()
    demo_post_form()
    demo_headers()
    demo_response()
