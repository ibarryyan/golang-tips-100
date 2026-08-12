"""httpx 和 aiohttp 异步请求演示"""
import asyncio
import time


def demo_httpx_sync():
    """httpx 同步用法"""
    import httpx

    response = httpx.get("https://httpbin.org/get", params={"name": "Tom"}, timeout=10)
    print(f"httpx 同步: {response.json()['args']}")


async def demo_httpx_async():
    """httpx 异步用法"""
    import httpx

    async with httpx.AsyncClient(timeout=10) as client:
        urls = [f"https://httpbin.org/delay/1?id={i}" for i in range(3)]

        start = time.time()
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        print(f"httpx 异步: {time.time() - start:.2f}s 完成 {len(responses)} 个请求")
        for r in responses:
            print(f"  {r.json()['args']}")


async def demo_aiohttp():
    """aiohttp 异步用法"""
    import aiohttp

    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        urls = [f"https://httpbin.org/delay/1?id={i}" for i in range(3)]

        start = time.time()
        tasks = [session.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        print(f"aiohttp 异步: {time.time() - start:.2f}s 完成 {len(responses)} 个请求")
        for r in responses:
            data = await r.json()
            print(f"  {data['args']}")
            r.close()


async def main():
    print("=== httpx 同步 ===")
    demo_httpx_sync()

    print("\n=== httpx 异步 ===")
    await demo_httpx_async()

    print("\n=== aiohttp 异步 ===")
    await demo_aiohttp()


if __name__ == "__main__":
    asyncio.run(main())
