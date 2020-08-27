from vkbottle import Bot, Message, keyboard_gen, VKError
import random
import generator
bot = Bot("TOKEN")
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
