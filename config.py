from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("8408766977:AAFU7tgGxkb09RC82MWlkCDmaxSYtWxr_x4")  # Bot Token
ADMINS = env.list("7759711404")  # adminlar ro'yxati
