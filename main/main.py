	from ota_update.main.ota_updater import OTAUpdater


    def download_and_install_update_if_available():
        o = OTAUpdater('https://github.com/ulprperera/ESP32py')
        o.download_and_install_update_if_available('RNA', 'Welcome2018!')


    def start():
        # your custom code goes here. Something like this: ...
        # from main.x import YourProject
        # project = YourProject()
        # ...		
		print ("ESP32 PICO Core says Hello Roshan")


    def boot():
        download_and_install_update_if_available()
        start()


    boot()