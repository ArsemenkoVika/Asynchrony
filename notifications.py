import asyncio

async def send_notification(user, delay):
    print(f"Начинается отправка уведомления для {user}...")

    await asyncio.sleep(delay)
    print(f"Уведомление для {user} отправлено! (ждали {delay} сек.)")

async def main():
    users = [("Alice", 2), ("Bob", 3), ("Charlie", 1), ("Diana", 4)]

    if not users:
        print("Список пользователей пуст.")
        return

    tasks = []
    for user, delay in users:
        task = asyncio.create_task(send_notification(user, delay))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())