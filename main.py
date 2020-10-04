import asyncio

from odoa import ODOA


async def main():
    o = ODOA()
    surah = await o.get_random_surah()
    print(surah)


if __name__ == '__main__':
    asyncio.run(main())
