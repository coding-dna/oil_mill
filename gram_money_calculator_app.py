import streamlit as s

s.title("Gram/Money Calculator")

def paisa():
    rate = s.number_input(label = "रेट प्रति केजी", value = None)
    weight = s.number_input(label = "वजन ग्राम में", value = None)
    if s.button("कितने पैसे बनते हैं?"):
        s.write(f"आपके {-((-rate*weight)//1000)} रुपये बनते हैं।")

def gram():
    rate = s.number_input(label = "रेट प्रति केजी", value = None)
    rupee = s.number_input(label = "कितने रुपये का तेल लेना चाहेंगे?", value = None)
    if s.button("कितना ग्राम तेल देना हैं?"):
        s.write(f"आपको {rupee//(rate/1000)} ग्राम तेल देना हैं।")

activity = s.sidebar.radio(label = "आप क्या निकालना चाहेंगे?",options = ["पैसा","ग्राम"])

if activity == "पैसा":
    paisa()

if activity == "ग्राम":
    gram()
