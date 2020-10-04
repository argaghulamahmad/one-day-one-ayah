import asyncio

from odoa import ODOA


async def main():
    o = ODOA()

    surah = await o.get_random_surah()
    print(surah.ayah, surah.desc, surah.translate, surah.sound)


if __name__ == '__main__':
    asyncio.run(main())
