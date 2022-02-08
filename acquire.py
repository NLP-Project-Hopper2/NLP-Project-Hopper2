#### Pulled from class will need to add values

"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests

from env import github_token, github_username

# TODO: Make a github personal access token.
#     1. Go here and generate a personal access token https://github.com/settings/tokens
#        You do _not_ need select any scopes, i.e. leave all the checkboxes unchecked
#     2. Save it in your env.py file under the variable `github_token`
# TODO: Add your github username to your env.py file under the variable `github_username`
# TODO: Add more repositories to the `REPOS` list below.

REPOS = [
    'python-discord/bot',
 'discord-tickets/bot',
 'go-chat-bot/bot',
 'SuMaiKaDe/bot',
 'microsoft/BotBuilder-Samples',
 'GAwesomeBot/bot',
 'roughike/BottomBar',
 'mithun-prasad/Bot',
 'boto/boto3',
 'howdyai/botkit',
 'thinkpixellab/bot',
 'gunthercox/ChatterBot',
 'boto/boto',
 'Ashok-Varma/BottomNavigation',
 'BotsAppOfficial/BotsApp',
 'edeng23/binance-trade-bot',
 'ruicky/jd_sign_bot',
 'microsoft/BotFramework-WebChat',
 'bottlepy/bottle',
 'botpress/botpress',
 'FireDiscordBot/bot',
 'python-telegram-bot/python-telegram-bot',
 'thoughtbot/factory_bot',
 'eternnoir/pyTelegramBotAPI',
 'microsoft/botframework-sdk',
 'Urinx/WeixinBot',
 'ittianyu/BottomNavigationViewEx',
 'GramAddict/bot',
 'wangshub/Douyin-Bot',
 'soarcn/BottomSheet',
 'microsoft/BotFramework-Emulator',
 'Mikibot/bot',
 'php-telegram-bot/core',
 'rubenlagus/TelegramBots',
 'freqtrade/freqtrade',
 'Just-Some-Bots/MusicBot',
 'liuwons/wxBot',
 'InstaPy/InstaPy',
 'botman/botman',
 'Nurutomo/wabot-aq',
 'twopg/Bot',
 'Cog-Creators/Red-DiscordBot',
 'NecronomiconCoding/NecroBot',
 'Flipboard/bottomsheet',
 'MhankBarBar/whatsapp-bot',
 'jagrosh/MusicBot',
 'yagop/node-telegram-bot-api',
 'maestron/botnets',
 'Superalgos/Superalgos',
 'SciSharp/BotSharp',
 '1inch/shieldy',
 'boto/botocore',
 'lcdevelop/ChatBotCourse',
 'tgbot-collection/YYeTsBot',
 'aiogram/bot',
 'RitaBot-Project/RitaBot',
 'kyb3r/modmail',
 'breakdowns/slam-mirrorbot',
 'hubotio/hubot',
 'PokemonGoF/PokemonGo-Bot',
 'bottlerocket-os/bottlerocket',
 'acrosa/bot',
 'Apostolique/Agar.io-bot',
 'botui/botui',
 'shaohui10086/BottomDialog',
 'sephiroth74/Material-BottomNavigation',
 'randombit/botan',
 'microsoft/BotFramework-Composer',
 'Yoctol/bottender',
 'Jessecar96/SteamBot',
 'SudhanPlayz/Discord-MusicBot',
 'whittlem/pycryptobot',
 'microsoft/BotFramework-BlogSamples',
 'offu/WeRoBot',
 'thoughtbot/factory_bot_rails',
 'maaaxim/bot',
 'DopplerHQ/awesome-bots',
 'Kwoth/NadekoBot',
 'chaychan/BottomBarLayout',
 'VazkiiMods/Botania',
 'BotLibre/BotLibre',
 'TelegramBots/Telegram.Bot',
 'ArugaZ/whatsapp-bot',
 'anasty17/mirror-leech-telegram-bot',
 'chrisleekr/binance-trading-bot',
 'esthercrawford/EstherBot',
 'malwares/Botnet',
 'pytorch/botorch',
 'CyberPunkMetalHead/Binance-volatility-trading-bot',
 'KoreaEva/Bot',
 'ZerioDev/Music-bot',
 'subinps/VCPlayerBot',
 'telegraf/telegraf',
 'ctubio/Krypto-trading-bot',
 'fbsamples/messenger-bot-samples',
 'PaulSonOfLars/tgbot',
 'lzzy12/python-aria-mirror-bot',
 'Haehnchen/crypto-trading-bot',
 'tdlib/telegram-bot-api',
 'google/bottery',
 'mpcabete/bombcrypto-bot',
 'facebookarchive/mention-bot',
 'aryanvikash/Youtube-Downloader-Bot',
 'philliphsu/BottomSheetPickers',
 'dice-discord/bot',
 'go-telegram-bot-api/telegram-bot-api',
 'microsoft/botframework-solutions',
 'line/line-bot-sdk-python',
 'isl-org/OpenBot',
 'linuxacademy/content-lambda-boto3',
 'viperadnan-git/google-drive-telegram-bot',
 'yagop/telegram-bot',
 'javiersantos/BottomDialogs',
 'irazasyed/telegram-bot-sdk',
 'Androz2091/AtlantaBot',
 'ceres993434/PornHubBot',
 'CodeXBotz/File-Sharing-Bot',
 'azamaulanaaa/botkaca',
 'joeldg/bowhead',
 'Drakkar-Software/OctoBot',
 'The-HellBot/HellBot',
 'jef/streetmerchant',
 'yasinkuyu/binance-trader',
 'leochen-g/wechatBot',
 'jw84/messenger-bot-tutorial',
 'infracloudio/botkube',
 'natewong1313/bird-bot',
 'stark666/smzdm_bot',
 'line/line-bot-sdk-java',
 'DevsExpo/FridayUserbot',
 'EmirhanSarac/discord-altyapi-bot',
 'botfront/botfront',
 'microsoft/botbuilder-dotnet',
 'cixingguangming55555/wechat-bot',
 'hangoutsbot/hangoutsbot',
 'tyzlmjj/PagerBottomTabStrip',
 'botgram/shell-bot',
 'DedSecInside/TorBot',
 'Jijinr/Filter-Bot',
 'Ice-Cirno/HoshinoBot',
 'freqtrade/freqtrade-strategies',
 'lefnire/tforce_btc_trader',
 'ergunemr/BottomPopup',
 'microsoft/BotBuilder-CognitiveServices',
 'maxbbraun/trump2cash',
 'hackerkid/bots',
 'ExtropyIO/defi-bot',
 'line/line-bot-sdk-php',
 'Kennyc1012/BottomSheetMenu',
 'slackapi/easy-peasy-bot',
 'Mahesh0253/Media-Search-bot',
 'Strip3s/PhoenixBot',
 'jagrosh/Vortex',
 'lyfe00011/whatsapp-bot',
 'nickoala/telepot',
 'NotReallyShikhar/YukkiMusicBot',
 'Bitwise-01/YouTubeViews-',
 'afnanplk/Pinky',
 'rubensousa/BottomSheetBuilder',
 'hungtraan/FacebookBot',
 'sbp/phenny',
 'PhantomBot/PhantomBot',
 'botlabs-gg/yagpdb',
 'brianzhouzc/RocketBot',
 'aryanvikash/Google-Drive-Uploader',
 'rhiever/TwitterFollowBot',
 'ianw/bottomupcs',
 'MiuLab/TC-Bot',
 'OfficeDev/BotBuilder-MicrosoftTeams',
 'Curzibn/BottomDialog',
 'AnimeKaizoku/SaitamaRobot',
 'tmobile/pacbot',
 'ClementTsang/bottom',
 'galnir/Master-Bot',
 'flashbots/simple-arbitrage',
 'pengrad/java-telegram-bot-api',
 'QueenArzoo/VCPlayBot',
 'AnIdiotsGuide/discordjs-bot-guide',
 'gorhom/react-native-bottom-sheet',
 'chalda/DiscordBot',
 'ehForwarderBot/ehForwarderBot',
 'TheHamkerCat/Telegram_VC_Bot',
 'alavers/smooch-bot-example',
 'aeon0/botty',
 'xditya/TeleBot',
 'TroJanzHEX/Unlimited-Filter-Bot',
 'remixz/messenger-bot',
 'peteanderson80/bottom-up-attention',
 'Nafidinara/bot-pancakeswap',
 'TannerGabriel/discord-bot',
 '7dog7/bottleneckOsmosis',
 'esbenp/pdf-bot',
 'BitBotFactory/MikaLendingBot',
 'botcrypto-io/awesome-crypto-trading-bots',
 'alexschimpf/Snkrs-Bot',
 'Roibal/Cryptocurrency-Trading-Bots-Python-Beginner-Advance',
 'CrazyBotsz/Adv-Auto-Filter-Bot-V2',
 'hartleybrody/fb-messenger-bot',
 'xMistt/fortnitepy-bot',
 'Flam3rboy/discord-bot-client',
 'FeezyHendrix/Insta-mass-account-creator',
 'claudiajs/claudia-bot-builder',
 'No-OnE-Kn0wS-Me/FileRenameBot',
 'adonespitogo/AdoBot',
 'kkyon/botflow',
 'vesln/bot',
 'MyBotRun/MyBot',
 'android-cjj/BottomSheets',
 'dappuniversity/price-bot',
 'CyberPunkMetalHead/Binance-News-Sentiment-Bot',
 'mitchellkrogza/nginx-ultimate-bad-bot-blocker',
 'osdnk/react-native-reanimated-bottom-sheet',
 'out386/aria-telegram-mirror-bot',
 'indes/flowerss-bot',
 'patheticGeek/torrent-aio-bot',
 'bottlesdevs/Bottles',
 'microsoft/botbuilder-tools',
 'microsoft/botbuilder-js',
 'metalmatze/alertmanager-bot',
 'confluentinc/bottledwater-pg',
 'YogaSakti/imageToSticker',
 'line/line-bot-sdk-nodejs',
 'freyacodes/archived-bot',
 'bwentzloff/trading-bot',
 'cinchrb/cinch',
 'dappuniversity/trading-bot',
 'Tomato6966/Multipurpose-discord-bot',
 'botwillacceptanything/botwillacceptanything',
 'binary-com/binary-bot',
 'rampatra/jbot',
 'CharlieHess/slack-poker-bot',
 'Omkar47/AutoLeecher',
 'poketwo/poketwo',
 'kanjielu/jeeves',
 'dewango/BottomNavigationBarXF',
 'lionheart/bottlenose',
 'TKperson/Nuking-Discord-Server-Bot-Nuke-Bot',
 'ruCyberPoison/-Mirai-Iot-BotNet',
 'LeoWuVinci/agar.io-bot',
 'ShailChoksi/lichess-bot',
 'vincreator/eunhamirror',
 'rmmh/skybot',
 'Necrobot-Private/NecroBot',
 'kjeymax/GDUPLOAD_BOT2',
 'odysseusmax/animated-lamp',
 'reminder-bot/bot',
 'souravkl11/Raganork',
 'odysseusmax/utube',
 'TCF-BOT-ALGERIE/BOT',
 'AsmSafone/VideoPlayerBot',
 'gaowanliang/DownloadBot',
 'jagrosh/GiveawayBot',
 'microsoft/botbuilder-python',
 'Spiderjockey02/Discord-Bot',
 'ibrahimsn98/SmoothBottomBar',
 'Eleirbag89/TelegramBotPHP',
 'splunk/botsv1',
 'CloudBotIRC/CloudBot',
 'pskrunner14/trading-bot',
 'KevinLage/YouTube-Livestream-Botter',
 'Nouridio/Discord-bot-website-template',
 'MsGsuite/CloneBot_Heroku',
 'Bottr-js/Bottr',
 'tuhinpal/WhatsBot',
 '1Danish-00/CompressorBot',
 'joaoricardo000/whatsapp-bot-seed',
 'microsoft/BotFramework-DirectLineJS',
 'telegram-rs/telegram-bot',
 'sabattle/CalypsoBot',
 'Nadyatjia/BotLinePython3',
 'NotSoSuper/NotSoBot',
 'MicrosoftDocs/bot-docs',
 'SlavyanDesu/BocchiBot',
 'watson-developer-cloud/botkit-middleware',
 'jamesblasco/modal_bottom_sheet',
 'Ekliptor/WolfBot',
 'amfoss/bot',
 'askmike/gekko',
 'adeshpande3/Facebook-Messenger-Bot',
 'jagrit007/Telegram-CloneBot',
 'opsdroid/opsdroid',
 'slack-ruby/slack-ruby-bot',
 'adidoank/buzz',
 'LittleFriendsGroup/BottomNavigation',
 'poshbotio/PoshBot',
 'superscriptjs/superscript',
 'young-steveo/bottlejs',
 'mishk0/slack-bot-api',
 'Tsuk1ko/cq-picsearcher-bot',
 'TheHamkerCat/WilliamButcherBot',
 'bananiumbot/bot',
 'raphaelbussa/BottomDialog',
 'aws-samples/aws-lex-web-ui',
 'yjose/twitter-bot',
 'pydata/bottleneck',
 'Black-Triangle-code/Telegram_coin_bot',
 'davechurchill/commandcenter',
 'jabbink/PokemonGoBot',
 'armcha/LuseenBottomNavigation',
 'w3c-lbd-cg/bot',
 'w3c-lbd-cg/bot',
 'SpEcHiDe/AnyDLBot',
 'ParkSangGwon/TedBottomPicker',
 'LucasMucGH/BottomSheet',
 'atipugin/telegram-bot-ruby',
 'witnessmenow/Universal-Arduino-Telegram-Bot',
 'oneHamidreza/MeowBottomNavigation',
 'ciro-unity/BotW-ToonShader',
 'TelegramBot/Api',
 'CyberPunkMetalHead/binance-trading-bot-new-coins',
 'Charca/bootbot',
 'pocheshire/BottomNavigationBar',
 'Kylmakalle/heroku-telegram-bot',
 'EverythingSuckz/TG-FileStreamBot',
 'shomali11/slacker',
 'iterativv/NostalgiaForInfinity',
 'codeforequity-at/botium-core',
 'RoyWallace/BottomNavigationBar',
 'groupme/bot-tutorial-nodejs',
 'Dragory/modmailbot',
 'qhutch/BottomSheetLayout',
 'Karumi/BothamUI',
 'atlasbot/bot',
 'miguelhincapie/CustomBottomSheetBehavior',
 'pedromassango/bottom_navy_bar',
 'ChristopherBThai/Discord-OwO-Bot',
 'edwardhdlu/q-trader',
 'iyear/E5SubBot',
 'CiscoDevNet/botkit-template',
 'Mantaro/MantaroBot',
 'aviddot/Pancakeswap-and-uniswap-trading-bot',
 'AbirHasan2005/PyroFilesStoreBot',
 'SebOuellette/LiveBot',
 'Malexion/Rhythm-Bot',
 'subinps/Instagram-Bot',
 'Xinz-Team/XinzBot',
 'saniales/golang-crypto-trading-bot',
 'line/line-bot-sdk-go',
 'php-telegram-bot/example-bot',
 'Khanmanan/automod-bot',
 'xHak9x/fbi',
 'jesse-ai/jesse',
 'splunk/botsv2',
 'TobyG74/ElainaBOT',
 'threatland/TL-BOTS',
 'gillesheinesch/LenoxBot',
 'taniman/profit-trailer',
 'a04512/Front-RunBot',
 'arghyac35/aria-telegram-mirror-bot',
 'SaturnsVoid/GoBot2',
 'HeyAlex/BottomDrawer',
 'hengyuan-hu/bottom-up-attention-vqa',
 'SGrondin/bottleneck',
 'microsoft/BotBuilder-Location',
 'loqix/BottlEye',
 'Bintang73/botst4rz',
 'inCaller/prometheus_bot',
 'pimax/fb-messenger-php',
 'backmeupplz/voicy',
 'linksplatform/Bot',
 'Gravebot/Gravebot',
 'TheSharks/WildBeast',
 'kingideayou/SlideBottomPanel',
 'semicons/java_oci_manage',
 'TelegramBots/Telegram.Bot.Examples',
 'Sorajz/line-bot-exam-php',
 'chadrem/market_bot',
 'MobBotTeam/PokeMobBot',
 'kiruto/debug-bottle',
 'microsoft/BotBuilder-Azure',
 'microsoft/botframework',
 'IVETRI/SongPlayRoBot',
 'kolton/d2bot-with-kolbot',
 'eggheads/eggdrop',
 'MoveAngel/One4uBot',
 'lushaimusic/VCsMusicBot',
 'BeepIsla/csgo-commend-bot',
 'DeltaCoderr/KarmaBot',
 'AnandaRauf/BotacsPro---Bot-Auto_Checkout-Flashsale-Shopee-Promo',
 'michaelbel/BottomSheet',
 'zeeoneofc/Haruka',
 'aj-4/tinder-swipe-bot',
 'RasaHQ/financial-demo',
 'shantnu/RedditBot',
 'cyberkallan/inshackle-bot',
 'Anorov/cloudflare-scrape',
 'paulpierre/informer',
 'UnityTechnologies/AngryBots_ECS',
 'greedisgoood/botbay',
 'rubenlagus/TelegramBotsExample',
 'Forden/aiogram-bot-template',
 'strorinWind/bot',
 'Naltox/telegram-node-bot',
 'Teahouse-Studios/bot',
 'Appeza/tg-mirror-leech-bot',
 'MShawon/YouTube-Viewer',
 'CiKu370/OSIF',
 'meepen/salien-bot',
 'leaderj1001/BottleneckTransformers',
 'REVENGE977/Discord-Bots-Hack',
 'paulpierre/informer',
 'Bluefissure/OtterBot',
 'MShawon/YouTube-Viewer',
 'tunitowen/fancy_bottom_navigation',
 'AlexFlipnote/discord_bot.py',
 'Clinton-Abraham/UPLOADER-BOT',
 'freeCodeCamp/100DaysOfCode-twitter-bot',
 'bors-ng/bors-ng',
 'microsoft/HealthBotContainerSample',
 'SAPConversationalAI/SAPConversationalAI',
 'cheran-senthil/TLE',
 'WhiteHouse/fb_messenger_bot',
 'DeviaVir/zenbot',
 'phonegapX/QuantBot',
 'etherdelta/bots',
 'iammert/ReadableBottomBar',
 'ThePhoDit/ModMail',
 'AgusAliansyah/vvipbot-wa',
 'Barsik008/PossumBot',
 'nodejs/github-bot',
 'pajbot/pajbot',
 'SpikeKing/BottomDialogDemo',
 'dkhamsing/awesome_bot',
 'smarkets/marge-bot',
 'theriley106/SneakerBotTutorials',
 'fuselabs/echobot',
 'reo7sp/tgbot-cpp',
 'Hoektronics/BotQueue',
 'cranklin/Instagram-Bot',
 'stonexer/wechatBot',
 'TobyG74/BotToby',
 'AcademicDog/onmyoji_bot',
 'hitherejoe/BottomNavigationViewSample',
 'zeeoneofc/BOTZ10a',
 'J-Rios/TLG_JoinCaptchaBot',
 'NeKosmic/NK-BOT',
 'r7kamura/ruboty',
 'MMMzq/bot_toast',
 'SpEcHiDe/PyroGramBot',
 'natario1/BottomSheetCoordinatorLayout',
 'BilalShahid13/PersistentBottomNavBar',
 'brucevanfdm/BottomNavigationView',
 'jaisonfdo/BottomNavigation',
 'germanattanasio/text-bot',
 'hikaruAi/FacebookBot',
 'xTCry/VCoin',
 'NNTin/discord-twitter-bot',
 'CharmingDays/kurusaki_voice',
 'CrazyBotsz/Adv-Auto-Filter-Bot',
 'paco0x/amm-arbitrageur',
 'nysamnang/react-native-raw-bottom-sheet',
 'fabston/TradingView-Webhook-Bot',
 '546669204/RebateBot',
 'topkecleon/telegram-bot-bash',
 'evil-mad/EggBot',
 'telegram-bot-rb/telegram-bot',
 'alfficcadenti/splinterlands-bot',
 'nodeWechat/wechat4u',
 'tucnak/telebot',
 'CarlGroth/Carl-Bot',
 'grapeot/WechatForwardBot',
 'googleworkspace/hangouts-chat-samples',
 'GreyWolfDev/Werewolf',
 'abdelhai/awesome-bots',
 'mdgspace/bot',
 'Sank6/Discord-Bot-List',
 'samc621/SneakerBot',
 'boto/boto3-sample',
 'huseinzol05/Stock-Prediction-Models',
 'SAPConversationalAI/Webchat',
 'soumyadityac/youtube-viewer',
 'CodeWithJoe2020/pancakeswapBot',
 'Merubokkusu/discord-spam-bots',
 'ZeroDiscord/EconomyBot',
 'scrapinghub/slackbot',
 'baidu/boteye',
 'kcloze/swoole-bot',
 'hyperchessbot/hyperbot',
 'yangyuan/hearthrock',
 'agermanidis/SnapchatBot',
 'brompwnie/botb',
 'thedevs-network/the-guard-bot',
 'jqs7/Jqs7Bot',
 'AdeelMufti/CryptoBot',
 'aracred/bot',
 'zeldaret/botw',
 'jh0ker/mau_mau_bot',
 'coq/bot',
 'sandimetz/1st_99bottles_ruby',
 'jsdelivr/bot',
 'mgp25/Telegram-Bot-API',
 'kereh/BOT',
 'MafiaBotOP/MafiaBot',
 'cloggy45/Gekko-Bot-Resources',
 'avipatilpro/FileStreamBot',
 'DalinMathew/AutoFilterBotV3',
 'seregazhuk/php-pinterest-bot',
 'RayzrDev/SharpBot',
 'tommybuonomo/morph-bottom-navigation',
 'jackpoz/BotFarm',
 'd-haxton/HaxtonBot',
 'tommybuonomo/morph-bottom-navigation',
 'Spandan-Madan/Me_Bot',
 'Bambooir/TeleSeed',
 'AbirHasan2005/Watermark-Bot',
 'kukume/kukubot',
 'SeanDaBlack/KelloggBot',
 'dsgriffin/opensea-sales-twitter-bot',
 'Siterizer/new-world-fishing-bot',
 'rameshkec85/BottomTabsFragmentTabHost',
 'dariusk/examplebot',
 'Agantor/viewerbot',
 'AbirHasan2005/Rename-Bot',
 'dtcarls/fantasy_football_chat_bot',
 'terry-fei/wechat-bot',
 'TG-Musics/Telegram_Vc_Bot',
 'TroJanzHEX/Auto-Filter-Bot-V2',
 'ChameleonBot/Bot',
 '0xEssential/opensea-discord-bot',
 'LyoSU/quote-bot',
 'discord-akairo/discord-akairo',
 'norecha/pokubot',
 'Splamy/TS3AudioBot',
 'Blankeer/WechatBotXposed',
 'alfonsrv/impf-botpy',
 'microsoft/AzureBot',
 'fccaikai/BottomMenuTutorial',
 'twtrubiks/line-bot-tutorial',
 'cesardeazevedo/react-native-bottom-sheet-behavior',
 'altf4/SmashBot',
 'Itz-fork/Mega.nz-Bot',
 'azlux/botamusique',
 'viperadnan-git/force-subscribe-telegram-bot',
 'plutov/bot',
 'DGXeon/DogeBot',
 'TroJanzHEX/Auto-Filter-Bot',
 'VikParuchuri/apartment-finder',
 'dxxoo/HisokaBOT-Whatsapp-Bot',
 'PokemonGoF/PokemonGo-Bot-Desktop',
 'carlos8f/bot18',
 'adib2149/BottomNavBar',
 'xhrvan/EvilBot',
 'mxssl/tg-captcha-bot',
 'ryantcullen/stock-bot',
 'adamfootdev/BottomSheet',
 'Falconerd/discord-bot-github',
 'AbirHasan2005/VideoCompress',
 'BotBotMe/botbot-bot',
 'Viir/bots',
 'zu1k/tg-keyword-reply-bot',
 'jakubroztocil/cointrol',
 'finn-no/BottomSheet',
 'BeyondTeam/Self-BotV1',
 'hacktons/convex_bottom_bar',
 'JettBurns14/super-super-heroku-bot',
 '6eer/uniswap-sushiswap-arbitrage-bot',
 'tgcallsjs/LemonJamsBot',
 'line/line-bot-sdk-ruby',
 'aws-samples/amazon-lex-bi-bot',
 'Droppers/AnimatedBottomBar',
 'fritx/wxbot',
 'FloatTech/ZeroBot-Plugin',
 'indianbhaiya/IndianBot',
 'SAPConversationalAI/bot-connector',
 'deStrO/eBot-CSGO',
 'cyz/Maratona-BOTs',
 'MinusKelvin/cold-clear',
 'Naval-Base/yuudachi',
 'lorcalhost/BTB-manager-telegram',
 '666wcy/ARPT-Bot',
 'kolar/telegram-poll-bot',
 'mitchellkrogza/apache-ultimate-bad-bot-blocker',
 'szastupov/musicbot',
 'shitcorp/discord-bot-dashboard',
 'bufferapp/AdaptableBottomNavigation',
 'ahmad-elassuty/BottomSheetController',
 'Rapptz/RoboDanny',
 'VeNoMouS/cloudscraper',
 'BotBuilderCommunity/botbuilder-community-dotnet',
 'timomeh/react-native-material-bottom-navigation',
 'botgram/botgram',
 'AnimeKaizoku/EnterpriseALRobot',
 'rougeth/bottery',
 'microsoft/BotBuilder-V3',
 '2018kguo/RobinhoodBot',
 'PandoraMedia/BottomNavigator',
 'Ns-Bots/TG-RENAMER-BOT',
 'piebotai/bot',
 'voussoir/reddit',
 'eljojo/telegram_bot',
 'stevschmid/track-o-bot',
 'xditya/BotStatus',
 'kwsch/SysBot.NET',
 'Makeblock-official/mDrawBot',
 'vishakha-lall/MapBot',
 'sdslabs/bot',
 'howdyai/botkit-starter-slack',
 'dotnet-architecture/eShopOnContainersAI',
 'dueros/bot-sdk-node.js',
 'Har-Kuun/DomainMegaBot']

headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        if "language" not in repo_info:
            raise Exception(
                "'language' key not round in response\n{}".format(json.dumps(repo_info))
            )
        return repo_info["language"]
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_download_url = get_readme_download_url(contents)
    if readme_download_url == "":
        readme_contents = ""
    else:
        readme_contents = requests.get(readme_download_url).text
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data() -> List[Dict[str, str]]:
    """
    Loop through all of the repos and process them. Returns the processed data.
    """
    return [process_repo(repo) for repo in REPOS]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data.json", "w"), indent=1)

 