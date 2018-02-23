import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await  orm.create_pool(loop=loop, user="www.data", password="www",database="awsome")
    u = User(name= "userA",email = "12@qq.com",password="123456",image="about:blank")
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
#
# import orm
# from models import User, Blog, Comment
# import asyncio
#
# async def test(loop):
#     await orm.create_pool(loop=loop, user='cc', password='password', db='myblog')
#     u = User(name='test1as5', email='thest140@exafsample.com', passwd='1k32456789010', image='about:blank')
#
#     await u.save()
#     # await User.findAll()
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# print('test')
# print('success')
# loop.close()