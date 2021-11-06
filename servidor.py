#Copia del original
import re
import random
from time import sleep
import pyttsx3
from threading import Thread

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate',150)


def get_response(user_input):
    split_message = re.split(r'\s|[,.-;:_*!"#$%&/()=?]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognzed_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognzed_words:
            message_certainty += 1
    
    percentage = float(message_certainty) / float(len(recognzed_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hello', ['hello', 'hi'], single_response=True)
        response('fine, and you?', ['how', 'are', 'you', 'about', "you're"], required_words=['you'])
        response("that's fine", ["i'm", 'i', 'am', 'good', 'fine'], required_words=['i'])
        response("Investing should be started by doing your research and finding assets that you can commit to, once that's done- you need to follow 1 principle. *lay out cash today to get more back in the future.", ['how','do','you','start','investing', 'i','can'], required_words=['how'])
        response('To get rich in the stock market, you need patience and emotional stability- buy sound businesses at fair prices and watch your money grow.',['how', 'do','i','you','can', 'get','rich','the','stock','market','with', 'stonks'],required_words=['how'])
        response('sure, you just have to know what you are doing',['i','can','me','rich','stock','stock','with','market'], required_words=['me'])
        response("To beat the market, you have to out learn everyone- the person who knows the most wins in investing.", ['how','do','i','you','can','beat','market'], required_words=['how','beat'])
        response("You can make money in 3-5 years, yet the stock market rewards those who can hold for 10+ years.", ['how','fast','can','i','you','money','rich','market','stock','stock', 'time'], required_words=['how'])
        response("You can make money in 3-5 years, yet the stock market rewards those who can hold for 10+ years.", ['how','fast','can','i','you','money','rich','market','stock','stock', 'time'], required_words=['soon'])
        response("To analyze a stock, use the annual report and simplify everything to understand the future of the company", ['how','do','you','i','analyse','stock','market'],required_words=['analyse'])
        response("To not lose money, apply a margin of safety in the business- the difference between price and value.",['how','do','you','i','lose','money','should','have','stock','stocks'],required_words=['lose'])
        response("Common mistakes: selling to early, speculating and listening to outside jargon.",['what', 'mistakes','i','you','do','should','can´t','stock','stocks','market', 'avoid'], required_words=['mistakes'])
        response("It is hard to invest, yet it is simple- read annual reports to make it easier.",['how','hard','is','it','invest','stock','stocks'],required_words=['invest'])
        response("You should approach stocks with a long term mindset and a temperament that allows you to go through 1000's of stocks before investing.",['how','should','you','i','approach','stock','stocks','market','do','can'], required_words=['approach'])
        response("You get the most out of investing by being patient and letting compound interest kick in.",['how','can','i','you','get','value','of','investing', 'stock','stocks','market'],required_words=["how"])
        response("The best positioning is to understand business and you make money.",['how','do','i','you','position','yourself','myself','make','with','stocks'], required_words=['position'])
        response("Diversification should only be done if it does not reduce your over all expected rate of return.",['how','to','diversify','i','you','can','do','stock'], required_words=['diversify'])
        response("The best way to learn about stocks is to understand business and the future economic characteristics of companies.",['how','i','you','learn','about','stock','stocks','can','do'], required_words=['learn'])
        response("The best way to understand a stock is to predict the future economic characteristics of the company through the financial data in the annual report.",['what','wich','way','understand','can','i','you','stock','stocks','best','market'],required_words=['what'])
        response("Stocks are good because they allow you to apply logic and grow money at a.",['what','makes','stocks','stock','market','good',], required_words=['good'])
        response("Stocks are simply the best long term investment, if you are patient- stocks will serve as the best long term investment.",['why','reason','invest','in','i','you','should','stock','stocks','market','other','investments','over'], required_words=['why'])
        response("The purpose of stocks is not to just make money, it is to apply your understanding of businesses and take a calculated chance at predicting the future of the bussiness.",['what','purpose','objective','investments','stock','stocks','market','is','i','you','should'],required_words=['what'])
        response("To invest safely, go with index funds- they are simple and they work.",['how', 'i','can','you','do','invest','safely','stock','stocks','market'], required_words=['invest'])
        response("To maximise stock market returns, buy cheap- find value and let compound interest play it's part.",['how','maximise','i','can','you','do','to','return','market','stock','stocks'], required_words=['how'])
        response("Money is lost due to impulsive action, speculation and the ability to not think with clarity or think independently.",['what','are','why','i','people','lose','money','stock','stocks','market','in','causes','the'], required_words=['what'])
        global best_match  
        best_match = max(highest_prob, key=highest_prob.get)

        # print(highest_prob,"\n")
        def fun():
            print('AI: ')
            for x in best_match:
                print(x,end='', flush=True)
                sleep(0.05)
        def el():
            engine.say(best_match)
            engine.runAndWait()

        if highest_prob[best_match] < 1:
            pass 
        else:
            Thread(target = el).start()
            Thread(target = fun).start()    

def unknow():
    response = ['i don´t understand you, try again please',"please, be more clearer", "try it again"][random.randrange(3)]
    return response

get_response(input('you: '))