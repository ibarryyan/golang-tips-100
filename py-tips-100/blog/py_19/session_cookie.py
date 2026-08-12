"""requests Session 和 cookie 演示"""
import requests


def demo_session_reuse():
    """Session 复用 TCP 连接"""
    with requests.Session() as session:
        session.headers.update({
            "User-Agent": "MyApp/1.0",
            "Authorization": "Bearer token123",
        })

        for i in range(3):
            response = session.get(
                f"https://httpbin.org/get?id={i}", timeout=10
            )
            print(f"请求 {i}: {response.json()['args']}")


def demo_cookie():
    """Session 自动管理 cookie"""
    with requests.Session() as session:
        # 设置 cookie
        session.get("https://httpbin.org/cookies/set?sid=abc123", timeout=10)
        # 读取 cookie
        response = session.get("https://httpbin.org/cookies", timeout=10)
        print(f"当前 cookie: {response.json()['cookies']}")

        # 手动设置 cookie
        session.cookies.set("custom_cookie", "hello")
        response = session.get("https://httpbin.org/cookies", timeout=10)
        print(f"设置后 cookie: {response.json()['cookies']}")


def demo_login_flow():
    """模拟登录流程"""
    with requests.Session() as session:
        # 模拟登录
        login_resp = session.post(
            "https://httpbin.org/post",
            json={"username": "admin", "password": "123456"},
            timeout=10,
        )
        print(f"登录响应码: {login_resp.status_code}")

        # 后续请求自动携带 cookie
        profile_resp = session.get("https://httpbin.org/get", timeout=10)
        print(f"会话 cookie: {session.cookies.get_dict()}")


if __name__ == "__main__":
    print("=== Session 复用 ===")
    demo_session_reuse()

    print("\n=== Cookie 管理 ===")
    demo_cookie()

    print("\n=== 登录流程 ===")
    demo_login_flow()
