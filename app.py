from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import json
from collections import namedtuple


class QuizBot:
    def __init__(self):
        self.bot = webdriver.Firefox()
        #self.bot = webdriver.Chrome()
        with open('data.json') as json_file:
            self.data = json.load(json_file, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    def startQuiz(self):
        bot = self.bot
        data = self.data
        bot.get('https://www.stagecast.io/')
        time.sleep(3)

        quizCode = bot.find_element_by_name('code')
        quizCode.clear()
        quizCode.send_keys('8483')
        enterButton = bot.find_element_by_xpath("//input[@type='submit']")  
        enterButton.send_keys(Keys.RETURN)
        time.sleep(5)
        bot.switch_to.frame("frame")
        legalCheckBox = bot.find_element_by_class_name('mc-checkmark')
        legalCheckBox.click()
        time.sleep(1)
        legalButton = bot.find_element_by_class_name('main-button')
        time.sleep(1)
        legalButton.click()

        time.sleep(1)
        nameInput = bot.find_element_by_class_name('name-input')
        nameInput.clear()
        nameInput.send_keys('Mateusz')
        time.sleep(1)
        startButton = bot.find_element_by_class_name('custom-button')
        startButton.click()
        time.sleep(7)
        while len(bot.find_elements_by_class_name('question')) > 0:
            i = 0
            question = bot.find_element_by_class_name('question-text').get_attribute("innerHTML").splitlines()[0]
            for obj in data:
                if  obj.question == question :
                    answer = bot.find_element_by_xpath("//span[text()=' "+obj.answer+" ']")
                elif i >= len(data):
                    answer = bot.find_element_by_class_name('choice')
        
            answer.click()
            time.sleep(1.2)

test = QuizBot()

test.startQuiz()