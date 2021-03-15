
#here is the file for builder tool
#instead of directly creating a TextField in main, import strings that act as commands for TextField

num_helper = '''
MDTextField:
    hint_text: "Enter number"
    helper_text: "Format: Country Code and Number"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.75}
    size_hint_x: None
    width: 300
'''

sms_helper = '''
MDTextField:
    hint_text: "Enter sms"
    helper_text: "Write or paste the message here"
    helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    size_hint_x: None
    width: 300
'''