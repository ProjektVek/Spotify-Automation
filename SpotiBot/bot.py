from botcity.web import WebBot, Browser
# import os
# from dotenv import load_dotenv 
# Importing dotenv files read
from decouple import config
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

class Bot(WebBot):
    def action(self, execution=None):
        # Configure whether or not to run on headless mode
        self.headless = False

        
        # Uncomment to change the default Browser to Chrome
        # self.browser = Browser.CHROME
        
        # Define your driver path
        self.driver_path = "C:/Users/Victor/Documents/GitHub/My Projects/Spotify Automation/My Bot/SpotiBot/drivers installation/drivers/chromedriver.exe"

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.browse("https://open.spotify.com/")
        
        # Changing windows size:
        # maximize_window(self)
        self.set_screen_resolution(1280, 720)
        
        # logging in
        self.wait(1000)
        self.login()

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )
        
        
        self.wait(1000)
        
        #If you are listening on desktop (using the bot to mute via web app), set this to True
        listening_on_desktop = True
        
        # if listening_on_desktop:
        #     self.maximize_window()
            
        # Muting/Unmuting and Skipping Ad
        # print('pre-loop')
        continue_loop = True
        
        
        while continue_loop:

            try:
                self.mute_ad(listening_on_desktop)
            except:
                pass
    
        # print('POST-LOOP')       

        # Wait for ??? seconds before closing
        self.wait(9999999)

        # Stop the browser and clean up
        self.stop_browser()

    def not_found(self, label):
        # print(f"Element not found: {label}")
        pass
    """
        #Search on feeling lucky
    def feeling_lucky_click(self):
        self.paste("Shall never Surrender")
        
        if not self.find( "button", matching=0.97, waiting_time=10000):
            self.not_found("button")
        self.click()
    """
    
    # Login Script
    def login(self):
        # click on login in the unlogged spotify web area
        if not self.find( "button_login_access", matching=0.97, waiting_time=10000):
            self.not_found("button_login_access")
        self.click()

        # Loading USER_LOGIN and USER_PASSWORD on .env file
        USER_LOGIN = config('USER_LOGIN')
        USER_PASSWORD = config('USER_PASSWORD')

        # logging in
        self.wait(1000)
        self.paste(USER_LOGIN)
        self.tab()
        self.paste(USER_PASSWORD)
        self.enter()
        
        return
        
    # mute audio command
    def mute(self):
        if not self.find( "mute", matching=0.97, waiting_time=100):
            self.not_found("mute")
        self.click()
        
    def unmute(self):
        if not self.find( "unmute", matching=0.97, waiting_time=100):
            self.not_found("unmute")
        self.click()
    
    def maximize_volume(self):
        try:
            self.web_maximize_volume(),
        except:
            pass
        try:
            self.desktop_maximize_volume(),
        except:
            pass
        
    def click_bar(self):
       if not self.find( "volume_bar", matching=0.5, waiting_time=100):
            self.not_found("volume_bar")
       self.click()
       
    def desktop_maximize_volume(self):
        if not self.find( "remote_icon", matching=0.97, waiting_time=1):
            self.not_found("remote_icon")
        self.click_relative(147, 7)
   
    def web_maximize_volume(self):
        if not self.find( "volume_mid", matching=0.97, waiting_time=1):
            self.not_found("volume_mid")
        self.click_relative(147, 5)
            
    def reduce_volume(self):
        if not self.find( "reduce_volume", matching=0.97, waiting_time=200):
            self.not_found("reduce_volume")
        self.click_relative(33, 7)

    def mute_ad(self,skip=False):
        if self.find_ad():
            self.mute()
            if skip:
                self.skip_music()
        else:
            self.demute_music()

    def demute_music(self):
        if not self.find_ad():
            self.maximize_volume()
    
    # verifying if is unmuted
    def is_unmuted(self):
        is_unmuted = False
        if not self.find( "mute", matching=0.97, waiting_time=100):
            self.not_found("mute")
        else:
            is_unmuted = True
        return is_unmuted
    
    def is_muted(self):
        muted = False
        if not self.find( "muted", matching=0.97, waiting_time=100):
            self.not_found("muted")
        else:
            muted = True
        return muted
        
    # skip music command
    def skip_music(self):
        try:
            if not self.find( "skip", matching=0.97, waiting_time=100):
                self.not_found("skip")
            self.click() # Click and wait 3 seconds
            # print('SKIP AD')
        except:
            pass
    
    # finding when can't skip
    # DONT USE: not working properly
    def find_skip_block(self):
        skip_blocked = False
        if not self.find( "skip_blocked", matching=0.97, waiting_time=100):
            self.not_found("skip_blocked")
        else:
            skip_blocked = True
        return skip_blocked
            
    # identifying ad
    def find_ad(self):
        ad_playing = False
        try:
            if not self.find( "spotify_ad", matching=0.97, waiting_time=100):
                self.not_found("spotify_ad")
            else:
                ad_playing = True
                return ad_playing
        except:
            pass

        try:    
            if not self.find( "ad_signal", matching=0.97, waiting_time=100):
                self.not_found("ad_signal")
            else:
                ad_playing = True
                return ad_playing
        except:
            pass
        
        return ad_playing
    
if __name__ == '__main__':
    Bot.main()



























































