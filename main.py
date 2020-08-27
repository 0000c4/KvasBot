from vkbottle import Bot, Message, keyboard_gen, VKError
import random
import generator
bot = Bot("6c559a97ae943bac9c3036fc1d331e777c5504a2a994a032937805ef4758d1b477e683a0be1e4a833b5a2")
@bot.on.message_handler()
async def handle(_):
    if random.randint(0,8) == 3:
        var = random.randint(0,3)
        if var == 0:
            return generator.genOne()
        elif var == 1:
            return generator.genTwo()
        elif var == 2:
            return generator.genThree()
        elif var == 3:
            return generator.genFour()
bot.run_polling()
